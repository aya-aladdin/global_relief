from django.shortcuts import render, redirect

def home(request):
    return render(request, "home.html")

def adhd(request):
    return render(request, "adhd.html")

def donate(request):
    return render(request, "donate.html")