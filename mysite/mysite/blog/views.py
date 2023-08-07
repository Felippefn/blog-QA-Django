#blog views.py

from django.shortcuts import redirect, render
from django.views import generic
from .models import Post

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

def about_me(request):
    return render(request, 'about.html')

def my_profile(request):
    if request.user.is_authenticated:
        return render(request, 'my_profile.html', {'username': request.user.username})
    else:
        return redirect('login')
    

def get_contact(request):

    return render(request, 'contact.html')