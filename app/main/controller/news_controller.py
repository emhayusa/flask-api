from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import NewsDto
from ..service.news_service import save_new, get_all, get_by_id
#from ..util.decorator import admin_token_required, token_required

api =  NewsDto.api
_schema =  NewsDto.schema
_entry =  NewsDto.entry

@api.route('/')
class NewsList(Resource):
    @api.doc('list of news')
    @api.marshal_list_with(_schema, envelope='data')
    #@admin_token_required
    def get(self):
        """List all news"""
        return get_all()

    @api.response(201, 'News successfully created.')
    @api.doc('create a new news')
    @api.expect(_entry, validate=True)
    #@admin_token_required
    def post(self):
        """Creates a new news"""
        data = request.json
        return save_new(data=data)

@api.route('/<int:id>')
@api.param('id', 'The News id')
@api.response(204, 'News not found.')
class News(Resource):
    @api.doc('get a news')
    @api.marshal_with(_schema)
    #@admin_token_required
    def get(self, id):
        """get a news given its id"""
        row = get_by_id(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'News ID is not found.',
        	}
        	return response_object, 204
        else:
            return row


