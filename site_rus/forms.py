from django.forms import ModelForm
from .models import ReviewRus, CommentRus

#class to add a review
class AddReviewRus(ModelForm):
	
	class Meta:
		#This references the model from which it should take the fields
		model = ReviewRus

		#Names of fields for html forms
		fields = ['book', 'book_author', 'review_text', 'review_author', 'review_pub_date']	

#class to add a comment
class AddCommentRus(ModelForm):

	class Meta:
		#This references the model from which it should take the fields
		model = CommentRus

		#Names of fields for html forms
		fields = ['review', 'comment_text', 'comment_author', 'comment_pub_date']