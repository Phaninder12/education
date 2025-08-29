from django.shortcuts import render,redirect
from educationapp.models import Parent,Contact
from educationapp.forms import ParentForm,ContactForm
# Create your views here.

def homeview(request):
	return render(request,'educationapp/home.html')


def contactview(request):
    form1 = ContactForm()
    if request.method == "POST":
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/contact')
    return render(request, 'educationapp/contact.html', {'d': form1})

def aboutview(request):
	return render(request,'educationapp/about.html')

def photoview(request):
	return render(request,'educationapp/Photos.html')

def videosview(request):
	return render(request,'educationapp/Videos.html')


def newsview(request):
	return render(request,'educationapp/LatestNews.html')

def Regview(request):
    form = ParentForm()
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/adminpage')
    return render(request, 'educationapp/ParentReg.html', {'f': form})

def classxview(request):
	return render(request,'educationapp/classX.html')

def classixview(request):
	return render(request,'educationapp/classIX.html')

def classviiiview(request):
	return render(request,'educationapp/classVIII.html')

def adminpageview(request):
    data = Parent.objects.all()
    data1 = Contact.objects.all()
    return render(request,'educationapp/adminpage.html',{'e':data,'f':data1})







