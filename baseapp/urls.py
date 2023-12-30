from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import productapp.urls as productapp_urls
import userapp.urls as userapp_urls
import sellerapp.urls as sellerapp_urls
import cartapp.urls as cartapp_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(productapp_urls.urlpatterns)),
    path('user/', include(userapp_urls.urlpatterns)),
    path('seller/', include(sellerapp_urls.urlpatterns)),
    path('cart/', include(cartapp_urls))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
