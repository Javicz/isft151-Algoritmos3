from datetime import datetime, timezone

from config import db, ma


def utcnow():
    return datetime.now(timezone.utc).replace(tzinfo=None)


class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True, nullable=False)
    fname = db.Column(db.String(32), nullable=False, default="")
    timestamp = db.Column(db.DateTime, default=utcnow, onupdate=utcnow)


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
