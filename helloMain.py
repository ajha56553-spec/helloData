from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Databricks App"

if __name__ == "__main__":
    import os
    app.run(
        host="0.0.0.0",
        port=int(os.environ["DATABRICKS_APP_PORT"])
    )
``
