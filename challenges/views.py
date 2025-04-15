from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'Home.html')

def beginner_task(request):
    if request.method == 'POST':
        # Add code validation logic here
        pass
    return render(request, 'beginner-taskpage.html')