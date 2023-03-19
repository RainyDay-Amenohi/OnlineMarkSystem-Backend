from django.contrib import admin
from questions.models import SingleChoice,ChoiceQuestion

# Register your models here.
admin.site.register(SingleChoice)
admin.site.register(ChoiceQuestion)
