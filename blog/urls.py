from django.urls import path

from rest_framework.authtoken import views as token_views

from . import views

urlpatterns = [
    path('blog', views.hello_world),
    path('blog/cbv', views.HelloWorld.as_view()),
    path('crypto', views.GetCryptoPrice.as_view()),
    path('articles', views.ArticleListView.as_view()),
    path('article/<int:pk>', views.ArticleDetailView.as_view()),
    path('articles/add', views.AddArticleView.as_view()),
    path('articles/update/<int:pk>', views.UpdateArticleView.as_view()),
    path('check', views.CheckToken.as_view()),
    path('login', token_views.obtain_auth_token),
]
