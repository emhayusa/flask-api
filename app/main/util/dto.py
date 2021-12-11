from flask_restplus import Namespace, fields

class NewsDto:
    api = Namespace('news', description='news related operations')
    schema = api.model('news_schema', {
        'news_id': fields.Integer(dump_only=True),
        'title': fields.String(required=True, description='title'),
        'summary': fields.String(required=True, description='summary'),
        'content': fields.String(required=True, description='content'),
        'created_at': fields.DateTime(required=True, description='created_at'),
        'created_by': fields.String(required=True, description='created_by')
    })
    entry = api.model('news_entry', {
        'title': fields.String(required=True, description='title'),
        'summary': fields.String(required=True, description='summary'),
        'content': fields.String(required=True, description='content'),
        'created_by': fields.String(required=True, description='created_by')
    })

