from django.urls import include, path

from api.views import filecreate

urlpatterns = [
    path('api/v1/filecreate/', filecreate),
    path('auth/', include('djoser.urls.authtoken')),
]
