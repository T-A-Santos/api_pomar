from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'especies', views.EspeciesViewSet)
router.register(r'arvores', views.ArvoresViewSet)
router.register(r'grupoArvores', views.GrupoArvoresViewSet)
router.register(r'colheita', views.ColheitaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]