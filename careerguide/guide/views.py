from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')
def choose(request):
    return render(request,'choose.html')
def explore(request):
    return render(request,'explore.html')
def test(request):
    return render(request,'test.html')


def result(request):
    if request.method=="POST":
        s=[]
        s.append(request.POST.getlist("fruits"))
        print(s)
    return render(request,'homepage.html')
