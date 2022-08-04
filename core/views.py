from ast import Is
from statistics import mode
from unittest import mock
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import News, Comments
from .serializers import CommentsSerializer, NewSerializer
from rest_framework import permissions
from .permissions import IsOwner
# Create your views here.

def test(request):
    return HttpResponse("Salam")



class NewsView(generics.ListCreateAPIView):
    # every autheticated user can create post and see all posts. 
    queryset = News.objects.all()
    serializer_class = NewSerializer
    # IsAuthenticated defined in setting. No need to specify here

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

   


class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewSerializer

    permission_classes = [IsOwner] # only owner can Update, Delete obj



class CommentsView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    # IsAuthenticated defined in setting. No need to specify here


class CommentsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsOwner] # only owner can Update, Delete obj


class UpvoteNews(generics.RetrieveAPIView):
    queryset = News.objects.all()
    # id = kwargs.get('id')