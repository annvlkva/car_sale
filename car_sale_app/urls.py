from django.conf.urls import url
from django.urls import path

from car_sale_app import views

from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view),
    path('openapi', get_schema_view(
            title="Car sale",
            description=""
        ), name='openapi-schema'),
    path('cars/', views.CarView.as_view()),
    path('cars/<int:id>/', views.CarIdView.as_view()),
    path('dealers/', views.DealerView.as_view()),
    path('dealers/<int:id>/', views.DealerIdView.as_view()),
]