from hashlib import new
import random
import string
from django.shortcuts import render
from django.http import HttpResponse
from tickets.models import * 

def randomString(strLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(strLength))

def index(request):
    return render(request,'index.html')

def submit(request):
#    new_ticket = Ticket(submitter=randomString(10),body="Help , I need Help with bug !!")  
 #   new_ticket.save()
    if request.method == 'POST':
        username=request.POST.get('username')
        body=request.POST.get('body')
        new_ticket = Ticket(submitter=username,body=body)
        new_ticket.save()
        return HttpResponse("Hello Rochak!")
    return render(request,'submit.html')

def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request,'tickets.html',{'tickets':all_tickets})
