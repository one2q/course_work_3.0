class Post:

	def __repr__(self):
		return f'Экземпляр класса Post, pk {self.pk}'

	def __init__(self, poster_name='', poster_avatar='', pic='', content='', views_count=0, likes_count=0, pk=0):

		self.pk = pk
		self.poster_name = poster_name
		self.poster_avatar = poster_avatar
		self.pic = pic
		self.content = content
		self.views_count = views_count
		self.likes_count = likes_count

	def get_dict(self):
		result_dict = {

			'pk': self.pk,
			'poster_name' : self.poster_name,
			'poster_avatar' : self.poster_avatar,
			'pic' : self.pic,
			'content': self.content,
			'views_count': self.views_count,
			'likes_count': self.likes_count,

		}
		return result_dict


