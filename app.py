from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask_question():
    return jsonify({
        "success": True,
        "answer": "这是智能问答系统的演示版本。请安装依赖后使用完整功能。",
        "sources": []
    })

if __name__ == '__main__':
    app.run(debug=True)
