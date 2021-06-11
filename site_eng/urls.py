from django.urls import path
from . import views

urlpatterns = [
    #default path for welcome page
    path('',views.welcomePage, name='welcomePage' ),

    #path for forms page
    path('comment-form', views.createCommentForBlog, name ='createCommentForBlog'),

    #path for review page
    path('review-page', views.reviewPage, name = 'reviewPage')
]