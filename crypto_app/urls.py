from django.urls import path
from crypto_app.views import homePage, appDetail, key_page, successfully

urlpatterns = [
    path('', view=homePage, name='homePage'),
    path('app/<int:app_id>/', view=appDetail, name='app_detail'),
    path('app/final/<int:app_id>/', view=key_page, name='key_page'),
    path('app/final/<int:app_id>/successful/', view=successfully, name='success'),
]