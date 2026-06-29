@echo off
echo 正在启动前端服务（使用端口8080）...
cd /d "%~dp0frontend"
start "前端服务-8080" cmd /k "python -m http.server 8080"
echo.
echo 前端服务已启动，请在浏览器打开：http://localhost:8080/index.html
echo.
pause