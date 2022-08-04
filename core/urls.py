from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsView.as_view()),
    path('news/<int:pk>/', views.NewsDetailAPIView.as_view()),
    path('news/<int:pk>/upvote/', views.UpvoteNews.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('comments/<int:pk>/', views.CommentsDetailAPIView.as_view(), name='comment-detail'),

]