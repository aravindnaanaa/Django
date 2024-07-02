from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
Name = ["Naa", "Deepi", "Mark"]


class NewTaskForm(forms.Form):
    task = forms.CharField(label="newtask")
    priority = forms.IntegerField(label="priority", min_value=1, max_value=10)

def index(request):

    if "tasks" not in request.session:
        request.session["tasks"] = []


    return render(request, "tasks/index.html", {
       # "Name": Name
       "Name":request.session["tasks"]
    })



def add(request):
    if request.method == "POST":
        formm = NewTaskForm(request.POST)
        if formm.is_valid():
            task = formm.cleaned_data["task"]
            #Name.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                "form": formm
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })