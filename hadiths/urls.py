# hadiths/urls.py

from django.urls import path
from .views import RandomBukhariHadithView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Hadiths API",
        default_version='v1',
        description="API for retrieving random Bukhari Hadiths",
        #terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="mohammedhafeeaz.mym@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('random-hadith/', RandomBukhariHadithView.as_view(), name='random_bukhari_hadith'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]