import random
import string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def generate_short_id(length=6):
    """Generate a random short ID using letters and numbers (Base62 encoding)."""
    characters = string.ascii_letters + string.digits  
    return ''.join(random.choices(characters, k=length))

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_id = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    visit_count = db.Column(db.Integer, default=0)

    def __init__(self, original_url, short_id=None):
        self.original_url = original_url
        self.short_id = short_id if short_id else self.generate_unique_short_id()

    @staticmethod
    def generate_unique_short_id():
        """Ensures the generated short ID is unique."""
        while True:
            new_id = generate_short_id()
            if not URL.query.filter_by(short_id=new_id).first():
                return new_id
