from django.forms import ModelForm
from .models import ReviewEng, CommentEng

#class to add a review
class AddReviewEng(ModelForm):
	
	class Meta:
		#This references the model from which it should take the fields
		model = ReviewEng

		#Names of fields for html forms
		fields = ['book_title', 'book_author', 'review_text', 'review_author', 'review_pub_date']	

#class to add a comment
class AddCommentEng(ModelForm):

	class Meta:
		#This references the model from which it should take the fields
		model = CommentEng

		#Names of fields for html forms
		fields = ['review', 'comment_text', 'comment_author', 'comment_pub_date']