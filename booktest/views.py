from django.shortcuts import render
from django.http import JsonResponse
from booktest.models import ProvCity

# Create your views here.


def index(request):

    return render(request,'booktest/index.html')

def prov(request):
    areas=ProvCity.objects.filter(aid__isnull=True)
    # areas_list=areas.values('aid','abittle')
    areas_list =[]
    for area in areas:
        # print(area.aid)
        # print(area.abittle)
        # print(area.id)
        # print((area.aid,area.abittle))
        areas_list.append((area.id,area.abittle))
    return JsonResponse({'data': list(areas_list)})


def city(request,pid):

    areas=ProvCity.objects.filter(aid__id=pid)
    areas_list =[]
    for area in areas:
        # print(area.aid)
        # print(area.abittle)
        # print(area.id)
        # print((area.aid,area.abittle))
        areas_list.append((area.id,area.abittle))
    return JsonResponse({'data': list(areas_list)})

from django.core.paginator import Paginator
def show_area(request,pindex):
        areas=ProvCity.objects.filter(aid__isnull=True)
        paginator=Paginator(areas,5)
        if pindex=="":
            pindex=1
        else:
            pindex=int(pindex)
        page=paginator.page(pindex)
        return render(request,'booktest/show_area.html',{'page':page})




