import json


class PostsDao:

	def __repr__(self):
		""" Экземпляр класса PostsDao"""

	def __init__(self, path: str):
		""" Укажите путь к файлу с данными для создания экземпляра класса"""
		self.path = path

	def load_data(self) -> list:
		""" Загружает данные из файла и возвращает список"""
		with open(self.path, 'r', encoding="utf-8") as file:
			data = json.load(file)
			return data

	def load_all(self):
		""" Возвращает список всех постов"""
		data = self.load_data()
		return data

	def get_post_by_username(self, username: str) -> list:
		""" Возвращает пост по имени пользователя"""
		data = self.load_all()
		result = []
		for i in data:
			if i['poster_name'] == username.lower():
				result.append(i)
		return result

	def get_post_by_pk(self, pk: int) -> dict | None:
		""" Возвращает пост по номеру поста"""
		data = self.load_all()
		for i in data:
			if i['pk'] == pk:
				return i
		return None

	def search_for_posts(self, query: str):
		""" Возвращает пост по ключевому слову в тексте поста"""
		data = self.load_all()
		result = []
		for i in data:
			if query.lower() in i["content"].lower():
				result.append(i)
		return result



# po = PostsDao('posts.json')
# print(po.get_post_by_username('leo'))
