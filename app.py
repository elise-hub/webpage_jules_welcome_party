import os
from flask import Flask, render_template
from pyngrok import ngrok, conf
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    auth_token = os.getenv("NGROK_AUTH_TOKEN")
    if auth_token:
        conf.get_default().auth_token = auth_token
        public_url = ngrok.connect(5000).public_url
        print(f"\n * Public URL for guests: {public_url}\n")

    app.run(port=5000)
