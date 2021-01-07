"""elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from students.views import student_detail
from api.views import UserViewSet
from courses.views import course_detail, course_list, course_add

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url('^', include('django.contrib.auth.urls'), namespace='auth'),

    url(r'^course_detail/(?P<pk>\d)/$', course_detail, name ='course_detail'),
    url(r'^course_add/$', course_add, name='course_add'),
    url(r'^student_detail/(?P<student_id>\d)/$', student_detail, name ='student_detail'),
    url(r'^api/', include(router.urls)),
    url(r'^$', course_list),
]
