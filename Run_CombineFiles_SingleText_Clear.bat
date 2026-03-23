@echo off
setlocal
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0CombineFiles_SingleText_Clear.ps1"
set "RC=%ERRORLEVEL%"
echo.
if not "%RC%"=="0" (
  echo Failed. Exit code: %RC%
) else (
  echo Success.
)
pause
exit /b %RC%
