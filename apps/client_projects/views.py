# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Client, Project
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    context = {
        'clients': Client.objects.all()
    }
    return render(request, "client_projects/index.html", context)

def show_add_client(request):
    return render(request, "client_projects/add_client.html")

def add_client(request):
    if request.method == "POST":
        errors = Client.objects.client_valid(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)
                return redirect("show_add_client")
        else:
            Client.objects.create(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], notes=request.POST['notes'])
            return redirect("index")

def show_client(request, client_id):
    context = {
        "client": Client.objects.get(pk=client_id)
    }
    return render(request, "client_projects/show_client.html", context)

def show_add_project(request, client_id):
    context = {
        "client": Client.objects.get(pk=client_id)
    }
    return render(request, "client_projects/add_project.html", context)

def add_project(request, client_id):
    if request.method == "POST":
        errors = Project.objects.project_valid(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)
                return redirect(reverse("show_add_project", kwargs={'client_id':client_id}))
        else:
            client = Client.objects.get(pk=client_id)
            Project.objects.create(client=client, name=request.POST['name'], notes=request.POST['notes'])
            return redirect(reverse('show_client', kwargs={'client_id': client_id}))

def show_project(request, client_id, project_id):
    context = {
        'client': Client.objects.get(pk=client_id),
        'project': Project.objects.get(pk=project_id)
    }
    return render(request, "client_projects/show_project.html", context)
