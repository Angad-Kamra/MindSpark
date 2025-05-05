from django.shortcuts import render

def Amainpage(request):
    return render(request,'index.html')
def Bmainpage(request):
    return render(request,'index2.html')
#Adventure
def Game1(request):
    return render(request,'game1.html')
def Game2(request):
    return render(request,'game2.html')
def Game3(request):
    return render(request,'game3.html')
def Game4(request):
    return render(request,'game4.html')
#Arcade
def GameA1(request):
    return render(request,'gameA1.html')
def GameA2(request):
    return render(request,'gameA2.html')