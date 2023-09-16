from django.urls import path

from post import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:post_id>/comment/', views.CommentList.as_view()),
    path('<int:post_id>/comment/<int:pk>', views.CommentDetail.as_view()),
]