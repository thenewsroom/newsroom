from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^main', views.home,name='home'),
    url(r'^c/(?P<category_name>\w+)/$', views.category_content, name='category_content'),
    url(r'^subcategory/(?P<subcategory_name>\w+)/$', views.subcategory_content, name='subcategory_content'),
    url(r'^view/(?P<story_id>\d+)/$', views.story, name='story'),
]