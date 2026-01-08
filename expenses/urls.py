from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, expense_summary
from .reports import export_excel

routers = DefaultRouter()
routers.register(r'expenses',ExpenseViewSet)

urlpatterns = [
    path('',include(routers.urls)),
    path('expenses/summary/',expense_summary),
    path('expenses/export/excel/', export_excel),
]
