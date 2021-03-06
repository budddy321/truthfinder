from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url(r'^_ah/warmup$', 'djangoappengine.views.warmup'),

    url(r'^$', 'main.views.home', name='home'),
    url(r'^orphans/$', 'main.views.orphans', name='orphans'),
    url(r'^flagged/$', 'main.views.flagged', name='flagged'),
    url(r'^about/$', 'main.views.about', name='about'),

    url(r'^search/$', direct_to_template, {'template': 'search.html'}, name='search'),

    url(r'^cron/changelist/$', 'main.views.cron_changelist', name='cron_changelist'),

    url(r'^ajax/rel/(\d+)/$', 'main.views.ajax_rel', name='ajax_rel'),
    url(r'^ajax/rel/(\d+)/json/$', 'main.views.ajax_rel_json', name='ajax_rel_json'),
    url(r'^ajax/node/(\d+)/$', 'main.views.ajax_node', name='ajax_node'),
    url(r'^ajax/node/(\d+)/json/$', 'main.views.ajax_node_json', name='ajax_node_json'),
    url(r'^ajax/search/$', 'main.views.ajax_search', name='ajax_search'),

    url(r'^changelist/$', 'main.views.changelist', name='changelist'),
    url(r'^add/$', 'main.views.add_node', name='add'),
    url(r'^unpin/(\d+)/$', 'main.views.unpin_node', name='unpin'),
    url(r'^invert/(\d+)/$', 'main.views.invert', name='invert'),
    url(r'^node/(\d+)/$', 'main.views.node', name='node'),
    url(r'^node/(\d+)/edit/$', 'main.views.edit_node', name='edit'),
    url(r'^node/(\d+)/delete/$', 'main.views.delete_node', name='delete'),
    url(r'^node/(\d+)/unpin/(\d+)/(\d+)/$', 'main.views.unpin_node', name='unpin'),
    url(r'^node/(\d+)/pin/$', 'main.views.pin_node', name='pin'),
    url(r'^node/(\d+)/pin/(\d+)/$', 'main.views.pin_existing', name='pin_existing'),
    url(r'^node/(\d+)/pro/$', 'main.views.add_pro', name='pro'),
    url(r'^node/(\d+)/con/$', 'main.views.add_con', name='con'),
    url(r'^node/(\d+)/premise/$', 'main.views.add_premise', name='premise'),

)
