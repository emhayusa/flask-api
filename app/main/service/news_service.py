import uuid
import datetime

from app.main import db 
from app.main.model.news import News


def save_new(data):
    new = News(
        title=data['title'],
        summary=data['summary'],
        content=data['content'],
        created_at=datetime.datetime.utcnow()+ datetime.timedelta(hours=7),
        created_by=data['created_by']
    )

    save_changes(new)
    response_object = {
        'status': 'success',
        'message': 'News successfully inserted.'
    }
    return response_object, 201

def get_all():
    return News.query.order_by('news_id').all()

def get_by_id(id):
    return News.query.filter_by(news_id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

