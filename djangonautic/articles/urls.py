from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='articles'
urlpatterns=[path('',views.index, name='index'),
path('create/',views.create,name='create'),
path('<str:slug>/',views.article_dis,name='article_dis'),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)