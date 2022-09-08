from flask import Blueprint, request, jsonify

from posts.dao.posts_dao import PostsDao

POSTS_PATH = './data/posts.json'

posts_dao = PostsDao(POSTS_PATH)

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')


@api_blueprint.route('/api/posts', methods=["GET"])
def all_posts():
	posts = posts_dao.load_all()
	return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>', methods=["GET"])
def page_post_by_pk(post_id):
	post = posts_dao.get_post_by_pk(post_id)
	# Проверить возвращает нон
	return jsonify(post)