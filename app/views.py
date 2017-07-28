from django.views import View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize, deserialize
import json
from app.models import Account, AccountType
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def json_error(msg):
    return json.dumps({
        'errmsg': msg
    })


class AccountView(View):

    @staticmethod
    def query_set_json(data):
        return serialize('json', data, indent=2, use_natural_foreign_keys=True)

    @staticmethod
    def post(request, pk=None):
        response = HttpResponse(content_type='application/json')
        for dso in deserialize('json', request.body.decode(), ignorenonexistent=True):
            dso.object.id = None  # 让数据库决定id字段的值
            dso.save()
        response.write(json.dumps({
            'id': dso.object.id
        }))
        return response

    @staticmethod
    def get(request, pk):
        # 获取详情
        if pk is not None:
            response = HttpResponse(content_type='application/json')
            response.write(
                AccountView.query_set_json(Account.objects.filter(pk=int(pk)))
            )
        # 获取列表
        else:
            qs = Account.objects.all()
            # 设置过滤条件
            if request.GET.get('type'):
                qs = Account.objects.filter(type=int(request.GET.get('type')))
            if request.GET.get('login_to'):
                qs = qs.filter(login_url__contains=request.GET.get('login_to'))
            if request.GET.get('search_term'):
                qs = qs.filter(desc__contains=request.GET.get('search_term'))
            if request.GET.get('order_by'):
                # TODO: 检查order_by携带的值是否为有效数据库字段
                qs = qs.order_by(request.GET.get('order_by'))

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

            paginator = Paginator(qs, page_size)
            try:
                accounts = paginator.page(page_num)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                accounts = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of
                accounts = paginator.page(paginator.num_pages)

            response = HttpResponse(content_type='application/json')
            response.write(AccountView.query_set_json(accounts))

        return response

    @staticmethod
    def delete(request, pk):
        response = HttpResponse(content_type='application/json')
        qs = Account.objects.filter(pk=pk)
        if qs:
            qs.delete()
        else:
            response.status_code = 404
            response.write(
                json_error('account being requested to delete is not found...')
            )
        return response

    @staticmethod
    def put(request, pk):
        response = HttpResponse(content_type='application/json')

        if pk is None:
            response.status_code == 400
            response.write(json_error('need to specify an id in the url'))
            return response

        qs = Account.objects.filter(pk=pk)
        if qs:  # 请求的对象存在时
            for dso in deserialize('json', request.body.decode(), ignorenonexistent=True):
                if dso.object.id == int(pk):
                    dso.save()
                else:
                    response.status_code = 400
                    response.write(json_error('put 对象id与url id不一致'))
        else:  # 请求的对象不存在时
            response.status_code = 400
            response.write(json_error('put 对象必须已经存在'))

        return response

    @staticmethod
    def account_count(request):
        count = Account.objects.count()
        return HttpResponse(json.dumps({'count': count}).encode(), content_type='application/json')

    @staticmethod
    def account_type_list(request):
        return HttpResponse(
            AccountView.query_set_json(AccountType.objects.all()),
            content_type='application/json'
        )


class UserView(View):
    def post(self, request, pk):
        response = HttpResponse(content_type='application/json')
        for dso in deserialize('json', request.body.decode(), ignorenonexistent=True):
            dso.object.id = None  # 让数据库决定id字段的值
            dso.object.set_password(dso.object.password)
            dso.save()
        response.write(json.dumps({
            'id': dso.object.id
        }))
        return response

    def delete(self, request, pk):
        response = HttpResponse(content_type='application/json')
        pk = int(pk)
        User.objects.filter(pk=pk).delete()
        return response


def login(request):

    response = HttpResponse(content_type='application/json')
    user_dict = json.loads(request.body.decode())

    user = authenticate(username=user_dict.get('username'), password=user_dict.get('password'))
    if user:
        login(request, user)
    else:
        response.status_code = 403
        response.write(json_error('User name or password is invalid!'))

    return response


def logout(request):
    response = HttpResponse(content_type='application/json')
    logout(request)
    return response










