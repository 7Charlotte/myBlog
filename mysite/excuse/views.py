from django.shortcuts import render
from django.http import HttpResponse
from excuse.models import Excuse
import random


# Create your views here.
def home(request):
    excuse = random.choice(Excuse.objects.all())
    return render(request, "index.html", {'excuse': excuse})