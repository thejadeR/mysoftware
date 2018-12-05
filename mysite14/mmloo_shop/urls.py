from django.conf.urls import url

from mmloo_shop import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^tb-cart/$',views.cart,name='tb-cart'),
]