# Deploy Commands

## To TrueNAS
```bash
scp *.html *.css *.js jdmal@100.83.75.4:/mnt/tank/websites/kusanagi/isn.biz/public/
ssh jdmal@100.83.75.4 "sudo service nginx reload"
```

## Verify
```bash
curl -I https://isn.biz
```

## Git
```bash
git add . && git commit -m "msg" && git push origin main
```
