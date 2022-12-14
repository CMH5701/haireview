from django.contrib import admin
from django.urls import path
from free import views  

urlpatterns = [
    path('f_write/', views.f_write, name = 'f_write'),
    path('f_list/', views.f_list, name='f_list'),
    path('f_detail/<str:id>/', views.f_detail, name='f_detail'),
    path('f_edit/<str:id>/', views.f_edit, name='f_edit'),
    path('f_delete/<str:id>/', views.f_delete, name='f_delete'),
    path('f_like/<str:id>/', views.f_likes, name="f_likes"),
    #path('p_clicks/<int:p_id>/', views.p_clicks, name="p_clicks"),
    path('f_search/', views.f_search, name='f_search'),
    path('<int:free_id>/p_comment/write/', views.p_commentwrite, name='p_commentwrite'),
    path('<int:free_id>/p_comment/<int:p_comment_id>/update/', views.p_commentedit, name="p_commentedit"),
    path('<int:free_id>/p_comment/<int:p_comment_id>/delete/', views.p_commentdelete, name="p_commentdelete"),
]