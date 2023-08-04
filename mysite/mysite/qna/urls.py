#qna urls.py

from . import views
from django.urls import path

urlpatterns = [
    path('questions/', views.QuestionList.as_view(), name='main'),
    path('<slug:slug>/', views.QuestionDetail.as_view(), name='question_detail'),
    path('create_question/', views.create_question, name='create_question'),
]