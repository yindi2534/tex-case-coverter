from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5419022866172835"
     crossorigin="anonymous"></script>
    <title>Text Case Converter Pro</title>
    <style>
        body { 
            font-family: 'Inter', 'Segoe UI', Arial, sans-serif; 
            margin: 0; 
            padding: 40px 20px; 
            background-color: #0f0f11; 
            color: #f5f5f7; 
            min-height: 100vh;
        }
        .card { 
            background: #18181c; 
            padding: 35px; 
            border-radius: 16px; 
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), 0 0 15px rgba(212, 175, 55, 0.15); 
            max-width: 680px; 
            margin: auto; 
            border: 1px solid rgba(212, 175, 55, 0.3);
        }
        h2 {
            background: linear-gradient(135deg, #d4af37 0%, #fffdd0 50%, #aa771c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 28px;
            margin-top: 0;
            font-weight: 700;
        }
        p {
            color: #a1a1a6;
            font-size: 15px;
        }
        textarea { 
            width: 100%; 
            height: 150px; 
            margin-top: 15px; 
            box-sizing: border-box; 
            padding: 15px; 
            border: 1px solid #333338; 
            border-radius: 10px; 
            background-color: #0f0f11; 
            color: #f5f5f7; 
            font-size: 15px;
            resize: vertical;
            outline: none;
            transition: border-color 0.3s;
        }
        textarea:focus {
            border-color: #d4af37;
        }
        .btn-group { 
            margin-top: 20px; 
            display: flex; 
            gap: 12px; 
        }
        button { 
            background: linear-gradient(135deg, #c5a059 0%, #f3e5ab 50%, #b38728 100%); 
            color: #000000; 
            border: none; 
            padding: 12px 20px; 
            border-radius: 25px; 
            cursor: pointer; 
            font-weight: 700; 
            font-size: 14px;
            flex: 1;
            box-shadow: 0 4px 15px rgba(197, 160, 89, 0.2);
            transition: all 0.3s ease;
        }
        button:hover { 
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
        }
        .ad-space { 
            background: #121215; 
            border: 1px dashed #d4af37; 
            padding: 15px; 
            text-align: center; 
            margin-bottom: 25px; 
            color: #d4af37; 
            border-radius: 8px;
            font-size: 13px;
        }
        .result-box { 
            background: #121215; 
            padding: 18px; 
            border-radius: 10px; 
            margin-top: 25px; 
            word-break: break-all; 
            border: 1px solid #2a2a30;
        }
        .result-box h3 {
            color: #d4af37;
            margin-top: 0;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="ad-space">
            <b>Google AdSense Area</b><br>Ads will appear here to generate revenue.
        </div>
        
        <!-- Temu Affiliate Banner -->
        <div style="background: linear-gradient(135deg, #ff6b00 0%, #ff8800 100%); color: #ffffff; padding: 20px; border-radius: 12px; text-align: center; margin: 25px 0; box-shadow: 0 4px 15px rgba(255,107,0,0.3);">
            <h3 style="margin: 0 0 10px 0; font-size: 20px; color: #ffffff;">🛍️ Exclusive Offer on Temu!</h3>
            <p style="margin: 0 0 15px 0; font-size: 14px; opacity: 0.95; color: #ffffff;">Get free gifts, free shipping, and 90-day free returns.</p>
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

        {% if converted_text %}
        <div class="result-box">
            <h3>Converted Result:</h3>
            <p style="color: #f5f5f7;">{{ converted_text }}</p>
        </div>
        {% endif %}
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
    app.run(debug=True)
