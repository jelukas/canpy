from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'sign.views.home', name='home'),
    url(r'^signing$', 'sign.views.signing', name='signing'),
    url(r'^list_signs', 'sign.views.list_signs', name='list_signs'),
    url(r'^save_sign', 'sign.views.save_sign', name='save_sign'),
)
