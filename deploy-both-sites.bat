@echo off
echo ============================
echo  DEPLOYING ISN.BIZ
echo ============================
cd /d D:\workspace\ISNBIZ_Files
git status
git add -A
git commit -m "chore: clean up stale files and update deployment docs"
git push origin main
echo.
echo ============================
echo  DEPLOYING HROC
echo ============================
cd /d D:\workspace\HROC_Files
set GITHUB_TOKEN=
git status
git push origin main
echo.
echo ============================
echo  VERIFYING SITES
echo ============================
curl -sI https://isn.biz
curl -sI https://hrocinc.org
echo.
echo Done! Check output above for any errors.
pause
