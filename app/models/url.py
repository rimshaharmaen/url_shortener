from datetime import datetime
from app import db


class URL(db.Model):
    __tablename__ = "urls"

    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=True)
    click_count = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "long_url": self.long_url,
            "short_code": self.short_code,
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "click_count": self.click_count,
        }