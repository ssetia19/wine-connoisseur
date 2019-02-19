from django.conf.urls import url
from . import views


#namespaceing
app_name = 'wines'

urlpatterns = [
    url(r'^$', views.wine_list,name="list"),
    url(r'^wine_search/$',views.wine_search,name="search"),
    url(r'^wine_sort/$',views.wine_sort,name="sort"),
    # url(r'^wine_search_grape/$',views.wine_search_grape,name="search_grape"),
    url(r'^(?P<slug>[\w-]+)/$',views.wine_detail,name="detail"),


]
