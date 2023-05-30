from django.urls import path
from . import views

# 名前空間を追加することで，複数アプリケーションのURLパターンが重複した場合に区別できる
app_name = 'demo'

# path('', views.IndexView.as_view(), name='index')は，demoアプリケーションのURLをdemo/urls.pyに追加する

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
