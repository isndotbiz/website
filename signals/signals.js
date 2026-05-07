// ISN Signals — public dashboard renderer

const DATA_URL = "data/signals-30d.json";
const TABLE_LIMIT = 100;

const fmtPct = (v) => {
    if (v === null || v === undefined || Number.isNaN(v)) return null;
    const n = Number(v);
    return (n >= 0 ? "+" : "") + (n * 100).toFixed(2) + "%";
};

const pctClass = (v) => {
    if (v === null || v === undefined || Number.isNaN(v)) return "ret-na";
    return Number(v) >= 0 ? "ret-pos" : "ret-neg";
};

const fmtDate = (iso) => iso ? iso.slice(0, 10) : "—";

async function load() {
    let data;
    try {
        const resp = await fetch(DATA_URL, { cache: "no-store" });
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        data = await resp.json();
    } catch (e) {
        document.getElementById("alerts-tbody").innerHTML =
            `<tr><td colspan="7" class="loading">Failed to load ledger: ${e.message}</td></tr>`;
        return;
    }
    renderHero(data);
    renderHitRateChart(data);
    renderReturnChart(data);
    renderTable(data);
    document.getElementById("footer-updated").textContent = fmtDate(data.generated_at);
    document.getElementById("footer-year").textContent = new Date().getFullYear();
}

function renderHero(data) {
    document.getElementById("stat-total").textContent = (data.total_alerts || 0).toLocaleString();
    document.getElementById("stat-scanners").textContent = (data.scanners_active || 0);
    const hr = data.median_hit_rate_20d;
    document.getElementById("stat-hitrate").textContent =
        hr === null || hr === undefined ? "—" : (hr * 100).toFixed(0) + "%";
    document.getElementById("stat-updated").textContent = fmtDate(data.generated_at);
}

function renderHitRateChart(data) {
    const byScanner = data.hit_rate_by_scanner || {};
    const labels = Object.keys(byScanner).sort();
    const values = labels.map(k => (byScanner[k] * 100).toFixed(1));
    const ctx = document.getElementById("chart-hitrate");
    if (!ctx || labels.length === 0) return;
    new Chart(ctx, {
        type: "bar",
        data: {
            labels,
            datasets: [{
                label: "Hit rate (%)",
                data: values,
                backgroundColor: "#4ade80",
                borderRadius: 2,
            }]
        },
        options: chartOpts("Hit rate (%)", "Positive 20d return %"),
    });
}

function renderReturnChart(data) {
    const bySig = data.median_return_20d_by_signal || {};
    const labels = Object.keys(bySig).sort();
    const values = labels.map(k => (bySig[k] * 100).toFixed(2));
    const ctx = document.getElementById("chart-returns");
    if (!ctx || labels.length === 0) return;
    new Chart(ctx, {
        type: "bar",
        data: {
            labels,
            datasets: [{
                label: "Median 20d return (%)",
                data: values,
                backgroundColor: values.map(v => Number(v) >= 0 ? "#4ade80" : "#f87171"),
                borderRadius: 2,
            }]
        },
        options: chartOpts("Median 20d return (%)", "Median return %"),
    });
}

function chartOpts(_yTitle, tooltipLabel) {
    return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { display: false },
            tooltip: {
                callbacks: {
                    label: (ctx) => `${tooltipLabel}: ${ctx.parsed.y}`,
                }
            }
        },
        scales: {
            x: {
                ticks: { color: "#9090a0", font: { family: "JetBrains Mono", size: 11 } },
                grid: { color: "#2a2a35" },
            },
            y: {
                ticks: { color: "#9090a0", font: { family: "JetBrains Mono", size: 11 } },
                grid: { color: "#2a2a35" },
            },
        },
    };
}

let currentSort = { key: "alert_date", dir: -1 };

function renderTable(data) {
    const rows = (data.recent_alerts || []).slice(0, TABLE_LIMIT);
    const tbody = document.getElementById("alerts-tbody");
    if (rows.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" class="loading">No alerts in the public window yet.</td></tr>`;
        return;
    }
    rows.sort((a, b) => sortFn(a, b, currentSort.key, currentSort.dir));
    tbody.innerHTML = rows.map(row => `
        <tr>
            <td>${fmtDate(row.alert_date)}</td>
            <td>${esc(row.scanner)}</td>
            <td>${esc(row.signal_type)}</td>
            <td>${esc(row.ticker || "—")}</td>
            <td class="num ${pctClass(row.return_5d)}">${fmtPct(row.return_5d) || "—"}</td>
            <td class="num ${pctClass(row.return_20d)}">${fmtPct(row.return_20d) || "—"}</td>
            <td class="num ${pctClass(row.return_60d)}">${fmtPct(row.return_60d) || "—"}</td>
        </tr>
    `).join("");
    bindSort(data);
}

function bindSort(data) {
    document.querySelectorAll("th[data-sort]").forEach(th => {
        th.onclick = () => {
            const key = th.dataset.sort;
            currentSort.dir = (currentSort.key === key) ? -currentSort.dir : -1;
            currentSort.key = key;
            renderTable(data);
        };
    });
}

function sortFn(a, b, key, dir) {
    const av = a[key], bv = b[key];
    if (av === null || av === undefined) return 1;
    if (bv === null || bv === undefined) return -1;
    if (typeof av === "number" && typeof bv === "number") return (av - bv) * dir;
    return String(av).localeCompare(String(bv)) * dir;
}

function esc(s) {
    return String(s ?? "").replace(/[&<>"']/g, c => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
}

document.addEventListener("DOMContentLoaded", load);
