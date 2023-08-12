#blog views.py

from django.shortcuts import redirect, render
from django.views import generic
from .models import Post
from qna.models import Question, Answer
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'indexblog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

def my_profile(request):
    # Retrieve the user's questions and posts
    questions = Question.objects.filter(author=request.user)
    posts = Post.objects.filter(author=request.user)

    # Combine questions and posts in the content list
    content = list(questions) + list(posts)
    question_list = list(questions)
    post_list = list(posts)
    question_list_length = len(question_list)  # Use len() instead of lenght()
    post_list_length = len(post_list)

    context = {
        'username': request.user.username,
        'content': content,
        'question_list': question_list,
        'post_list': post_list,
        'question_list_length': question_list_length,
        'post_list_length': post_list_length
    }
    return render(request, 'my_profile.html', context)
# @method_decorator(login_required, name='dispatch')
# class MyProfile(generic.DetailView):
#     template_name = 'my_profile.html'
#     context_object_name = 'contentProfile'
    
#     def get_object(self, queryset=None):
#         return self.request.user

#     def get_queryset(self):
#         # Retrieve both questions and posts made by the user (self.request.user)
#         # Use Q objects to filter on multiple fields (author in Question and user in Post)
#         return (Question.objects.filter(author=self.request.user.username) |
#                 Post.objects.filter(user=self.request.user))


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['username'] = self.request.user.username
#         return context

def about_me(request):
    return render(request, 'about.html')

    

def get_contact(request):

    return render(request, 'contact.html')