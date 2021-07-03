from django.db import models
from datetime import date

class ReviewEng(models.Model):
	"""Model for writting reviews in English"""

	#the title of the book
	book_title = models.CharField(max_length = 50)

	#Book author name
	book_author = models.CharField(max_length = 100)

	#Your review of this book
	review_text = models.TextField()

	#Review author name
	review_author = models.CharField(max_length = 100, blank = True)

	#Review publication date
	review_pub_date = models.DateField(default=date.today().strftime('%d/%m/%Y'))

	def __str__(self):
		return self.book_title

class CommentEng(models.Model):

	review = models.ForeignKey(ReviewEng, related_name="comments" ,on_delete = models.CASCADE)

	#Comment text
	comment_text = models.TextField(default = " ")

	#Comment author
	comment_author = models.CharField(max_length = 100, blank = True)

	#Comment publication date
	comment_pub_date = models.DateField(default=date.today().strftime('%d/%m/%Y'))

	def __str__(self):
		return self.comment_author