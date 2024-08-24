from django.urls import path, re_path, include
from .views import MainPageView, SlugPageView, NamedPageView


urlpatterns = [

    path('', MainPageView.as_view(), name='main'),
    path('vegetables/', NamedPageView.as_view(), name='vegs'),
    path('fruits/', NamedPageView.as_view(), name='fruits'),
    path('spices/', NamedPageView.as_view(), name='spices'),

    path('<slug:prod_name>/', SlugPageView.as_view(), name='slugurl'),
    path('<path:page_name>/', SlugPageView.as_view(), name='pathurl'),

]
