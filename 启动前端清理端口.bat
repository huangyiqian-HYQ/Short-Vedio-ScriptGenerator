@echo off
echo 正在检查端口5001占用情况...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :5001') do (
    echo 发现进程占用端口5001，PID: %%a
    taskkill /F /PID %%a
    echo 已终止进程 %%a
)
echo.
echo 正在启动前端服务...
cd /d "%~dp0frontend"
start "前端服务" cmd /k "python -m http.server 5001"
echo.
echo 前端服务已启动，请在浏览器打开：http://localhost:5001/index.html
echo.
pause