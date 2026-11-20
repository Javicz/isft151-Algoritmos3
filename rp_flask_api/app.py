from flask import render_template

from config import app, connex_app, db
from models import Person

connex_app.add_api("swagger.yml")


def initialize_database():
    with app.app_context():
        db.create_all()
        if not Person.query.first():
            db.session.add_all(
                [
                    Person(fname="Tooth", lname="Fairy"),
                    Person(fname="Knecht", lname="Ruprecht"),
                    Person(fname="Easter", lname="Bunny"),
                ]
            )
            db.session.commit()


initialize_database()


@app.route("/")
def home():
    people = Person.query.order_by(Person.lname).all()
    return render_template("home.html", people=people)


if __name__ == "__main__":
    connex_app.run(host="0.0.0.0", port=8000)
