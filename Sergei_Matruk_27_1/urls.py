from django.contrib import admin
from django.urls import path
from Sergei_Matruk_27_1 import settings
from posts.views import main_view, products_view, product_detail_view
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('products/<int:id>', product_detail_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)