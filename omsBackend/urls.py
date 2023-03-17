from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from questions import views

router = DefaultRouter()
router.register(r'singleChoice', views.SingleChoiceViewSet)
router.register(r'choice-question', views.ChoiceQuestionViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    # path('questions/', include('questions.urls', namespace='questions')),
]
