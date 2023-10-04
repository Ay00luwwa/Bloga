from django.urls import path
from .views import PostListView, PostCreateView, PostDeleteView, PostUpdateView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import get_paginated_posts



urlpatterns = [
    path('', views.intro, name='intro'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('post/new', PostCreateView.as_view(), name ='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('get_paginated_posts/', get_paginated_posts, name='get_paginated_posts'), 
    path('search/', views.search_view, name='search-view'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



