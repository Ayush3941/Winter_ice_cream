from django.shortcuts import render,HttpResponse
from home.models import Contact
import datetime
from django.contrib import messages
# Create your views here.
def index(request):
	var = {"alpha":1}
	return render(request,"index.html",var)
def about(request):
	return render(request,"about.html")
def services(request):
	return render(request,"services.html")
def contact(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("e-mail")
		phone = request.POST.get("phone")
		desc = request.POST.get("desc")
		x = Contact(name =name,email = email,phone = phone,desc = desc,date = datetime.datetime.today())
		x.save()
		messages.success(request,"Your Query is Submitted")
	return render(request,"contact.html")
