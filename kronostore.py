from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Did I break it<h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
