"""elanmanweb URL Configuration

968021183096-rgses4fccrdatsg6trn05c5d85fq6gti.apps.googleusercontent.com
sv_VC0oaaZJYfKIfMNvwSfnN

Dev
b6fbea6393bc3109f8b3
84856266d8b821180e05a8725d5a859b36a4f4cc

Prod
04e4857f84b31717609a
55716c16ef9db443f2b57fd7353e45009c72549d


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
from django.conf import settings
from django.contrib import admin
from extender.views import HomeView
from runnow.views import AnswerWizard, FORMS

# from myprofile.urls import
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^start/$', AnswerWizard.as_view(FORMS)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
