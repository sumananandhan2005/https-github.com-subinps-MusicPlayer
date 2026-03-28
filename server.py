from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Music Bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    Thread(target=run).start()
```

5. Click **Commit new file** (green button at bottom)

---

## Step 2 — Edit `requirements.txt`

1. In your repo, click on `requirements.txt`
2. Click the **pencil icon** to edit
3. Add this line at the very bottom:
```
flask
