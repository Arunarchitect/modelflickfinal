from django.urls import path, include
from .views import Index, DetailArticleView, LikeArticle, Featured, DeleteArticleView, AddPostView, EditPostView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>/', DetailArticleView.as_view(), name= 'detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='featured'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
]
