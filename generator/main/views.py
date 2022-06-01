from django.shortcuts import render
import string
import random


def home(request):
	return render(request, 'main/home.html')


def password(request):
	alphabet = string.ascii_lowercase

	if request.GET.get('uppercase'):
		alphabet += string.ascii_uppercase

	if request.GET.get('numbers'):
		alphabet += '1234567890'

	if request.GET.get('special'):
		alphabet += '!@#$%^&*()_-+-='

	length = int(request.GET.get('length', 8))
	the_password = ''
	for i in range(length):
		the_password += random.choice(alphabet)
	return render(request, 'main/password.html', {'password': the_password})