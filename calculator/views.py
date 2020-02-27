from django.shortcuts import render

# Create your views here.
def calculator_POST(request):
    if request.POST:
        
    return render(request,'calculator_POST.html')
def calculator_GET(request):
    return render(request,'calculator_GET.html')
def about(request):
    return render(request,'about.html')
