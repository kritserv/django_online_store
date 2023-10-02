"""
URL configuration for ddice_online_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from main import views
from main.formview.computer_formview import ComputerFormView
from main.formview.smartphone_formview import SmartphoneFormView
from main.formview.headphone_formview import HeadphoneFormView
from main.formview.cloth_formview import ClothFormView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path("", views.home, name = "home"),

	path("computer/product/<int:id>", views.product_computer, name = "view_product_computer"),
	path("smartphone/product/<int:id>", views.product_smartphone, name = "view_product_smartphone"),
	path("headphone/product/<int:id>", views.product_headphone, name = "view_product_headphone"),
	path("cloth/product/<int:id>", views.product_cloth, name = "view_product_cloth"),

	path('computer/', ComputerFormView.as_view(), name='view_computer'),
	path('smartphone/', SmartphoneFormView.as_view(), name='view_smartphone'),
	path('headphone/', HeadphoneFormView.as_view(), name='view_headphone'),
	path('cloth/', ClothFormView.as_view(), name='view_cloth'),

	path("product/addtocart/<str:title>", views.add_to_cart, name = "add_to_cart"),
	path("product/removefromcart/<str:title>", views.remove_from_cart, name = "remove_from_cart"),
	path("product/removeonefromcart/<str:title>", views.remove_single_item_from_cart, name = "remove_one_from_cart"),

	path('accounts/', include('allauth.urls')),
	
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
