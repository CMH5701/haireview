"""haireview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import review.views
import main.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name = 'main'),
    path('hashtag', main.views.hashtag, name = 'hashtag'),
    path('m_search/',main.views.m_search, name="m_search"),
    path('h_list', main.views.h_list, name='h_list'),
    path('r_write/', review.views.r_write, name = 'r_write'),
    path('r_list/', review.views.r_list, name='r_list'),
    path('r_detail/<str:id>/', review.views.r_detail, name='r_detail'),
    path('r_edit/<str:id>/', review.views.r_edit, name='r_edit'),
    path('r_delete/<str:id>/', review.views.r_delete, name='r_delete'),
    path('r_like/<str:id>/', review.views.r_likes, name="r_likes"),
    path('r_search/', review.views.r_search, name='r_search'),
    path('<int:review_id>/r_comment/write/', review.views.r_commentwrite, name='r_commentwrite'),
    path('<int:review_id>/r_comment/<int:r_comment_id>/update/', review.views.r_commentedit, name="r_commentedit"),
    path('<int:review_id>/r_comment/<int:r_comment_id>/delete/', review.views.r_commentdelete, name="r_commentdelete"),
    
    path('', include('account.urls')),
    path('', include('free.urls')),
    path('', include('QnA.urls')),
    path('', include('bookmark.urls')),
	path('summernote/', include('django_summernote.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

