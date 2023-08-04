# qna views.py

from django.shortcuts import get_object_or_404, redirect, render
from .models import Question
from django.views import generic
from .forms import QuestionForm, AnswerForm

class QuestionList(generic.ListView):
    queryset = Question.objects.filter(status=0).order_by('-created_on')
    template_name = 'indexqa.html'


class QuestionDetail(generic.DetailView):
    model = Question
    template_name = 'question_detail.html'

    # def check_user_authenticated(request):
    #     if request.user.is_authenticated:
    #         pass
    #     else:
    #         return redirect('login')

def create_question(request):
    if request.user.is_authenticated:
           if request.method == 'POST':
                form = QuestionForm(request.POST)
                if form.is_valid():
                    form.instance.author = request.user.username
                form.save()
                return redirect('/questions')
    else:
         redirect('login')

def post_answer(request, question_slug):
    question = get_object_or_404(Question, slug=question_slug)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.question = question
                answer.author = request.user.username
                answer.save()
                return redirect('question_detail', question_slug=question_slug)
    else:
        return redirect('login')

def change_question_status(request, question_slug):
    question = get_object_or_404(Question, slug=question_slug)

    # Check if the user is authenticated and is the author of the question
    if request.user.is_authenticated and question.can_change_status(request.user):
        # Assume the new_status value comes from the form data or somewhere else
        new_status = 1  # Assuming you want to change it to "Solved"
        question.change_status(request.user, new_status)
        # Redirect or do something else after the status is changed
        return redirect('question_detail', question_slug=question_slug)  # Change 'question_detail' to your question detail view name
    else:
        # Handle unauthorized access here (e.g., show an error message or render a template)
        return render(request, 'unauthorized.html')  # Replace 'unauthorized.html' with the template name for unauthorized access

