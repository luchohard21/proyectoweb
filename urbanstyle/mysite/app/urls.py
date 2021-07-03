from django.urls import path, admin
from django.conf.urls import url
from . views import index, quienesomos, servicios, reservatuhora, contactanos, dejanostuopinion



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('quienesomos/', quienesomos, name="quienesomos"),
    path('servicios/', servicios, name="servicios"),
    path('reservatuhora/', reservatuhora, name="reservatuhora"),
    path('contactanos/', contactanos, name="contactanos"),
    path('dejanostuopinion/', dejanostuopinion, name="dejanostuopinion"),




]