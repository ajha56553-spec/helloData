import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Databricks!"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("DATABRICKS_APP_PORT", 8000))
    )
