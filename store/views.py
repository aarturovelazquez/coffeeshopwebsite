from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import UserForm
from .mongofunction import *
from .mysqlapi import *

def sign_up(request):
	form = UserForm()
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
	context = {'form':form}
	return render(request, 'store/sign_up.html', context)

def home(request):
	return render(request, 'store/index.html')

def products(request):
	list_cursor = mongodbGet();
	output = ""
	template = loader.get_template('store/products.html')
	context = {
		'list_cursor' : list_cursor,
	}
	return HttpResponse(template.render(context, request))

def addproduct(request):
	if request.method == 'POST':
		newname = request.POST.get('product_name')
		newcost = request.POST.get('product_cost')
		newimage = request.POST.get('product_image')
		mongodbInsert(newname, newcost, newimage)
		return HttpResponseRedirect(reverse('Manage_Products'))
	return render(request, 'store/productinsert.html')

def productmanager(request):
	list_cursor = mongodbGet();
	output = ""
	template = loader.get_template('store/productmanager.html')
	context = {
		'list_cursor' : list_cursor,
	}
	return HttpResponse(template.render(context, request))

def delete(request, id):
	mongodbDelete(id)
	return HttpResponseRedirect(reverse('Manage_Products'))

def update(request, id):
	product= mongodbFind(id)
	template = loader.get_template('store/productupdate.html')
	context = {
		'product': product,
	}
	return HttpResponse(template.render(context, request))
	
def productupdate(request, id):
	if request.method == 'POST':
		updatename = request.POST['product_name']
		updatecost = request.POST['product_cost']
		updateimage = request.POST['product_image']
		mongodbUpdate(id, updatename, updatecost, updateimage)
		return HttpResponseRedirect(reverse('Manage_Products'))

def checkout(request, id):
	product= mongodbFind(id)
	template = loader.get_template('store/checkout.html')
	context = {
		'product' : product,
	}
	if request.method == 'POST':
		newfirstname = request.POST.get('order_firstname')
		newlastname = request.POST.get('order_lastname')
		newemail = request.POST.get('order_email')
		newaddress = request.POST.get('order_address')
		newcountry = request.POST.get('order_country')
		newcity = request.POST.get('order_city')
		newzip = request.POST.get('order_zip')
		newproduct = request.POST.get('order_products')
		post_to_api(url, headers, newfirstname, newlastname, newemail, newaddress, newcountry, newcity, newzip, newproduct)
		return HttpResponseRedirect(reverse('Coffee Bags'))
	return HttpResponse(template.render(context, request))

def addorder(request):
	if request.method == 'POST':
		newfirstname = request.POST.get('order_firstname')
		newlastname = request.POST.get('order_lastname')
		newemail = request.POST.get('order_email')
		newaddress = request.POST.get('order_address')
		newcountry = request.POST.get('order_country')
		newcity = request.POST.get('order_city')
		newzip = request.POST.get('order_zip')
		newproduct = request.POST.get('order_products')
		post_to_api(url, headers, newfirstname, newlastname, newemail, newaddress, newcountry, newcity, newzip, newproduct)
		return HttpResponseRedirect(reverse('Coffee Bags'))
