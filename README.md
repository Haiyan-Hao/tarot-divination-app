# 简易塔罗牌占卜Web应用

一个基于Python Flask的本地塔罗牌占卜Web应用，用户可输入问题，系统自动抽取三张塔罗牌并生成简要解读。

## 功能特点

- 🔮 随机抽取三张塔罗牌（支持正位/逆位）
- 📝 根据用户问题生成个性化解读
- 🎨 简洁美观的Web界面
- 📱 响应式设计，支持移动端
- 🚀 无需数据库，本地直接运行

## 项目结构

```
cursor_trial/
├── app.py                 # Flask主应用文件
├── templates/
│   └── index.html         # 主页面模板
├── static/
│   ├── css/
│   │   └── style.css      # 样式文件
│   └── js/
│       └── script.js      # JavaScript脚本
├── 需求.ini               # 项目需求文档
└── README.md              # 项目说明文档
```

## 安装和运行

### 环境要求

- Python 3.6+
- Flask

### 安装依赖

```bash
pip install flask
```

### 运行应用

```bash
python app.py
```

应用将在 `http://localhost:5000` 启动。

### 使用方法

1. 在浏览器中打开 `http://localhost:5000`
2. 在输入框中输入您想要占卜的问题
3. 点击"开始占卜"按钮
4. 系统将随机抽取三张塔罗牌并生成解读
5. 查看塔罗牌和解读结果

## 技术实现

### 后端 (Flask)
- 使用Flask框架提供Web服务
- 内置22张大阿卡纳塔罗牌数据
- 随机抽取算法和解读生成逻辑
- RESTful API接口设计

### 前端 (HTML/CSS/JavaScript)
- 响应式设计，支持桌面和移动端
- 现代化UI界面，渐变背景和卡片设计
- 异步请求处理，流畅的用户体验
- 加载动画和错误处理

### 塔罗牌数据
- 包含22张大阿卡纳牌
- 每张牌包含名称、含义和图片链接
- 支持正位/逆位随机选择
- 使用占位符图片（可替换为真实塔罗牌图片）

## 扩展功能

### 可选增强
- 集成OpenAI API实现AI智能解读
- 添加更多塔罗牌图片资源
- 实现占卜历史记录功能
- 添加不同牌阵选择（十字牌阵等）

### 自定义配置
如需使用AI解读功能，可在 `app.py` 中配置OpenAI API密钥：

```python
# 在generateReading函数中添加AI调用
import openai
openai.api_key = "your-api-key-here"
```

## 部署说明

### 本地部署
直接运行 `python app.py` 即可在本地启动服务。

### 生产部署
建议使用Gunicorn等WSGI服务器：

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### GitHub部署
1. 将代码上传至GitHub仓库
2. 其他用户可通过以下命令下载和运行：

```bash
git clone <repository-url>
cd <repository-name>
pip install flask
python app.py
```

## 注意事项

- 本项目仅供娱乐参考，塔罗牌解读结果不应作为重要决策依据
- 图片使用占位符链接，实际部署时可替换为真实塔罗牌图片
- 建议在本地环境运行，避免将API密钥等敏感信息上传至公共仓库

## 许可证

MIT License - 可自由使用和修改

## 贡献

欢迎提交Issue和Pull Request来改进这个项目！
