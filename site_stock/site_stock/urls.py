from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('store.urls')),
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('captcha/', include('captcha.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
