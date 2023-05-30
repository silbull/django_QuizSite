"""
URL configuration for demo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# path('demo/', include('demo.urls'))は，demoアプリケーションのURLをdemo_project/urls.pyに追加する
# path('admin/', admin.site.urls)は，管理サイトのURLをdemo_project/urls.pyに追加する
# path('', RedirectView.as_view(url='/demo/'))は，URLが空の場合にdemoアプリケーションのURLにリダイレクトする
urlpatterns = [
    path('demo/', include('demo.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/demo/')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
