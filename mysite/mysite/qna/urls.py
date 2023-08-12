#qna urls.py

from . import views
from django.urls import path

urlpatterns = [
    path('questions/', views.QuestionList.as_view(), name='main'),
    path('create-question/', views.create_question, name='create_question'),
    path('<slug:slug>/', views.QuestionDetail.as_view(), name='question_detail'),
    path('<slug:question_slug>/post-answer/', views.post_answer, name='post_answer')
]