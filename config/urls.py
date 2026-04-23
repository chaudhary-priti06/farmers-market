from django.contrib import admin
from django.urls import path, include
from market import views
from django.contrib.auth import views as auth_views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('market.urls')),
    path('signup/', views.signup, name='signup'),
]

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('orders/', views.order_history, name='orders'),

]
