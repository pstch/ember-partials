from django.conf.urls import url, include
from rest_framework import routers

from .views import (
    CurrentUserView,
    TestObjViewSet, GroupViewSet, DocumentViewSet
)

router = routers.DefaultRouter()
router.register(r'testobjs', TestObjViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'documents', DocumentViewSet)


urlpatterns = [
    url(r'^auth/users/me', CurrentUserView.as_view()),
    url(r'^auth/token',
        'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^', include(router.urls)),

]
