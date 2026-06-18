// Cloudflare Pages Function — contact form handler.
// Route: POST /api/contact  (GET /contact still serves the static contact.html page)
//
// Sends submissions via the Resend HTTP API (works in the Pages Functions runtime;
// raw SMTP is not available in Workers). Required env vars (set in the Cloudflare
// Pages dashboard → Settings → Environment variables):
//   RESEND_API_KEY   — Resend API key (https://resend.com/api-keys)
//   CONTACT_TO        — destination address (default: jdm@isn.biz)
//   CONTACT_FROM      — verified sender on a Resend-verified domain
//                       (default: "iSN.BiZ Contact <contact@isn.biz>"; isn.biz must be
//                        verified in Resend for delivery)
//
// Until RESEND_API_KEY is set the endpoint returns HTTP 503 with a clear message,
// so the form degrades visibly rather than silently dropping mail.

const JSON_HEADERS = { 'Content-Type': 'application/json; charset=utf-8' };

function json(body, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: JSON_HEADERS });
}

function escapeHtml(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

export async function onRequestPost(context) {
  const { request, env } = context;

  // Parse either form-encoded or JSON bodies
  let data = {};
  try {
    const ct = request.headers.get('content-type') || '';
    if (ct.includes('application/json')) {
      data = await request.json();
    } else {
      const form = await request.formData();
      for (const [k, v] of form.entries()) data[k] = v;
    }
  } catch {
    return json({ ok: false, error: 'Could not parse request body.' }, 400);
  }

  // Honeypot — bots fill hidden fields; humans don't. Pretend success, send nothing.
  if (data._gotcha) return json({ ok: true });

  const name = (data.name || '').toString().trim();
  const email = (data.email || '').toString().trim();
  const message = (data.message || '').toString().trim();

  // Validation
  if (!name || !email || !message) {
    return json({ ok: false, error: 'Name, email, and message are required.' }, 422);
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return json({ ok: false, error: 'Please provide a valid email address.' }, 422);
  }
  if (message.length > 8000) {
    return json({ ok: false, error: 'Message is too long.' }, 422);
  }

  const apiKey = env.RESEND_API_KEY;
  if (!apiKey) {
    return json(
      { ok: false, error: 'Contact backend is not yet configured. Please email info@isn.biz directly.' },
      503,
    );
  }

  const to = env.CONTACT_TO || 'jdm@isn.biz';
  const from = env.CONTACT_FROM || 'iSN.BiZ Contact <contact@isn.biz>';

  const fields = ['company', 'phone', 'interest', 'budget', 'timeline'];
  const extra = fields
    .filter((f) => data[f])
    .map((f) => `<tr><td style="padding:4px 12px 4px 0;font-weight:bold;">${escapeHtml(f)}</td><td>${escapeHtml(data[f])}</td></tr>`)
    .join('');

  const html = `
    <h2>New contact form submission — isn.biz</h2>
    <table style="border-collapse:collapse;font-family:sans-serif;font-size:14px;">
      <tr><td style="padding:4px 12px 4px 0;font-weight:bold;">Name</td><td>${escapeHtml(name)}</td></tr>
      <tr><td style="padding:4px 12px 4px 0;font-weight:bold;">Email</td><td>${escapeHtml(email)}</td></tr>
      ${extra}
    </table>
    <h3>Message</h3>
    <p style="white-space:pre-wrap;font-family:sans-serif;font-size:14px;">${escapeHtml(message)}</p>
  `;

  try {
    const resp = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from,
        to: [to],
        reply_to: email,
        subject: `Contact form: ${name}${data.company ? ` (${data.company})` : ''}`,
        html,
      }),
    });

    if (!resp.ok) {
      const detail = await resp.text().catch(() => '');
      return json({ ok: false, error: 'Email delivery failed. Please email info@isn.biz directly.', detail: detail.slice(0, 300) }, 502);
    }
    return json({ ok: true });
  } catch (e) {
    return json({ ok: false, error: 'Network error sending message. Please email info@isn.biz directly.' }, 502);
  }
}

// Reject non-POST methods explicitly (GET /api/contact has no static fallback).
export async function onRequest(context) {
  if (context.request.method === 'POST') return onRequestPost(context);
  return json({ ok: false, error: 'Method not allowed.' }, 405);
}
