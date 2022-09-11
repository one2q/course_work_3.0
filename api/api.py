from flask import Blueprint, request, jsonify

from logger_api import logger_api
from posts.dao.posts_dao import PostsDao

POSTS_PATH = './data/posts.json'

posts_dao = PostsDao(POSTS_PATH)

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')


@api_blueprint.get('/api/posts')
def all_posts():
	posts = posts_dao.load_all()
	logger_api.warning("Запрошены все посты")
	return jsonify([post.get_dict() for post in posts]), 200


@api_blueprint.get('/api/posts/<int:post_id>')
def page_post_by_pk(post_id):
	post = posts_dao.get_post_by_pk(post_id)
	logger_api.warning(f'Запрос api/posts/{post_id}')
	return jsonify(post.get_dict()), 200