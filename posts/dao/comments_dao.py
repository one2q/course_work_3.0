import json
from json import JSONDecodeError

from posts.dao.comment import Comment


class CommentsDao:

	def __repr__(self):
		""" Экземпляр класса CommentsDao"""

	def __init__(self, path: str):
		""" Укажите путь к файлу с данными для создания экземпляра класса Comment"""
		self.path = path

	def load_data(self) -> list:
		""" Загружает данные из файла и возвращает список экземпляров класса Comment"""
		try:
			with open(self.path, 'r', encoding="utf-8") as file:
				data = json.load(file)
				instances = [Comment(**item) for item in data]
				return instances
		except FileNotFoundError:
			print("Файл не найден")
		except JSONDecodeError:
			print("Файл не удается преобразовать")

	def load_all(self):
		""" Возвращает список экземпляров класса Comment"""
		data = self.load_data()
		return data

	def load_by_pk(self, pk: int) -> list:
		""" Возвращает список экземпляров класса Comment к посту с номером pk"""
		data = self.load_data()
		result = []
		for i in data:
			if i.post_id == pk:
				result.append(i)
		return result
