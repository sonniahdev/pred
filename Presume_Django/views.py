from django.shortcuts import render



def indexpage(request):
    return render(request, 'index.html')

def registerpage(request):
    return render(request, 'register.html')

def loginpage(request):
    return render(request, 'login.html')


def homepage(request):
    return render(request, 'index.html')



def aboutpage(request):
    return render(request, 'about.html')


def doctorspage(request):
    return render(request, 'doctors.html')

def protectpage(request):
    return render(request, 'protect.html')

def newspage(request):
    return render(request, 'news.html')




