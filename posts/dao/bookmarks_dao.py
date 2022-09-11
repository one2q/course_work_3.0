import json
from json import JSONDecodeError

from posts.dao.posts_dao import PostsDao


class Bookmarks:
	"""
	Это экземпляр класса закладки, он может добавить пост в закладки
	или удалить его из закладок.
	"""

	def __init__(self, path: str, posts_path='./data/posts.json'):
		"""
		:param path: Путь к файлу с закладками
		:param posts_path: Путь к файлу с постами
		"""
		self.path = path
		self.posts_path = posts_path

	def load_bookmarks(self):
		"""
		Метод, загружает все закладки
		:return: Список постов в закладках
		"""
		try:
			with open(self.path, 'r', encoding="utf-8") as file:
				data = json.load(file)
				return data
		except FileNotFoundError:
			print("Файл не найден")
		except JSONDecodeError:
			print("Файл не удается преобразовать")

	def add_bookmarks(self, pk):
		"""
		Добавляет пост в закладки
		:param pk: Номер поста
		"""
		bookmarks = self.load_bookmarks()
		posts = PostsDao(self.posts_path)
		post = posts.get_post_by_pk(pk).get_dict()
		bookmarks.append(post)
		with open(self.path, 'w', encoding='utf-8') as file:
			json.dump(bookmarks, file, ensure_ascii=False)


	def del_bookmark(self, pk):
		"""
		Удаляет пост из закладок
		:param pk: Номер поста
		"""
		bookmarks = self.load_bookmarks()
		for i in bookmarks:
			if i['pk'] == pk:
				bookmarks.remove(i)
				with open(self.path, 'w', encoding='utf-8') as file:
					json.dump(bookmarks, file, ensure_ascii=False)
				break
