from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):


	title = "Welcome"


	form = SignUpForm(request.POST or None)
	context = {

		"title": title,
		"abc": 123,
		"form": form
	}

	if request.method == "POST":
		print (request.POST)

	if request.user.is_authenticated():
		title = "Current User : %s  " %(request.user)



	if form.is_valid():
		instance = form.save()
		print (instance)
		context = {

			"title" :"Thank you",
			"abc" : 123

		}

	return render(request,"home.html", context)





def accueil(request):
	print("fffffff")
	print(type(request))
	print(request.POST.get("full_name"))
	return render(request,"accueil.html",None)