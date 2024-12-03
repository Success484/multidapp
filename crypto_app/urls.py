from django.urls import path
from crypto_app.views import homePage, appDetail

urlpatterns = [
    path('', view=homePage, name='homePage'),
    path('app/<int:app_id>/', view=appDetail, name='app_detail'),
]