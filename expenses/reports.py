import openpyxl
from django.http import HttpResponse
from .models import Expense

def export_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Date", "Category", "Amount", "Payment Mode"])

    for e in Expense.objects.all():
        ws.append([e.date, e.category, e.amount, e.payment_mode])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=expenses.xlsx'
    wb.save(response)
    return response
