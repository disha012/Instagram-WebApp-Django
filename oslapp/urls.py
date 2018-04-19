from django.conf.urls import url
from django.contrib.auth import views as auth_views
from oslapp import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'},
        name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent,
        name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
    url(r'^uploads/form/$', core_views.model_form_upload, name='model_form_upload'),
    # url(r'^(?P<id>\w+)/$', core_views.profileview, name='profileview')
    # path('<slug:id>/', core_views.profileview),
    # url(r'^profile_view/(?P<username>\d+)/$', core_views.profileview,
    #    name='profile_view'),
    url(r'^profile_view/(?P<username>[\w.@+-]+)/$', core_views.profileview, name='profile_view'),
    url(r'^profile_view/(?P<username>[\w.@+-]+)/follow/$', core_views.follow_user, name='follow'),
    url(r'^profile_view/(?P<username>[\w.@+-]+)/upvote/(?P<photo_id>[0-9]+)/$', core_views.upvote, name='upvote'),
    url(r'^profile_view/(?P<username>[\w.@+-]+)/listofupvotes/(?P<photo_id>[0-9]+)/$', core_views.listofupvotes, name='listofupvotes'),
    url(r'^profile_view/(?P<username>[\w.@+-]+)/followers$', core_views.follower, name='followers'),
    url(r'^profile_view/(?P<username>[\w.@+-]+)/following$', core_views.following, name='following'),
    url(r'^profile_view/(?P<username>[\w.@+-]+)/deletephoto/(?P<photo_id>[0-9]+)/$', core_views.deletephoto, name='deletephoto'),
    url(r'^search$', core_views.search, name='search'),
]
