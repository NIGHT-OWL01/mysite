from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import quiz
# Create your views here.

def quizView(request):
    if request.method=='GET':
        quizes=quiz.objects.all()
        context={"quizes":quizes}
        return render(request,'quiz.html',context)
    if request.method=='POST':
        print(request.POST)
        return redirect('/')