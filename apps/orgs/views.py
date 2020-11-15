from django.shortcuts import render
from .models import OrgInfo, TeacherInfo, CityInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from operations.models import UserLove


# Create your views here.

def org_list(request):
    all_orgs = OrgInfo.objects.all().order_by('id')
    all_citys = CityInfo.objects.all()
    sort_orgs = all_orgs.order_by('-love_num')[:3]

    # 按照机构类别进行过滤筛选
    cate = request.GET.get('cate', '')
    if cate:
        all_orgs = all_orgs.filter(category=cate)

    # 按照地区类别进行过滤筛选
    cityid = request.GET.get('cityid', '')
    if cityid:
        all_orgs = all_orgs.filter(cityinfo_id=int(cityid))

    # 排序
    sort = request.GET.get('sort', '')
    if sort:
        all_orgs = all_orgs.order_by('-' + sort)

    # 分页功能
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(all_orgs, 3)

    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request, 'orgs/org-list.html', {
        'all_orgs': all_orgs,
        'pages': pages,
        'all_citys': all_citys,
        'sort_orgs': sort_orgs,
        'cate': cate,
        'cityid': cityid,
        'sort': sort
    })


def org_detail(request, org_pk):
    if org_pk:
        org = OrgInfo.objects.filter(pk=int(org_pk))[0]

        return render(request, 'orgs/org-detail-homepage.html', {
            'org': org
        })
