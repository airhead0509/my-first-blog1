from django.conf.urls import urls
from . import views

urlpatterns = [
	url(r'^$', view.post_list, name 'post_list')
]