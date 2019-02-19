from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from wines import views as wine_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wines/',include('wines.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^$', wine_views.wine_list,name="home"),
    
]

urlpatterns += staticfiles_urlpatterns()