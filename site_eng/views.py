from django.shortcuts import render, redirect
from .forms import  AddCommentEng
from django.contrib import messages
from .models import ReviewEng, CommentEng


def welcomePage(request):
	"""view function to render the welcome page"""

	#if the user is not filling the form but
	#on the page then we just render the page
	#and the form to fill
	return render(request, 'welcomepage.html')


def reviewPage(request):
	"""view function to render the page with all reviews and comments"""

	#collect all the queries from the database
	#for all the comments and all the reviews
	reviews = ReviewEng.objects.all()

	comments = CommentEng.objects.all()

	#pass the reviews and comments in the dictionary
	#to render them on the html page
	context = {'reviews':reviews, 'comments':comments}

	return render(request, 'review.html', context)


def createCommentForBlog(request):
	"""view function for rendering the page with form for blogs"""

	#creating dictionary to pass the AddCommentEng form to the page
	#and render it in the html document 
	context = {"form":AddCommentEng}


	#when the user will fill in the form
	#a post request will be send and I 
	#need to save the form and redirect 
	#the user to the comment they created
	if request.method == 'POST':
		form = AddCommentEng(request.POST or None)

		#check if the form is valid and save it if it is
		if form.is_valid():
			form.save()

			#a message will popup sayuing that the comment has been added
			messages.success(request, "Comment has been added!")

			#then we redirect the user to the page with all the blogs
			return redirect('reviewPage')

	#rendering the page and form
	return render(request, 'form.html', context)

