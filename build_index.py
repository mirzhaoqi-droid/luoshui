import os

# 配置：过滤掉不需要显示的文件
EXCLUDE_FILES = ['index.html', 'build_index.py']

def generate_index():
    # 获取当前文件夹下所有 .html 文件
    files = [f for f in os.listdir('.') if f.endswith('.html') and f not in EXCLUDE_FILES]
    
    # 按照修改时间排序（可选）
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

    # HTML 模板
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>我的 AI 工具箱导航</title>
        <style>
            body {{ font-family: sans-serif; background: #0b0f1a; color: white; padding: 40px; text-align: center; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; max-width: 1000px; margin: 40px auto; }}
            .card {{ background: #161e31; padding: 20px; border-radius: 12px; border: 1px solid #1e293b; text-decoration: none; color: #22d3ee; transition: 0.3s; }}
            .card:hover {{ transform: translateY(-5px); border-color: #6366f1; background: #1e293b; }}
            h1 {{ color: #6366f1; }}
        </style>
    </head>
    <body>
        <h1>🛠️ 我的 AI 提示词工具箱</h1>
        <p>已自动收录 {len(files)} 个工具</p>
        <div class="grid">
            {" ".join([f'<a class="card" href="{f}"><h3>{f.replace(".html", "").replace("_", " ")}</h3></a>' for f in files])}
        </div>
    </body>
    </html>
    """
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✅ index.html 已更新！")

if __name__ == "__main__":
    generate_index()
