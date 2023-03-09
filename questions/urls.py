from django.urls import path
from questions import views
app_name = 'questions'

urlpatterns = [
    path('', views.questions_list, name='list'),
]