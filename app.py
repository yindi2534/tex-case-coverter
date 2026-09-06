from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5419022866172835"
     crossorigin="anonymous"></script>
    <title>Text Case Converter Pro</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f6f8; }
        .card { background: white; padding: 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); max-width: 650px; margin: auto; }
        textarea { width: 100%; height: 140px; margin-top: 10px; box-sizing: border-box; padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; }
        .btn-group { margin-top: 15px; display: flex; gap: 10px; }
        button { background: #007bff; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; font-weight: bold; flex: 1; }
        button:hover { background: #0056b3; }
        .ad-space { background: #fff3cd; border: 1px dashed #ffebaa; padding: 15px; text-align: center; margin-bottom: 20px; color: #856404; border-radius: 4px; font-size: 13px; }
        .result-box { background: #e8f4f8; padding: 15px; border-radius: 4px; margin-top: 20px; word-break: break-all; }
    </style>
</head>
<body>
    <div class="card">
        <div class="ad-space">📢 <b>Google AdSense Area</b><br>Ads will appear here to generate revenue.</div>
        <!-- Temu Affiliate Banner -->
<div style="background: linear-gradient(135deg, #ff6b00 0%, #ff8800 100%); color: #ffffff; padding: 20px; border-radius: 12px; text-align: center; margin: 25px 0; box-shadow: 0 4px 15px rgba(255,107,0,0.3);">
    <h3 style="margin: 0 0 10px 0; font-size: 20px; color: #ffffff;">🛍️ Exclusive Offer on Temu!</h3>
    <p style="margin: 0 0 15px 0; font-size: 14px; opacity: 0.95;">Get free gifts, free shipping, and 90-day free returns.</p>
    <a href="https://temu.to/k/e6o45ia6r43" target="_blank" style="display: inline-block; background-color: #ffffff; color: #ff6b00; padding: 12px 28px; text-decoration: none; border-radius: 25px; font-weight: bold; font-size: 16px; transition: transform 0.2s;">
        Claim Free Gift & Shop Now! (Use Code: als868300)
    </a>
</div>

        <h2>✨ Text Case Converter Pro</h2>
        <p>Convert your text to Uppercase, Lowercase, or Title Case instantly.</p>
        <form method="POST">
            <textarea name="user_text" placeholder="Type or paste your text here..." required>{{ original_text }}</textarea>
            <div class="btn-group">
                <button type="submit" name="mode" value="upper">UPPERCASE</button>
                <button type="submit" name="mode" value="lower">lowercase</button>
                <button type="submit" name="mode" value="title">Title Case</button>
            </div>
        </form>
        {% if result %}
        <div class="result-box">
            <h3>Result:</h3>
            <p><b>{{ result }}</b></p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    original_text = ""
    if request.method == 'POST':
        original_text = request.form.get('user_text', '')
        mode = request.form.get('mode', 'upper')
        if mode == 'upper':
            result = original_text.upper()
        elif mode == 'lower':
            result = original_text.lower()
        elif mode == 'title':
            result = original_text.title()
    return render_template_string(HTML, result=result, original_text=original_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
