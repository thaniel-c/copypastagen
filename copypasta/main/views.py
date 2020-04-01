from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import json
import random

with open("/home/nathan/Desktop/copypasta/copypasta/main/static/data.json", 'r') as f:
    posts_dict = json.load(f)

def gen():
    # Create your views here
    global p
    p = []
    p.append(posts_dict[random.randint(0, 24)])

gen()

def home(request):
    context = {
        'posts': p
    }
    gen()
    return render(request, 'main/index.html', context)