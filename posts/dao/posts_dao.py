import json
from json import JSONDecodeError
from posts.dao.post import Post


class PostsDao:

	def __init__(self, path: str):
		""" Укажите путь к файлу с данными для создания экземпляра класса"""
		self.path = path

	def _load_data(self) -> list:
		""" Загружает данные из файла и возвращает список экземпляров класса Post"""
		try:
			with open(self.path, 'r', encoding="utf-8") as file:
				data = json.load(file)
				instances = [Post(**item) for item in data]
				return instances
		except FileNotFoundError:
			print("Файл не найден")
		except JSONDecodeError:
			print("Файл не удается преобразовать")

	def load_all(self):
		""" Возвращает список экземпляров класса Post"""
		data = self._load_data()
		hashtags = []
		for i in data:
			for word in i.content.split():
				if word[0] == "#":
					hashtags.append(word)
				if word in hashtags:
					link = f'<a href="/tag/{word[1:]}">{word}</a>'
					i.content = i.content.replace(word, link, 1)
		return data

	def get_post_by_username(self, username: str) -> list:
		""" Возвращает список экземпляров класса Post по имени пользователя"""
		data = self.load_all()
		result = []
		for i in data:
			if i.poster_name == username.lower():
				result.append(i)
		return result

	def get_post_by_pk(self, pk: int):
		""" Возвращает экземпляр класса Post по номеру поста"""
		data = self.load_all()
		hashtags = []
		for i in data:
			if i.pk == pk:
				for word in i.content.split():
					if word[0] == "#":
						hashtags.append(word)
					if word in hashtags:
						link = f'<a href="/tag/{word[1:]}">{word}</a>'
						i.content = i.content.replace(word, link, 1)
				return i
		return None

	def search_for_posts(self, query: str) -> list:
		""" Возвращает экземпляры класса Post по ключевому слову в тексте поста"""
		data = self.load_all()
		result = []
		for i in data:
			if query.lower() in i.content.lower():
				result.append(i)
		return result




# po = PostsDao('posts.json')
# posts = print(po.get_post_by_pk(1).content)

