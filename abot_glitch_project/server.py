import threading
from flask import Flask
import bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running on Glitch!"

def run_server():
    app.run(host="0.0.0.0", port=3000)

def run_bot():
    bot.main()

if __name__ == "__main__":
    threading.Thread(target=run_server).start()
    run_bot()
