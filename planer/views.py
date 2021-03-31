from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm

def post_list(request):
    return render(request, 'planer/post_list.html', {})

from django.shortcuts import render
from .forms import UserForm

def index(request):
    firstname=''
    lastname=''
    emailvalue=''
    submitbutton = ''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            firstname= form.get("first_name")
            lastname= form.get("last_name")
            emailvalue= form.get("email")
            submitbutton = form.get("submittion")

    context= {'form': form, 'firstname': firstname, 
            'lastname':lastname, 'submitbutton': submitbutton,
            'emailvalue':emailvalue}
    print(context)
    print("HEY  ")
    return render(request, 'UserInfo/index.html', context)
