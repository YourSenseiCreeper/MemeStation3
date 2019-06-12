from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import datetime

from memes.models import Meme
from memes.forms import AddMeme

# def oops(request):
#     args = {'user': request.user}
#     return render(request, 'memes/oops.html', args)

def index(request):
    # It's okey, no worries
    all_memes = Meme.objects.filter(waiting=False).order_by('-publication_date')
    args = {'all_memes': all_memes, 
    'user': request.user, 
    'liked': [meme.likes.filter(id=request.user.id).exists() for meme in all_memes],
    'dislikes': [meme.dislikes for meme in all_memes]}

    # profile_link = '{% url 'admin:index' %}' if args['user'].is_authenticated and args['user'].is_superuser else '{% url 'memes:index' %}'
    # logged = True if args['user'].is_authenticated else False
    # args['profile_link'] = profile_link
    # args['logged'] = logged

    if request.method == 'GET':
        return render(request, 'memes/index.html', args)
    else:
    	# Get the amount of likes per meme
    	# 
        # moved_meme = Meme.objects.get(pk=request.POST['meme_id'])
        # if moved_meme.waiting:
        #     moved_meme.waiting = False
        # else:
        #     moved_meme.waiting = True
        # moved_meme.save()
        # It's possible it won't refresh the page at the first time
        return render(request, 'memes/index.html', args)

def waitingroom(request):
	all_memes = Meme.objects.filter(waiting=True).order_by('-add_date')
	args = {'all_memes': all_memes, 'user': request.user, 'likes': [meme.likes for meme in all_memes], 
    'dislikes': [meme.dislikes.count() for meme in all_memes]}
	return render(request, 'memes/index.html', args)

def user(request, user):
    user = User.objects.get(username=user)
    memes = Meme.objects.filter(author=user.username)
    if user is None:
        raise Http404("User does not exist")
    else:
        args = {'user': request.user, 'user_profile': user, 'memes': memes}
        return render(request, 'memes/user.html', args)

def logout_view(request):
    logout(request)
    return redirect('memes:index')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = UserCreationForm()
		args = {'form': form}
		return render(request, 'memes/register.html', args)

# @login_required(login_url="/login/")
def meme_add(request):
    # if this is a POST request we need to process the form data
    args = {'form': AddMeme(), 'user': request.user}
    if request.method == 'POST' and request.user is not None:
        form = AddMeme(request.POST, request.FILES)
        if form.is_valid():
            internal = form.save(commit=False)
            internal.author = request.user
            internal.save()
            return redirect('memes:index')
    # if a GET (or any other method) we'll create a blank form
    return render(request, 'memes/add.html', args)

def meme_like(request):
    if request.method == 'POST':
        meme = Meme.objects.get(pk=request.POST.get('meme_id'))
    	# is_liked = False
        if meme.likes.filter(id=request.user.id).exists():
            meme.likes.remove(request.user)
            meme.likes_number = meme.likes_number -1
        else:
            meme.likes.add(request.user)
            meme.likes_number = meme.likes_number +1 

        meme.save()
    return redirect('/')

def meme_dislike(request):
	meme = Memes.objects.get(pk=request.POST.get('meme_id'))
	meme.dislikes.add(request.user)
	return redirect('/')

def status(request):
    if request.method == 'POST':
        meme = Meme.objects.get(pk=request.POST.get('meme_id'))
        if meme.waiting:
            meme.waiting = False
            meme.publication_date = datetime.datetime.now()
        else:
            meme.waiting = True
        meme.save()
        return index(request)