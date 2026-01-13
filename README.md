# 🎓 智能教学问答系统

基于RAG（Retrieval-Augmented Generation）架构的智能教学问答系统，能够根据上传的教学文档进行智能问答。

## ✨ 功能特性
- 📚 多格式文档支持：PDF、TXT、MD文件自动解析
- 🔍 语义搜索：基于向量数据库的智能检索
- 🤖 智能问答：集成GPT生成准确回答
- 📊 来源追溯：每个回答附带参考来源
- 🎨 美观界面：现代化响应式Web界面

## 🚀 快速开始

### 环境要求
- Python 3.8+
- OpenAI API密钥

### 安装步骤
     克隆项目
```bash
git clone https://github.com/qs21123330/smart-teaching-qa.git
cd smart-teaching-qa
    安装依赖

bash

pip install -r requirements.txt

    配置环境变量

bash

cp .env.example .env
# 编辑.env文件，填入你的OpenAI API密钥

    准备知识库

bash

mkdir -p data/textbooks
# 将教学PDF/TXT文件放入data/目录

    初始化数据库

bash

python init_database.py

    启动服务

bash

python app.py
