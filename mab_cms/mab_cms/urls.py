"""mab_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from mab_blog.views import view_post, view_category

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<slug>[^\.]+)/?',
        view_post,
        name='view_blog_post'),
    url(
        r'^(?P<slug>(artigo)|(noticia)|(charge))s/?',
        view_category,
        name='view_blog_category'),
    url(r'^', include('cms.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
