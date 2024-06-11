"""
URL configuration for businessinteligence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from business_intelligence.views import index, servicios_barra, servicios_pastel, ganancias_lineal

from business_intelligence.views.index_view import index
from business_intelligence.views.servicios_views import servicios_barra
from business_intelligence.views.maintenance_view import maintenance_pastel
from business_intelligence.views.ganancia_view import ganancias_lineal

from business_intelligence.views.get_service_name import get_service_names_view
from business_intelligence.views.get_brand_vehicle import get_vehicle_brands_view
from business_intelligence.views.get_vehicle_year import get_vehicle_years_view
from business_intelligence.views.get_year_maintenance import get_maintenance_years_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    
    path('kpi/servicios-adicionales/', servicios_barra, name='servicios_adicionales'),
    path('kpi/vehiculos-mantenimiento/', maintenance_pastel, name='vehiculos-mantenimiento'),
    path('kpi/ganancias-totales/', ganancias_lineal, name='ganancias-totales'),

    path('get-service-names/', get_service_names_view, name='get_service_names'),
    path('get-brand-vehicles/', get_vehicle_brands_view, name='get_service_names'),
    path('get-year-vehicles/', get_vehicle_years_view, name='get_year_vehicles'),
    path('get-year-maintenance/', get_maintenance_years_view, name='get_year_maintenance'),
]
