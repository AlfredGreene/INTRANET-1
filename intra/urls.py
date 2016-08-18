from django.conf.urls import include, url
from django.contrib import admin

from local_apps.frontend import views as front_views
from local_apps.profiles import auth as local_auth

urlpatterns = [
    url(r'^$', front_views.home, name="Home"),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('local_apps.dashboard.urls')),
    url(r'^inventario/', include('local_apps.inventory.urls')),
    url(r'^reportes/', include('local_apps.reports.urls')),
    url(r'^tickets/', include('local_apps.tickets.urls')),

    # Auth
    url(r'^entrar/', local_auth.login, name = 'Login'),
    url(r'^salir/', local_auth.logout, name = 'Logout'),
    url(r'^registro/', local_auth.register, name = 'Register'),
]
