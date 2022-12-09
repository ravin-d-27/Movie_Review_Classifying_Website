from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'predictor/home.html')

def pred(request):
    return render(request, 'predictor/preds.html')