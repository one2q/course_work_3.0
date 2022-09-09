class Comment:

	def __init__(self, pk=0, post_id=0, commenter_name='', comment=''):
		self.pk = pk
		self.post_id = post_id
		self.commenter_name = commenter_name
		self.comment = comment

	def __repr__(self):
		return f'Comment {self.pk} к посту {self.post_id}'
