from django.views import View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize
import json
from app.models import Account


def account_count(request):
    count = Account.objects.count()
    return HttpResponse(json.dumps({'count': count}).encode(), content_type='application/json')


class AccountList(View):

    @staticmethod
    def get(request):
        max_page_size = 100
        min_page_size = 1

        input_page_size = request.GET.get('page_size')
        if input_page_size is not None:
            page_size = int(input_page_size)
            page_size = min(page_size, max_page_size)
            page_size = max(page_size, min_page_size)
        else:
            page_size = 10

        input_page_num = request.GET.get('page')
        if input_page_num is not None:
            page_num = int(input_page_num)
        else:
            page_num = 1

        paginator = Paginator(Account.objects.all().order_by('id'), page_size)
        try:
            accounts = paginator.page(page_num)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            accounts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            accounts = paginator.page(paginator.num_pages)

        response = HttpResponse(content_type='application/json')
        response.write(serialize('json', accounts, use_natural_foreign_keys=True, indent=2))
        return response


class AccountDetail(View):

    @staticmethod
    def get(request, pk):
        response = HttpResponse(content_type='application/json')
        response.write(serialize('json', Account.objects.filter(pk=pk), use_natural_foreign_keys=True, indent=2))
        return response



