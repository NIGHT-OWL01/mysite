from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from datetime   import datetime,date
from .models import QrCode
import pyqrcode
import png
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'index.html')

def time_since_created(request):
    now=datetime.now().date()
    print('now :',now)
    created = date(2022,9,11)
    print('created : ',created)
    days=now-created
    print(days)
    return HttpResponse(f'today : {now} <br> created {created} <hr> days passed {days}')


def QrCodeView(request):
    img=pyqrcode.create('https://www.google.com/')
    # QrCode.objects.create(title='no title',img=img.png('img01',scale=6))
    img.png('some')
    return HttpResponse(f'{img}')

# def send_Mail(request):
#     s=send_mail(
#         'subject',
#         'msg',
#         'ganeshp.ap07@gmail.com',
#         ['ganeshp.py07@gmail.com','ganeshp7754@gmail.com'],
#         fail_silently=False
#     )
#     return HttpResponse(s)

def session_read(request):
    print(request.session.items())
    request.session['color']='red'
    request.session['token']='Token'
    return HttpResponse(request.session)
import random
# @login_required(login_url='accounts/login/')
def rock_paper_scissor(request):
    if request.method=='GET':
        code=''
        return render(request,'rock_paper.html')

    if request.method=='POST':
        print('POST called')
        print(request.POST['player'])
        player_move=request.POST['player'].lower()
        choices=['rock','paper','scissor']
        bot_move = random.choice(choices).lower()
        result=''
        if bot_move==player_move:
            result='Tie'
        elif bot_move=='rock' and player_move=='scissor' or bot_move=='paper' and player_move=='rock' or bot_move=='scissor' and player_move=='paper':
            result='Bot won!'
        else:
            result='You Won!'
        # return HttpResponse(f'Bot Move : {bot_move}, Your Move : {player_move},<hr>Result : {result}')
        messages.info(request,f'Result : {result}')
        messages.info(request,f'Your Move : {player_move}')
        messages.info(request,f'Bot Move : {bot_move}')
        return redirect('/')
def test_API(request):
    return JsonResponse({"sum":"value","second":"book","third":'animal'})
def fetch_page(request):
    return render(request,'fetch.html')

from datetime import datetime
import pytz
def time(request):
    UTC = pytz.utc
    IST = pytz.timezone("Asia/Kolkata")
    day_and_time=datetime.now(IST)
    print(day_and_time.day)
    return JsonResponse({"time":day_and_time.strftime("%H:%M:%S"),"date":day_and_time.date()})