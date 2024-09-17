"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static

from . import settings
import catalog.views

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("catalog/", catalog.views.index),
        path("catalog/new_user/", catalog.views.save_user_post),
        path("catalog_items/", catalog.views.paginated_items_view),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(
        settings.IMAGES_URL,
        view=catalog.views.serve_images,
        document_root=settings.IMAGES_ROOT,
    )
)
