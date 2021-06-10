from django.shortcuts import render

# Create your views here.
def russianWelcomePage(request):
	return render(request, 'welcomerus.html')