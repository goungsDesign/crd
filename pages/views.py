from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def homeView(request):
    context = {"current_page": "home"}  # Set a flag to indicate the current page
    return render(request, 'pages/home.html', context=context)
def aboutView(request):
    context = {"current_page": "about"}  # Set a flag to indicate the current page
    return render(request, 'pages/about.html', context=context)

def contactView(request):
    context = {"current_page": "contact"}  # Set a flag to indicate the current page
    return render(request, 'pages/contact.html', context=context)

def serviceView(request):
    context = {"current_page": "service"}  # Set a flag to indicate the current page
    return render(request, 'pages/services.html', context=context)

def service_researchView(request):
    context = {"current_page": "research_service"}  # Set a flag to indicate the current page
    return render(request, 'pages/service_recherche.html', context=context)

def consultingView(request):
    return render(request, 'pages/consulting.html')
def service_dataView(request):
    return render(request, 'pages/service_donnees.html')
