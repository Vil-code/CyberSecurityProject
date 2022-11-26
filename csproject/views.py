from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account

@login_required
def homePageView(request):
	accounts = Account.objects.exclude(user_id=request.user.id)
	return render(request, 'index.html', {'accounts': accounts})

@login_required
def transferView(request):
	request.session['to'] = request.GET.get('to')
	to = User.objects.get(username=request.session['to'])
	to.account.likes += 1
	to.account.save()
	return redirect('/')


