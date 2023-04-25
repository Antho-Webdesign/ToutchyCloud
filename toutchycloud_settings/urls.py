from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from toutchycloud_settings import settings
from toutchycloud_settings.views import home

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('', include('gstPhotos.urls')),
    path('', include('gstDocuments.urls')),
    path('', include('accounts.urls')),
    path('', include('gstRappels.urls')),
    path('', include('gstTasks.urls')),
    path('gestion/contact/', include('gstContact.urls')),
    path('gestion-passwords/', include('gstPasswords.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
