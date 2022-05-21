from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'messages', views.MessageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    url(r'messages/(?P<pk>\d+)/comments/$', view=views.MessageViewSet.as_view({'get':'comments', 'post':'comments'})),
    url(r'messages/(?P<pk>\d+)/comments/(?P<comment>\d+)/$', view=views.MessageViewSet.as_view({'delete':'remove_comment'}))
]