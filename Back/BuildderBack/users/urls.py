from django.urls import path

from .views import(
    user_login,
    user_logout,
    user_list,
    user_create,
    user_detail,
    user_edit,
    user_delete,
)

app_name = 'users'

urlpatterns = [
    path('',user_login,name='login'),
    path('logout',user_logout,name='logout'),
    path('list',user_list,name='list'),
    path('create',user_create,name="user_create"),
    path('<int:user_id>',user_detail,name="detail"),
    path('<int:user_id>/edit',user_edit,name="edit"),
    path('<int:user_id>/delete',user_delete,name="delete")
]