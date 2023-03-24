from django.contrib import admin
from questions.models import ChoiceQuestion, SubjectiveQuestion, BlankQuestion

# Register your models here.
# admin.site.register(SingleChoice)
admin.site.register(ChoiceQuestion)
admin.site.register(SubjectiveQuestion)
admin.site.register(BlankQuestion)
