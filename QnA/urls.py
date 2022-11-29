from django.contrib import admin
from django.urls import path
from QnA import views  
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('q_write/', views.q_write, name = 'q_write'),
    path('q_list/', views.q_list, name='q_list'),
    path('q_detail/<str:id>/', views.q_detail, name='q_detail'),
    path('q_edit/<str:id>/', views.q_edit, name='q_edit'),
    path('q_delete/<str:id>/', views.q_delete, name='q_delete'),
    path('q_like/<str:id>/', views.q_likes, name="q_likes"),
    #path('q_clip/<int:q_id>/', views.q_clip, name="q_clips"),
    path('q_search/',views.q_search, name = 'q_search'),
    path('<int:question_id>/answers/write/', views.answer_write, name='answer_write'),
    path('<int:question_id>/answers/<int:answer_id>/update/', views.answer_edit, name="answer_edit"),
    path('<int:question_id>/answers/<int:answer_id>/delete/', views.answer_delete, name="answer_delete"),
    ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)