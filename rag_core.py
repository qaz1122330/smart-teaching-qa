"""
RAG核心模块（简化演示版）
"""
class RAGEngine:
    def __init__(self):
        self.model_name = "GPT-3.5 + RAG"
    
    def search_knowledge(self, question):
        """模拟知识检索"""
        return ["人工智能是...", "机器学习是..."]
    
    def generate_answer(self, question):
        """模拟生成回答"""
        return f"基于知识库，{question}的答案是..."
