from django.conf.urls.static import static
from django.urls import path

from core import settings
from .views import home, login, hub_digital, barra_navegacao, open_finance

app_name = 'TecHub'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('hub/', hub_digital, name='hub'),
    path('openfinance/', open_finance, name='open_finance')
]
