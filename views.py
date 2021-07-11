from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.


def index(request):

	return render(request ,'quiz/index.html' )


def questions(request):

	questions = Questions.objects.all()

	context = {'questions' : questions }

	return render(request, 'quiz/questions.html', context)





	

	