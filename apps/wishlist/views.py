# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..login.models import User
from .models import Item
from django.contrib import messages


# Create your views here.


def index(request):
    context = {
        "message" : "test shit",
    }
    return render(request, "index.html", context)

def dashboard(request):
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        "user" : current_user,
        "wish_list_items" : current_user.item_set.all(),
        # https://stackoverflow.com/questions/35012942/related-field-got-invalid-lookup-icontains/35013091
        "non_wish_items" : Item.objects.exclude(wished_by__name__icontains = current_user.name)
    }
    return render(request, "dashboard.html", context)

def create(request):
    return render(request, "create.html")

def add(request):
    added_by = User.objects.get(id=request.session['user_id'])
    result = Item.objects.validate_item(request.POST, added_by)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/wish_items/create')
    return redirect('/dashboard')

def display(request, item_id):
    current_item = Item.objects.get(id = item_id)
    context = {
        "people" : Item.objects.get(id = item_id).wished_by.all(),
        "item" : current_item
    }
    return render(request, "display.html", context)

def item_add(request, item_id):
    current_user = User.objects.get(id=request.session['user_id'])
    current_item = Item.objects.get(id = item_id)
    current_item.wished_by.add(current_user)
    return redirect('/dashboard')

   

def remove(request, item_id):
    current_user = User.objects.get(id=request.session['user_id'])
    current_item = Item.objects.get(id = item_id)
    current_item.wished_by.remove(current_user)
    return redirect('/dashboard')

def delete(request, item_id): 
    current_item = Item.objects.get(id = item_id)
    current_item.delete()
    return redirect('/dashboard')