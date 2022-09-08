import json


class CommentsDao:

	def __repr__(self):
		""" Экземпляр класса CommentsDao"""

	def __init__(self, path: str):
		""" Укажите путь к файлу с данными для создания экземпляра класса"""
		self.path = path

	def load_data(self) -> list:
		""" Загружает данные из файла и возвращает список"""
		with open(self.path, 'r', encoding="utf-8") as file:
			data = json.load(file)
			return data

	def load_all(self):
		""" Возвращает список всех комментов"""
		data = self.load_data()
		return data

	def load_by_pk(self, pk: int) -> list:
		""" Возвращает список всех комментов к посту с номером pk"""
		data = self.load_data()
		result = []
		for i in data:
			if i["post_id"] == pk:
				result.append(i)
		return result
