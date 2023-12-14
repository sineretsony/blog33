from django.urls import path
from . import views
# добавлено 44
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:id>', views.post, name='post'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('category/<str:name>', views.category, name='category'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    # добавлено 44
    path('login', LoginView.as_view(), name='blog_login'),
    path('logout', LogoutView.as_view(), name='blog_logout'),
    path('registration_user', views.registration_user, name='registration_user'),
    path('profile', views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),

]
