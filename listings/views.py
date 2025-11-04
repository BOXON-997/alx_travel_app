from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(requests):
    return JsonResponse({'message': 'Welcome to ALX Trave App Listings API!'})
