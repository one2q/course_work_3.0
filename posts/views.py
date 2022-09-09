from flask import Blueprint, render_template, request

from posts.dao.comments_dao import CommentsDao
from posts.dao.posts_dao import PostsDao

POSTS_PATH = './data/posts.json'
COMMENTS_PATH = './data/comments.json'

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDao(POSTS_PATH)
comments_dao = CommentsDao(COMMENTS_PATH)


# Главная страница с постами
@posts_blueprint.route('/')
def page_all_posts():
	posts = posts_dao.load_all()
	return render_template('index.html', posts=posts)


# Страница поста по номеру pk
@posts_blueprint.route('/post/<int:pk>')
def get_post_by(pk):
	post = posts_dao.get_post_by_pk(pk)
	comments = comments_dao.load_by_pk(pk)
	num_of_comments = len(comments)
	return render_template('post.html', post=post, comments=comments, num=num_of_comments)


# Страница поиска
@posts_blueprint.route('/search', methods=["GET"])
def search_posts():
	search = request.args.get("search")
	posts = posts_dao.search_for_posts(search)
	return render_template('search.html', posts=posts)


# Страница постов выбранного юзера
@posts_blueprint.route('/users/<username>')
def get_post_by_username(username):
	user_posts = posts_dao.get_post_by_username(username)
	return render_template('user-feed.html', posts=user_posts)


# Страница тэгов
@posts_blueprint.get('/tag/<tagname>')
def get_post_by_tag(tagname):
	user_posts = posts_dao.search_for_posts(tagname)
	return render_template('tag.html', posts=user_posts, tagname=tagname)
