import html
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Account

@login_required
def homePageView(request):
	accounts = Account.objects.exclude(user_id=request.user.id)
	return render(request, 'index.html', {'accounts': accounts})

# @login_required
def likeView(request):
	request.session['to'] = request.GET.get('to')
	to = User.objects.get(username=request.session['to'])
	to.account.likes += 1
	to.account.save()
	return redirect('/')

@login_required
def profileView(request):
	profile = request.POST['profile']
	# profile = html.escape(profile)
	print(profile)
	accounts = Account.objects.exclude(user_id=request.user.id)
	cur_acc = Account.objects.get(user_id=request.user.id)
	cur_acc.profile = profile
	cur_acc.save()
	return redirect('/')
