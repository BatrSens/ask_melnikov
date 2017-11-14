from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from questions import questions

def auth():
	f = open('session', 'r')
	auth = f.read()
	f.close()
	return auth

def index(request):
    pagination_list = pagination(request, questions, 5)
    return render(request, 'index.html', {
        'title': 'JustAsk!!!',
        'auth': auth(),
        'questions': pagination_list,
        'pagination_list': pagination_list,
        'h_title': 'New questions',
    })

def ask(request):
	return render(request, 'ask.html', {
		'title': 'Ask',
		'auth': auth(),
	})

def question(request, quest_id):
    q = questions[int(quest_id)]
    pagination_list = pagination(request, q['answers'], 5)
    return render(request, 'question.html', {
        'title': q['title'] + str(q['id']),
        'auth': auth(),
        'answers': pagination_list,
        'pagination_list': pagination_list,
        'quest': q,
    })

def settings(request):
    return render(request, 'settings.html', {
		'title': 'Settings: Vitalya',
		'auth': auth(),
	})

def tag(request, tag_name):
    pagination_list = pagination(request, questions, 5)
    return render(request, 'index.html', {
        'title': 'Tag: ' + tag_name,
        'auth': auth(),
        'questions': pagination_list,
        'pagination_list': pagination_list,
        'h_title': 'Tag: ' + tag_name,
    })

def hot(request):
    pagination_list = pagination(request, questions, 5)
    return render(request, 'index.html', {
        'title': 'Hot',
        'auth': auth(),
        'questions': pagination_list,
        'pagination_list': pagination_list,
        'h_title': 'Hot questions',
    })

def signin(request):
	return render(request, 'signin.html', {
		'title': 'Sign in',
		'auth': auth(),
	})

def signup(request):
	return render(request, 'signup.html', {
		'title': 'Sign up',
		'auth': auth(),
	})

def login(request):
	f = open('session', 'w')
	f.write('1')
	f.close()
	return redirect('/')

def logout(request):
	f = open('session', 'w')
	f.close()
	return redirect('/')

def pagination(request, objects, objects_count):
	paginator = Paginator(objects, objects_count)
	page = request.GET.get('page')

	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)

	return objects