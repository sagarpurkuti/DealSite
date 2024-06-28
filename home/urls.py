from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from home import views
from .views import edit_deal, delete_deal
from django.conf import settings
from django.conf.urls.static import static




admin.site.site_header = 'DealSite Django Admin '                  # default: "Django Administration"
admin.site.index_title = ' DealSite Django Admin'                  # default: "Site administration"
admin.site.site_title = 'DealSite Django adminsitration'           # default: "Django site admin"

# app_name = "home"


urlpatterns = [
    path('', views.index, name="home"),
    # path('dashboard', views.dashboard, name="sellerDashboard"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path("contact", views.contact, name='contact'),
    path("breadfruit/<str:username>/",views.breadfruit, name='breadfruit'),
    path("daraz/<str:username>/",views.daraz,name='daraz'),
    path("itti/<str:username>/",views.itti,name='itti'),
    path("esewa/<str:username>/",views.esewa,name='esewa'),
    path("services", views.services, name='services'),
    path('banner',views.banner,name='banner'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addDeal',views.addDeal,name='addDeal'),
    path('Dashboard/edit_deal/<int:deal_id>/',views.edit_deal, name='edit_deal'),
    path('Dashboard/delete/<int:deal_id>/',views.delete_deal, name='delete_deal'),
    path('delete_banner/<int:banner_id>/', views.delete_banner, name='delete_banner'),
    path('brand/<str:name>/', views.delete_banner, name='brand'),

]

