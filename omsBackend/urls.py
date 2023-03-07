from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# 序列化器是用来定义API的表示形式。
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets定义视图的行为。
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 路由器提供一个简单自动的方法来决定URL的配置。
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# 通过URL自动路由来给我们的API布局。
# 此外，我们还要把登录的URL包含进来。
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]