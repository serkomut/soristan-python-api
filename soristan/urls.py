from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from soristan import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     url(r'^', include(router.urls))
]