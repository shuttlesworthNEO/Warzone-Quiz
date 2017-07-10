# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import SignUpForm, LoginForm
from django.shortcuts import render, redirect
from models import UserModel, SessionToken
from django.contrib.auth.hashers import make_password, check_password
from datetime import timedelta
from django.utils import timezone

# Create your views here.
def signup_view(request):
    dict = {}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print request.body
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if UserModel.objects.filter(username=username):
                dict['message'] = 'Username already exists!'
            else:
                user = UserModel(name=name, password=make_password(password), email=email, username=username)
                user.save()
                return redirect('/login/')
    else:
        form = SignUpForm()

    dict['form'] = form
    return render(request, 'index.html', dict)


def login_view(request):
    dict = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = UserModel.objects.filter(username=username).first()

            if user:
                # Check for the password
                print make_password(password), user.password
                if not check_password(password, user.password):
                    dict['message'] = 'Incorrect Password! Please try again!'
                else:
                    token = SessionToken(user=user)
                    token.create_token()
                    token.save()
                    response = redirect('/quiz/')
                    response.set_cookie(key='session_token', value=token.session_token)
                    return response
    else:
        form = LoginForm()

    dict['form'] = form
    return render(request, 'login.html', dict)

#For validating the session
def check_validation(request):
    if request.COOKIES.get('session_token'):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            time_to_live = session.created_on + timedelta(days=1)
            if time_to_live > timezone.now():
                return session.user
    else:
        return None