from django.conf.urls import url
from Registration import views
from Registration import api_views as av

app_name = 'URLROUTE'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^api_list/$', views.api_list, name='api_list'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_delete/$', views.user_delete, name='delete_usr'),
    url(r'^user_update/$', views.user_update_password, name='update_pass'),
    url(r'^data/$', av.UserDataShowAPI.as_view(), name='all_api_data'),
    url(r'^new_user/$', av.RegisterNewUserAPIView.as_view(), name='new_user'),
    url(r'^(?P<username>[\w-]+)/all/$', av.UserDataAll.as_view(), name='all_api'),
    url(r'^(?P<username>[\w-]+)/update/$', av.UpdateUserPassword.as_view(), name='update_pass'),

]
