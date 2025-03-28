from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import shortuuid

db = SQLAlchemy()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_id = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    visit_count = db.Column(db.Integer, default=0)

    def __init__(self, original_url, custom_short_id=None):
        self.original_url = original_url
        self.short_id = custom_short_id if custom_short_id else self.generate_unique_short_id()

    @staticmethod
    def generate_unique_short_id(length=6):
        while True:
            new_id = shortuuid.ShortUUID().random(length=length)
            if not URL.query.filter_by(short_id=new_id).first():
                return new_id

