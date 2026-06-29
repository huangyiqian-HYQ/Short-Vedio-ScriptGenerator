# 短视频脚本生成器

基于 B/S 三层架构的短视频脚本生成器，采用 Python Flask + SQLite + OpenAI API 技术栈。

## 功能特点

- 用户注册登录（JWT鉴权）
- 10类短视频赛道模板（好物带货、知识科普、探店Vlog等）
- AI智能生成短视频脚本
- 三种文案风格（口语日常、爆款短句、专业科普）
- 云端历史记录 + 本地缓存
- 脚本导出（TXT/Word）

## BUG修复说明

本版本修复了三大核心缺陷：
1. **页面自动生成问题**：删除页面加载自动调用AI代码，仅按钮点击触发生成
2. **关键词校验误判**：统一分隔符过滤空白关键词，精准统计有效数量
3. **生成功能失效**：完善API请求封装，增加加载状态、错误弹窗反馈

## 项目结构

```
qimozuoye2/
├── backend/                 # 后端服务
│   ├── app/
│   │   ├── controllers/     # 控制器
│   │   ├── models/          # 数据模型
│   │   ├── services/        # 业务服务
│   │   └── utils/           # 工具类
│   ├── app.py               # 主程序
│   ├── config.py            # 配置文件
│   └── requirements.txt     # 依赖列表
├── frontend/                # 前端页面
│   ├── css/                 # 样式文件
│   ├── js/                  # JavaScript
│   ├── login.html           # 登录页面
│   ├── register.html        # 注册页面
│   └── index.html           # 主页面
└── start.ps1                # 启动脚本
```

## 安装运行

### 方式一：使用启动脚本（推荐）

双击运行项目根目录下的 `一键启动.bat` 或 `start.ps1`，系统将自动启动后端服务。

### 方式二：手动启动

#### 1. 安装依赖

```powershell
cd backend
pip install -r requirements.txt
```

#### 2. 启动服务（只启动后端）

后端已配置为同时提供前端静态文件和API服务，因此只需启动后端即可：

```powershell
cd backend
python app.py
```

#### 3. 访问系统

打开浏览器访问：http://localhost:5001

> **注意**：现在只需启动后端服务(5001端口)，无需单独启动前端。后端会同时服务前端页面和API请求，避免了跨域问题。

## API接口

| 接口 | 方法 | 说明 |
|------|------|------|
| /api/user/register | POST | 用户注册 |
| /api/user/login | POST | 用户登录 |
| /api/user/info | GET | 获取用户信息 |
| /api/template/list | GET | 获取模板列表 |
| /api/script/generate | POST | 生成脚本 |
| /api/script/list | GET | 获取历史记录 |
| /api/script/export | GET | 导出脚本 |

## 配置说明

修改 `backend/.env` 文件配置：

```
OPENAI_API_KEY=your-api-key-here
```

如未配置API密钥，系统将使用模拟数据生成脚本。