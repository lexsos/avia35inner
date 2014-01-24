import csv
from math import fabs

from django.contrib import messages

from .models import MonthlyLimit, Month, Consumption, Phone


def to_float(str_number):
    return float(str_number.replace(',', '.'))


def add_consumption(month, phone_number, consumption_sum):
    monthly_limit = MonthlyLimit.objects.filter(
        deleted_at__isnull=True,
        phone__phone_number=phone_number
        )
    if monthly_limit.exists():
        monthly_limit = monthly_limit[0]
        consumption = Consumption(
            month=month,
            monthly_limit=monthly_limit,
            consumption_sum=consumption_sum,

        )
        consumption.save()


def test_consumption(request, row):
    phone_number = row[0]

    phone = Phone.objects.filter(phone_number=phone_number)
    if not phone.exists():
        messages.add_message(
            request,
            messages.WARNING,
            'Not found phone: {0} '.format(phone_number)
        )

    monthly_limit = MonthlyLimit.objects.filter(
        deleted_at__isnull=True,
        phone__phone_number=phone_number,
    )
    if not monthly_limit.exists():
        messages.add_message(
            request,
            messages.INFO,
            'Not found limit for {0} phone'.format(phone_number)
        )

    consumption_sum = 0
    for str_sum in row[1:7]:
        consumption_sum += to_float(str_sum)
    if fabs(to_float(row[7]) - consumption_sum) > 1:
        messages.add_message(
            request,
            messages.ERROR,
            'Consumption sum not eq for number {0}'.format(phone_number)
        )


def make_consumptions(request, month_pk):
    month = Month.objects.get(pk=month_pk)
    month.consumption_set.all().delete()
    csv_file = open(month.consumption_file._get_path(), 'rb')
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        test_consumption(request, row)
        consumption_sum = to_float(row[7])
        add_consumption(month, row[0], consumption_sum)
    messages.add_message(
        request,
        messages.INFO,
        'Month {0} processed'.format(month)
    )
