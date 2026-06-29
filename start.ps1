# 短视频脚本生成器 - 统一启动脚本
# 此脚本只需启动后端服务(5001端口)
# 后端已配置为同时提供前端静态文件和API服务

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "短视频脚本生成器" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查Python是否可用
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python版本: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "错误: 未找到Python，请先安装Python 3.x" -ForegroundColor Red
    exit 1
}

# 检查后端依赖
Write-Host ""
Write-Host "正在检查依赖..." -ForegroundColor Yellow

# 尝试安装后端依赖（如果缺失）
if (Test-Path "backend\requirements.txt") {
    Write-Host "安装后端Python依赖..." -ForegroundColor Yellow
    pip install -r backend\requirements.txt -q
}

# 启动后端服务（同时提供前端和API）
Write-Host ""
Write-Host "正在启动服务(5001端口)..." -ForegroundColor Green
Write-Host "后端将同时服务前端页面和API请求" -ForegroundColor Gray
Write-Host ""

# 切换到后端目录并启动
Set-Location "backend"

# 使用默认浏览器打开
Start-Process "http://localhost:5001"

# 启动Flask应用
python app.py

# 这个脚本会保持运行，直到用户按Ctrl+C
