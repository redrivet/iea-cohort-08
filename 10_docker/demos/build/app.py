import configparser
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

config = configparser.ConfigParser()
has_config = config.read("/opt/guestbook/vars.ini")

app = Flask(__name__)

# MySQL configurations
if "db" in config:
    db_user = config["db"]["MYSQL_DATABASE_USER"]
    db_pass = config["db"]["MYSQL_DATABASE_PASSWORD"]
    db_name = config["db"]["MYSQL_DATABASE_DB"]
    db_host = config["db"]["MYSQL_DATABASE_HOST"]
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://%s:%s@%s/%s" % (
        db_user,
        db_pass,
        db_host,
        db_name,
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Signatures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000))


db.create_all()


@app.route("/guestbook", methods=["GET"])
def sign():
    result = Signatures.query.all()
    return "\n".join(map(lambda x: x.message, result))


@app.route("/guestbook", methods=["POST"])
def write():
    message = request.args.get("message")
    signature = Signatures(message=message)
    db.session.add(signature)
    db.session.commit()

    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
