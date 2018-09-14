from django.contrib import admin

# Register your models here.
#from newsletter.models import SignUp   It is not a good practice to put newsletter because we are inside that application
from .models import SignUp
from .forms import SignUpForm


class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__","timestamp","updated"]
	#class Meta:
	#	model = SignUp

	form = SignUpForm

admin.site.register(SignUp,SignUpAdmin)
#admin.site.register(SignUp)