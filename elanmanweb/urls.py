from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from extender.views import HomeView, hello
from runnow.views import AnswerWizard, FORMS


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^dev/', include('extender.urls', namespace='extend')),
    url(r'^start/$', AnswerWizard.as_view(FORMS)),
    url(r'^api/hello/$', hello, name='hello'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

