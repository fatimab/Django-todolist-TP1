"""todomanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from todo.views import TaskListView
from todo.views import TaskRetrieveView
from todo.views import TaskCreateView
from todo.views import TaskUpdateView
from todo.views import TaskDeleteView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TaskListView.as_view(), name='task-list'),
    url(r'^(?P<pk>\d+)/$', TaskRetrieveView.as_view(), name='retrieve'),
    url(r'create/', TaskCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/', TaskUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/', TaskDeleteView.as_view(), name='delete'),
]
