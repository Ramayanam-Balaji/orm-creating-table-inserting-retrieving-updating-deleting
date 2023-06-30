from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import *
def insert_Topic(request):
    tn=input('enter topic name')
    t1=Topic.objects.get_or_create(Topic_Name=tn)[0]
    t1.save()
    return HttpResponse('topic data is inserted')
def insert_Webpage(request):
    tn=input('enter topic name')
    t1=Topic.objects.get_or_create(Topic_Name=tn)[0]
    t1.save()
    n=input('enter name')
    u=input('enter url')
    t2=Webpage.objects.get_or_create(Topic_Name=t1,Name=n,url=u)[0]
    t2.save()

    return HttpResponse('webpage data is inserted')
def insert_AccessRecord(request):
    tn=input('enter topic name')
    t1=Topic.objects.get_or_create(Topic_Name=tn)[0]
    t1.save()
    n=input('enter name')
    u=input('enter url')
    t2=Webpage.objects.get_or_create(Topic_Name=t1,Name=n,url=u)[0]
    t2.save()

    d=input('enter date')
    a=input('enter author name ')
    t3=AccessRecord.objects.get_or_create(Name=t2,date=d,author=a)[0]
    t3.save()
    return HttpResponse('Accessrecord is inserted')

def display_Topic(request):
    t4=Topic.objects.all()
    d={'t4':t4}
    return render(request,'display_Topic.html',d)
def display_Webpage(request):
    t5=Webpage.objects.all()
    d={'t5':t5}
    return render(request,'display_Webpage.html',d)
def display_AccessRecord(request):
    t6=AccessRecord.objects.all()
    d={'t6':t6}
    return render(request,'display_AccessRecord.html',d)
def update_Webpage(request):
    Webpage.objects.filter(Name='virat').update(url='https://virat.com')
    Webpage.objects.update_or_create(Name='virat',defaults={'url':'https://virat.in'})
    t7=Webpage.objects.all()
    d={'t7':t7}
    return render(request,'display_Webpage.html',d)
def delete_Webpage(request):
    Topic.objects.filter(Topic_Name='rugby').delete()
    t9=Topic.objects.all()
    d={'t9':t9}
    return render(request,'display_Webpage.html',d)

