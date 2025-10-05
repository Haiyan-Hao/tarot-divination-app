# 🚀 Vercel部署指南

## 部署步骤

### 1. 准备GitHub仓库

1. 在GitHub上创建一个新仓库
2. 将代码推送到仓库：
```bash
git init
git add .
git commit -m "Initial commit: Tarot divination app"
git branch -M main
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```

### 2. 在Vercel部署

1. 登录 [Vercel](https://vercel.com)
2. 点击 "New Project"
3. 选择 "Import Git Repository"
4. 选择你的GitHub仓库
5. 点击 "Deploy"

### 3. 配置环境变量

在Vercel项目设置中添加环境变量：

- **OPENAI_API_KEY**: 你的OpenAI API密钥
- **FLASK_ENV**: production
- **FLASK_DEBUG**: False

### 4. 部署完成

部署成功后，你会得到一个类似这样的网址：
`https://你的项目名.vercel.app`

## 🔧 环境变量说明

| 变量名 | 值 | 说明 |
|--------|-----|------|
| OPENAI_API_KEY | sk-xxx... | OpenAI API密钥 |
| FLASK_ENV | production | 生产环境 |
| FLASK_DEBUG | False | 关闭调试模式 |

## 📝 注意事项

1. **API密钥安全**：不要将API密钥提交到代码仓库
2. **费用控制**：OpenAI API按使用量收费，建议设置使用限制
3. **域名**：可以绑定自定义域名

## 🆘 常见问题

### 部署失败
- 检查requirements.txt中的依赖是否正确
- 确认vercel.json配置正确

### API调用失败
- 检查OPENAI_API_KEY是否正确设置
- 确认API密钥有足够的额度

### 页面无法访问
- 检查Vercel部署日志
- 确认所有环境变量已正确设置

## 📞 技术支持

如果遇到问题，请检查：
1. Vercel部署日志
2. 环境变量配置
3. OpenAI API状态
