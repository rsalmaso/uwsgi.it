from django.conf.urls import patterns

urlpatterns = patterns('uwsgi_it_api.views',
    (r'^containers/$', 'containers'),
    (r'^containers/(\d+)$', 'container'),
    (r'^containers/(\d+)\.ini$', 'container_ini'),
    (r'^me/$', 'me'),
    (r'^distros/$', 'distros'),
    (r'^domains/$', 'domains'),
    (r'^domains/rsa/$', 'domains_rsa'),
    (r'^domains/(\d+)$', 'domain'),
)
