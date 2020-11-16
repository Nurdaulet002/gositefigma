from django.urls import path
from . import views
app_name = 'management'

urlpatterns = [
    path('', views.InformationView.as_view(), name='information_page'),
    path('mysite', views.MySiteListView.as_view(), name='mysite_page'),
    path('site/list', views.SiteListView.as_view(), name='site_list_page'),
    path('site/list/<int:category>', views.SiteListView.as_view(), name='site_list_page'),
    path('user/site/create/<int:site>', views.UserSiteCreateView.as_view(), name='user_site_page'),
    path('user/registration', views.UserRegistrationView.as_view(), name='user_registration_page'),
]