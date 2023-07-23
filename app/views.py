# views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import Question, Answer, Like

@login_required
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        question = Question.objects.create(title=title, content=content, author=request.user)
        question.save()
        return redirect('home')

    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'home.html', context)


@login_required
def answer_question(request, question_id):
    if request.method == 'POST':
        content = request.POST['content']
        question = Question.objects.get(pk=question_id)
        answer = Answer.objects.create(content=content, question=question, author=request.user)
        answer.save()
        return redirect('home')

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)
    if not created:
        like.delete()
    return redirect('home')

