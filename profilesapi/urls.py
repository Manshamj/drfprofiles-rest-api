from django.urls import path,include
from profilesapi import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello_viewset')
"""Note: base_name is use to retrive the URL in our router """


urlpatterns = [
    path('', include(router.urls)),
    path('hello-view/', views.HelloApiVIew.as_view()),
]
