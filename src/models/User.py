# -*- coding: utf-8 -*-
from src.models.shared import db

class User(db.Model):
    __tablename__ = 'User'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    phone_number = db.Column(db.String(15))
    is_verified = db.Column(db.Boolean)

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.is_verified = False

    def __repr__(self):
        content = {"id": self._id,
                    "phone_number": self.phone_number
                    }
        return str({"User": content})

    def to_dict(self):
        return {"_id": self._id,
                "phone_number": self.phone_number
                }
