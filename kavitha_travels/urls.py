from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # Django Admin
    path('admin/', admin.site.urls),

    # Main Website
    path('', include('website.urls')),

    # Travel ERP
    path('erp/', include('travel_erp.urls')),

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )