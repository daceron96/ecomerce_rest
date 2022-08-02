from django.urls import path
from products.api.views.general_views import IndicatorListAPIView, MeasuerUnitListAPIView, CategoryProductListAPIView

urlpatterns = [
    path('measure_unit/',MeasuerUnitListAPIView.as_view(), name='measure_unit'),
    path('indicator/',IndicatorListAPIView.as_view(), name='indicator'),
    path('category_product/',CategoryProductListAPIView.as_view(), name='category_product'),
]
