from django.conf.urls.static import static
from django.urls import path

from core import settings
from .views import home, login, hub_digital, open_finance, instituicao_view, realiza_cambio, realiza_tranferencia

app_name = 'TecHub'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('hub/', hub_digital, name='hub'),
    path('openfinance/', open_finance, name='open_finance'),
    path('hub/banco/<pk>', instituicao_view, name='instituicao_view'),
    path('hub/banco/<pk>/cambio', realiza_cambio, name='realiza_cambio'),
    path('hub/banco/<pk>/transferencia', realiza_tranferencia, name='realiza_tranferencia'),
]
