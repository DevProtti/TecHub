from django.conf.urls.static import static
from django.urls import path

from core import settings
from .views import home, login, hub_digital

app_name = 'TecHub'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    # path('cadastro', views.cadastro, name='cadastro'),
    path('hub/', hub_digital, name='hub')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)