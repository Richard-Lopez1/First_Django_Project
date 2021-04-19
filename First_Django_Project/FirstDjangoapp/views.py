from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse('<h1>Placeholder to later display a list of all bull bear profits</h1>')

def new(request):
    return HttpResponse('<h1>Placeholder to display a new form to create a new blog<h1>')

def create(request):
    return redirect('/')    

def show(request, number):
    return HttpResponse(f"placeholder to display blog number {number}.")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}.")
    
def destroy(request, number):
    return redirect('/')