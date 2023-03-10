from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from questions import views

router = DefaultRouter()
router.register(r'singleChoice', views.SingleChoiceViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls))
    # path('questions/', include('questions.urls', namespace='questions')),
]
