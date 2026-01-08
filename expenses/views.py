from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = 'expense_id'
    
@api_view(['GET'])
def expense_summary(request):
    summary = Expense.objects.values('category').annotate(
        total = Sum('amount')
    )
    return Response(summary)