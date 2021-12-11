from .. import db

class News(db.Model):
    """ News Model for storing news related details """
    __tablename__ = "news"

    news_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(100), nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'news_id'}

       