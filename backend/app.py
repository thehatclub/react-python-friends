import os

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)

frontend_folder = os.path.join(os.getcwd(), "..", "frontend", "dist")


# serve static files from the "dist"" folder under the "frontend" directory
@app.route("/", defaults={"filename": ""})
@app.route("/<path:filename>")
def index(filename):
    if not filename:
        filename = "index.html"
    return send_from_directory(frontend_folder, filename)


# api routes
import routes

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
