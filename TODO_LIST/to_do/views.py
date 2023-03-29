from django.shortcuts import render
from .models import to_DO_List
from django.http import HttpResponseRedirect, HttpResponseNotFound

def create(request):
    products = to_DO_List.objects.all()
    if request.method == "POST":
        product = to_DO_List()
        product.name = request.POST.get("name")
        product.save()
        return HttpResponseRedirect("/")
    
    companies = to_DO_List.objects.all()
    return render(request, "index.html", {"companies": companies, "products": products})




def edit(request, id):
    try:
        product = to_DO_List.objects.get(id=id)
 
        if request.method == "POST":
            product.name = request.POST.get("name")
            product.save()
            return HttpResponseRedirect("/")
        else:
            companies = to_DO_List.objects.all()
            return render(request, "edit.html", {"product": product, "companies": companies})
    except to_DO_List.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
     

def delete(request, id):
    try:
        product = to_DO_List.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except to_DO_List.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")