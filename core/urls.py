from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('account/', include('account.urls', namespace='account')),
    path('about/', include('about.urls', namespace='aboutus')),
    path('contact/', include('contact.urls', namespace='contactus')),
    path('certificates/', include('certificates.urls', namespace='certificates')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('payment/', include('payment.urls', namespace='payment')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
