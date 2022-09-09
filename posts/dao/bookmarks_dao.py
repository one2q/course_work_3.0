import json
from json import JSONDecodeError

from posts.dao.posts_dao import PostsDao


class Bookmarks:

	def __init(self, path):
		self.path = path

	def load_bookmarks(self):
		try:
			with open(self.path, 'r', encoding="utf-8") as file:
				data = json.load(file)
				return data
		except FileNotFoundError:
			print("Файл не найден")
		except JSONDecodeError:
			print("Файл не удается преобразовать")

	# def add_bookmarks(self, pk):
	# 	posts = PostsDao()
	# 	post = .get_post_by_pk(pk)
	# 	with open(bookmarks_path, 'a', encoding='utf-8') as file:
	# 		json.dump(post, file, ensure_ascii=False)