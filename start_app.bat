@echo off
cd /d "e:\软件工程\01\qimozuoye2"
echo 启动短视频脚本生成器...
echo.
echo 正在启动前端服务（端口5001）...
start /min cmd /c "cd frontend && python -m http.server 5001"
echo.
echo 正在启动后端服务（端口5000）...
start /min cmd /c "cd backend && python app.py"
echo.
echo 服务已启动！
echo 前端页面：http://localhost:5001/index.html
echo 脚本创作：http://localhost:5001/create.html
echo 后端API：http://localhost:5000/api
echo.
pause