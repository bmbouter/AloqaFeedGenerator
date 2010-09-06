from django.conf.urls.defaults import *

urlpatterns = patterns('AloqaFeedGenerator',
    (r'^feed$', 'views.viewFeed'),
)
