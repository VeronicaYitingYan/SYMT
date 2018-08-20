

from django.conf.urls import url, include
from django.contrib import admin

#importing views from newsletter app 
urlpatterns = [	
    url(r'^admin/', admin.site.urls),
    url(r'^', include('mywaitfree.urls'))
]