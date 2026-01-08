import openpyxl
from django.http import HttpResponse
from django.db.models import Sum
from .models import Expense

# we use openpyxl to get the summary reports of total expenses by category in Excel format
def export_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Expense Summary"

    # Header
    ws.append(["Category", "Total Amount"])

    # GROUP BY category + SUM amount
    expenses = Expense.objects.values('category').annotate(
        total_amount=Sum('amount')
    )

    for e in expenses:
        ws.append([e['category'], e['total_amount']])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=expense_summary.xlsx'

    wb.save(response)
    return response
