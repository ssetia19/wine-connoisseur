from django.shortcuts import render
from .models import Test
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q


@login_required(login_url="/accounts/login")
# Create your views here.
def wine_list(request):
	wine_list = Test.objects.all()
	paginator = Paginator(wine_list,20)
	page = request.GET.get('page')
	wines = paginator.get_page(page)
	return render(request,'wines/wine_list.html',{'wines':wines})

def wine_search(request):
	query1 = request.GET.get('search-place-box')
	query2 = request.GET.get('search-grape-box')
	if query1 == "":
		wine_list = Test.objects.filter(Q(variety__icontains=query2))
	else:
		wine_list = Test.objects.filter((Q(country=query1)  | Q(province=query1) | Q(region_1=query1) | Q(region_2=query1)) & Q(variety__icontains=query2))
	paginator = Paginator(wine_list,20)
	page = request.GET.get('page')
	wines = paginator.get_page(page)
	return render(request,'wines/wine_list.html',{'wines':wines})

# def wine_search_grape(request):
# 	query = request.GET.get('search-grape-box')
# 	wines = Test.objects.filter(Q(variety__icontains=query))
# 	return render(request,'wines/wine_list.html',{'wines':wines})

def wine_sort(request):
	# return HttpResponse("sagar")
	wine_list = Test.objects.all().order_by('-price')
	paginator = Paginator(wine_list,20)
	page = request.GET.get('page')
	wines = paginator.get_page(page)
	return render(request,'wines/wine_list.html',{'wines':wines})

def wine_detail(request,slug):
	 # return HttpResponse(slug)
	var = Test.objects.get(id=slug)
	return render(request,'wines/wine_detail.html',{'wine':var})

