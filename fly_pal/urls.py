from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^logout/?$', 'social_auth_app.views.logout'),
    url(r'^login/?$', 'social_auth_app.views.login'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', 'social_auth_app.views.main', name='main'),
    url(r'^flights/?$', 'flights.views.search', name='flight_search'),
    url(r'^book/?$', 'flights.views.book', name='flight_book'),
    url(r'^pals/?$', 'flights.views.pals', name='find_pals'),

    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
