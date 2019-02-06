
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('home/', include('myapp.urls')),
    path('login/', include('myapp.urls')),
    path('signup/', include('myapp.urls')),
    path('contact/', include('myapp.urls')),
    path('loginsuccess/', include('myapp.urls')),
    path('credit/', include('myapp1.urls')),
    path('debit/', include('myapp1.urls')),
    path('logout/', include('myapp1.urls')),
    path('check_bal/', include('myapp1.urls')),
    path('edit_profile/', include('myapp1.urls')),

]
