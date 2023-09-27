from django.conf.urls.static import static
from django.urls import path

from core import settings
from .views import home, login, hub_digital, barra_navegacao, open_finance

app_name = 'TecHub'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('hub/', hub_digital, name='hub'),
    # path('navegacao/', barra_navegacao, name='nav'),
    path('openfinance/', open_finance, name='open_finance')
    # path('cadastro', views.cadastro, name='cadastro'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)