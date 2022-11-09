from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account


def homePageView(request):
	return render(request, 'index.html')


@login_required
def transferView(request):
	request.session['to'] = request.GET.get('to')
	request.session['likes'] = int(request.GET.get('likes'))
	return render(request, 'pages/confirm.html')


