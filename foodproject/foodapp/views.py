from django.http import HttpResponse
from django.shortcuts import render, redirect

from foodapp.forms import foods
from foodapp.models import foodtab


# Create your views here.
def index(request):
    obj = foodtab.objects.all()
    return render(request,"index.html",{'result':obj})

def details(request, food_id):
        obj2 =foodtab.objects.get(id=food_id)
        return render(request, "details.html", {'result2': obj2})

def adding(request):
    if request.method == "POST":
        fname=request.POST.get('name')
        fingre = request.POST.get('ingre')
        fdesc = request.POST.get('desc')
        fimage = request.FILES['image']
        food = foodtab(name=fname,ingre=fingre,desc=fdesc,image=fimage)
        food.save()
    return render(request, "add.html")

def update(request,id):
    foodobj = foodtab.objects.get(id=id)
    form = foods(request.POST or None, request.FILES, instance=foodobj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'result3':form, 'result4':foodobj})
def delete(request,id):
    if request.method=='POST':
        foodobj = foodtab.objects.get(id=id)
        foodobj.delete()
        return redirect('/')
    return render(request,'delete.html')


