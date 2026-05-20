from flask import Flask
from flask_sqlalchemy import MySQlALchemy
from sqlalchemy import text

app = Flask(__name__)
app.config["MYSQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:root123@localhost/uki_school"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = MySQlALchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, Primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)


if __name__ == "__main__":
    try:
        with app.app_context():
            db.session.execute(text("SELECT 1"))
            print("SUCCESS: Database Connected Successfully")
            print("Database Tables are created")
            db.create_all()

    except Exception as error:
        print("ERROR: Database Connection Failed")
        print({error})
        print(error)

    app.run(debug=True, port=8040)
