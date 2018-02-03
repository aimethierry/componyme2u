# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MyModelForm, SignUpForm
from .models import compony, users
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ComponylistSerializer, UserlistSerializer, ClientSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



# for api
def home(request):
    return render(request, "asco/home.html")


class ComponyCreateAPIView(generics.ListCreateAPIView):
    queryset = users.objects.all()
    serializer_class = ComponylistSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserlistSerializer
   
class ClientCreateAPIView(generics.ListAPIView):
    queryset = compony.objects.all()
    serializer_class = ClientSerializer
 


#for list api
class ComponyListAPIView(generics.ListAPIView):
    queryset = users.objects.all()
    serializer_class = ComponylistSerializer
  
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserlistSerializer
    

class ClientListAPIView(generics.ListAPIView):
    queryset = compony.objects.all()
    serializer_class = ClientSerializer
  
    


#for details and put
class ComponyADetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = users.objects.all()
    serializer_class = ComponylistSerializer
  

class UserADetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserlistSerializer




#for deleting

class UserDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserlistSerializer


class ComponyDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = users.objects.all()
    serializer_class = ComponylistSerializer


    




'''
def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)
'''

#
# def list(request):
#     name = Titi.objects.all()
#
#     answer_data = {
#     "answer_detail" : answer_info
#     }
#
# print answer_data
#  return render_to_response('quizzes.html'', answer_data, context_instance=RequestContext(request))
