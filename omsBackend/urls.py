from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from questions import views as question_view
from user_info import views as user_view
from exams import views as exam_view

router = DefaultRouter()

router.register(r'user', user_view.UserViewSet)
router.register(r'choice', question_view.ChoiceQuestionViewSet)
router.register(r'blank', question_view.BlankQuestionViewSet)
router.register(r'subjective', question_view.SubjectiveQuestionViewSet)
router.register(r'exam', exam_view.ExamViewSet)
router.register(r'exam-question', exam_view.ExamQuestionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

# 注册媒体文件路由
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
