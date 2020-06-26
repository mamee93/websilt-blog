
from django.shortcuts import render
from  .forms import AdForm
from .models import Ad,Category
# Create your views here.
 
def all_ads(request):
    all_ads = Ad.objects.all()
    return render(request,'ad/all-ads.html',{'ads':all_ads})

def single_ad(request,id):
    ad = Ad.objects.get(id=id)
    return render(request,'ad/single.html',{'ad':ad})

def all_categories(request):
    all_category = Category.objects.filter(main_category = None)

    return render(request,'ad/all-categories.html',{'all_category':all_category})

def category_ads(request,id):

    return render(request,'ad/category_ads.html',{})


def add_ad(request):

    if request.method == "POST": ## save
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
    else:
        form = AdForm()

    return render(request,'ad/post-ad.html',{'form':form})