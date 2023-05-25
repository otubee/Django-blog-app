from django.urls import path 
from . import views
from accounts.views import (
    login_view, logout_view, register_view
)
    



urlpatterns=[
    path('', views.home_view),
    path('core/', views.search_view),
    path('core/create/', views.create_view),
    path('core/<int:id>/',views.link_view ),
    path('accounts/login/', login_view),
    path('accounts/logout/', logout_view),
    path('accounts/register/', register_view),
]