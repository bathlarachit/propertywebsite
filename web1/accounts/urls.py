from django.urls import path
from django.contrib.auth import views as auth_view
from accounts import views
from django.conf import settings
from django.conf.urls import static
#####
app_name = 'accounts'
urlpatterns= [
    path('login/',auth_view.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('about/',views.About.as_view(),name ='about'),
    path('buy/',views.LandList.as_view(),name = 'buy'),
    path('buy/<int:pk>/',views.LandDetail.as_view(),name='detail'),
    path('sell/',views.SellList.as_view(),name='sell'),
    path('sellpost/',views.LandPost.as_view(),name='sellpost'),
    path('sell/<int:pk>/',views.sellDetail.as_view(),name='selldetail'),
    path('requests/',views.SellRequest.as_view(),name='requests'),
    path('requests/<int:pk>/',views.sellDetail.as_view(),name='requestsdetail'),
    path('delete/<int:pk>/',views.PostDelete.as_view(),name='delete'),
    path('buydelete/<int:pk>/',views.BuyDelete.as_view(),name='buydelete'),
    path('addbuy/',views.BuyCreate.as_view(),name = 'addbuy')

]
