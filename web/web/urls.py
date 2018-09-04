from django.conf.urls import url, include
from django.contrib import admin
from users_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include(router.urls)),

]
