from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5419022866172835" crossorigin="anonymous"></script>
    <title>Text Case Converter Pro</title>
    <style>
        body { font-family: 'Inter', Arial, sans-serif; margin: 0; padding: 40px 20px; background-color: #0f0f11; color: #f5f5f7; min-height: 100vh; }
        .container { max-width: 680px; margin: auto; display: flex; flex-direction: column; gap: 25px; }
        .card { background: #18181c; padding: 35px; border-radius: 16px; box-shadow: 0 15px 35px rgba(0,0,0,0.6); border: 1px solid rgba(212,175,55,0.3); }
        h2 { background: linear-gradient(135deg, #d4af37 0%, #fffdd0 50%, #aa771c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 28px; margin-top: 0; }
        p { color: #a1a1a6; font-size: 15px; }
        textarea { width: 100%; height: 150px; margin-top: 15px; box-sizing: border-box; padding: 15px; border: 1px solid #333338; border-radius: 10px; background-color: #0f0f11; color: #f5f5f7; font-size: 15px; outline: none; }
        textarea:focus { border-color: #d4af37; }
        .btn-group { margin-top: 20px; display: flex; gap: 12px; }
        .btn-convert { background: linear-gradient(135deg, #c5a059 0%, #f3e5ab 50%, #b38728 100%); color: #000; border: none; padding: 12px 20px; border-radius: 25px; cursor: pointer; font-weight: 700; flex: 1; }
        .btn-convert:hover { transform: translateY(-2px); }
        .ad-space { background: #121215; border: 1px dashed #d4af37; padding: 15px; text-align: center; color: #d4af37; border-radius: 8px; font-size: 13px; }
        .result-box { background: #121215; padding: 18px; border-radius: 10px; margin-top: 25px; word-break: break-all; border: 1px solid #2a2a30; }
        .result-box h3 { color: #d4af37; margin-top: 0; }
        
        /* Massage Banner Card */
        .massage-card { background: linear-gradient(145deg, #1f1b14 0%, #121215 100%); border: 1px solid #d4af37; text-align: center; padding: 25px; }
        .massage-img { width: 100%; max-width: 500px; border-radius: 12px; margin-bottom: 20px; border: 1px solid rgba(212,175,55,0.4); box-shadow: 0 8px 20px rgba(0,0,0,0.5); }
        .btn-book { display: inline-block; background: linear-gradient(135deg, #d4af37 0%, #f3e5ab 50%, #aa771c 100%); color: #000; text-decoration: none; padding: 14px 32px; border-radius: 30px; font-weight: bold; font-size: 16px; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4); transition: all 0.3s ease; }
        .btn-book:hover { transform: scale(1.05); box-shadow: 0 6px 20px rgba(212, 175, 55, 0.6); }
    </style>
</head>
<body>
    <div class="container">
        <div class="ad-space"><b>Google AdSense Area</b><br>Ads will appear here to generate revenue.</div>
        
        <div class="card">
            <h2>✨ Text Case Converter Pro</h2>
            <p>Convert your text to Uppercase, Lowercase, or Title Case instantly.</p>
            <form method="POST">
                <textarea name="user_text" placeholder="Type or paste your text here..." required>{{ original_text }}</textarea>
                <div class="btn-group">
                    <button type="submit" name="mode" value="upper" class="btn-convert">UPPERCASE</button>
                    <button type="submit" name="mode" value="lower" class="btn-convert">lowercase</button>
                    <button type="submit" name="mode" value="title" class="btn-convert">Title Case</button>
                </div>
            </form>
            {% if converted_text %}
            <div class="result-box">
                <h3>Converted Result:</h3>
                <p style="color: #f5f5f7;">{{ converted_text }}</p>
            </div>
            {% endif %}
        </div>

        <!-- Massage Promotion Banner -->
        <div class="card massage-card">
            <a href="https://yindi-massasje.netlify.app" target="_blank">
                <img src="https://raw.githubusercontent.com/yindi2534/tex-case-coverter/main/yindi%20massasje.png" alt="Yindi Massasje" class="massage-img">
            </a>
            <br>
            <a href="https://yindi-massasje.netlify.app" target="_blank" class="btn-book">📅 จองคิว / Bestill Time</a>
        </div>

        <!-- Temu Offer Banner -->
        <div style="background: linear-gradient(135deg, #ff6b00 0%, #ff8800 100%); color: #fff; padding: 20px; border-radius: 12px; text-align: center;">
            <h3 style="margin: 0 0 10px 0; font-size: 20px; color: #fff;">🛍️ Exclusive Offer on Temu!</h3>
            <p style="margin: 0 0 15px 0; font-size: 14px; color: #fff;">Get free gifts, free shipping, and 90-day free returns.</p>
            <a href="https://temu.to/k/e6o45ia6r43" target="_blank" style="display: inline-block; background-color: #fff; color: #ff6b00; padding: 12px 28px; text-decoration: none; border-radius: 25px; font-weight: bold;">Claim Free Gift & Shop Now! (Use Code: als868300)</a>
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    original_text = ""
    converted_text = ""
    if request.method == 'POST':
        original_text = request.form.get('user_text', '')
        mode = request.form.get('mode', '')
        if mode == 'upper':
            converted_text = original_text.upper()
        elif mode == 'lower':
            converted_text = original_text.lower()
        elif mode == 'title':
            converted_text = original_text.title()
    return render_template_string(HTML, original_text=original_text, converted_text=converted_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
