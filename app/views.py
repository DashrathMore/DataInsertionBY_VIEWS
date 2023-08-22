from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_lib (request):
    se=input("Enter section : ")
    so=Liabrary.objects.get_or_create(section=se)[0]
    so.save()
    return HttpResponse('<h1>DATE Inserted ')

def insert_Book(request):
    se=input('enter Section : ')
    """so=Liabrary.objects.get_or_create(section=se)[0]
    so.save()"""
    so=Liabrary.objects.get(section=se)
    nm=input('enter name of Book :')
    at=input('Enter name of auther :')
    bo=Books.objects.get_or_create(section=so, Bname=nm, auther=at)[0]
    bo.save()
    return HttpResponse('<h1>DATE Inserted ')

def insert_reader(request):
    rid=int(input('Enter rid :'))
    rn=input('Enter name : ')
    em=input('enter mail id :')
    ro=reader.objects.get_or_create(Rid=rid, Rname=rn, Email=em)[0]
    ro.save()
    return HttpResponse('<h1>DATE Inserted..................... ')


def insert_reading(request):
    id=int(input('enter your id : '))
    io=reader.objects.get(Rid=id)
    bn=input('enter Book name : ')
    bo=Books.objects.get(Bname=bn)
    td=input('Enter taking date : ')
    sd=input('Enter submit date : ')
    ro=reading.objects.get_or_create(Rid=io, Bname=bo, Tdate=td, Sdate=sd)[0]
    ro.save()
    return HttpResponse('<h1>DATE Inserted..................... ')
