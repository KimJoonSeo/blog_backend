from django.urls import path

from post import views

app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('<int:post_id>/comment/', views.CommentList.as_view(), name='comment_list'),
    path('<int:post_id>/comment/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
]