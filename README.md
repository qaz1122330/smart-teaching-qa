🎓 智能教学问答系统

基于RAG（Retrieval-Augmented Generation）架构的智能教学问答系统，能够根据上传的教学文档进行智能问答。
✨ 功能特性

    📚 多格式文档支持：PDF、TXT、MD文件自动解析

    🔍 语义搜索：基于向量数据库的智能检索

    🤖 智能问答：集成GPT生成准确回答

    📊 来源追溯：每个回答附带参考来源

    🎨 美观界面：现代化响应式Web界面

🚀 快速开始
环境要求

    Python 3.8+

    OpenAI API密钥

安装步骤
1. 克隆项目
bash

git clone https://github.com/qs21123330/smart-teaching-qa.git
cd smart-teaching-qa

2. 安装依赖
bash

pip install -r requirements.txt

3. 配置API密钥
bash

# 复制配置文件
cp .env.example .env

# 编辑.env文件，填入你的OpenAI API密钥
# 获取密钥：https://platform.openai.com/api-keys

4. 运行系统
bash

python app.py

5. 开始使用

打开浏览器访问：http://localhost:5000
🛠️ 技术栈

    后端框架: Python, Flask

    AI模型: OpenAI GPT, Sentence Transformers

    向量数据库: ChromaDB

    前端技术: HTML5, CSS3, JavaScript

📁 项目结构
text

smart-teaching-qa/
├── app.py              # Flask主应用
├── config.py          # 配置文件
├── requirements.txt   # 依赖列表
├── .env.example      # 环境变量示例
├── .gitignore        # Git忽略文件
└── templates/        # 前端页面
    └── index.html

📞 联系我们

如有问题或建议，请在GitHub提交Issue。

⭐ 如果这个项目对你有帮助，请给个Star支持！
