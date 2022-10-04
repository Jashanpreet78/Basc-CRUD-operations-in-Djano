from django.urls import path
from .views import Home,Add_User,Delete_User,EditUser
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('add-user/',Add_User.as_view(),name='add-user'),
    path('delete-user/',Delete_User.as_view(),name='delete-user'),
    path('edit-user/<int:id>/',EditUser.as_view(),name='edit-user'),
]
