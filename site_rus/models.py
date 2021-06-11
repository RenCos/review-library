from django.db import models

class ReviewRus(models.Model):
	#Title of the book
	book = models.CharField(max_length = 50)

	#Book author name
	book_author = models.CharField(max_length = 100)

	#Your review of this book
	review_text = models.TextField()

	#Review author name
	review_author = models.CharField(max_length = 100, blank = True)

	#Review publication date
	review_pub_date = models.DateField()

	def __str__(self):
		return self.book

class CommentRus(models.Model):

	review = models.ForeignKey(ReviewRus, on_delete = models.CASCADE)

	#Comment text
	comment_text = models.TextField()

	#Comment author
	comment_author = models.CharField(max_length = 100, blank = True)

	#Comment publication date
	comment_pub_date = models.DateField()

	def __str__(self):
		return self.comment_author