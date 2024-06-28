from django.shortcuts import render, redirect ,get_object_or_404 # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import logout, authenticate, login# type: ignore
from datetime import datetime
from home.models import Contact
from django.contrib import messages # type: ignore
from home.models import Deal
from home.models import Banner


#usename: sagar and password:djangosagar10
# Create your views here.
def index(request):

    banner=Banner.objects.all()
    
    return render(request, 'index.html',{'banners':banner})
    #return HttpResponse("This is homepage")

def breadfruit(request, username):
    # username:breadfruit
    # password:userbf1234
    user = get_object_or_404(User, username='breadfruit' and 'admin')
    deals = Deal.objects.filter(user=user)
    return render(request, 'vendors/breadfruit.html', {'deals': deals, 'username': username})

def daraz(request, username):
    # username:daraz
    # password:dealsite123
    user = get_object_or_404(User, username='daraz')
    deals = Deal.objects.filter(user=user)
    return render(request, 'vendors/daraz.html', {'deals': deals, 'username': username})

def itti(request, username):
    # username:itti
    # password:dealsite1234
    user = get_object_or_404(User, username='itti')
    deals = Deal.objects.filter(user=user)
    return render(request, 'vendors/daraz.html', {'deals': deals, 'username': username})

def esewa(request, username):
    # username:esewa
    # password:dealsitesewa
    user = get_object_or_404(User, username='esewa')
    deals = Deal.objects.filter(user=user)
    return render(request, 'vendors/esewa.html', {'deals': deals, 'username': username})

def brand(request, name):
    # username:daraz
    # password:
    user = get_object_or_404(User, username=name)
    deals = Deal.objects.filter(user=user)
    return render(request, 'daraz.html', {'deals': deals, 'username': name})

def dashboard(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    user = request.user
    deals =Deal.objects.filter(user=user)
    
    return render(request, 'dashboard.html',{'deals': deals})

def addDeal(request):

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        images = request.FILES['images']
        code = request.POST.get('code')
        url = request.POST.get('link')
        deal = Deal(title=title, description=description, images=images, code=code, url=url, user=request.user)
        deal.save()
        messages.success(request, "Deal has been uploaded!")
        return redirect("dashboard")  # Redirect back to the dashboard after successful submission
    
    return render(request, 'addDeal.html')
 
def contact(request):
    if request.method== "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")


    return render(request, 'contact.html')

   # return HttpResponse("This is contact page")

def services(request):
    return render(request, 'services.html')

def loginUser(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password=request.POST.get('password')
        # print(username, password)

                # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
             # A backend authenticated the credentials
             login(request,user)
             return redirect("/dashboard")
        else:
            return render(request, 'login.html')
   
    return render(request, 'login.html')

def register(request):
    if request.method=="POST":
        username= request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        # print(username, password)
                # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
             # A backend authenticated the credentials
             login(request,user)
             return redirect("/dashboard")
        else:
            return render(request, 'login.html')
   
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")

def edit_deal(request, deal_id):
    deal = Deal.objects.get(pk=deal_id)
    if deal.user != request.user:
        return render(request, 'edit_deal.html', {'deal': deal})
    if request.method == "POST":
        # Update deal details based on form data
        deal.title = request.POST.get('title')
        deal.description = request.POST.get('description')
        deal.code = request.POST.get('code')
        deal.url=request.POST.get('link')
        if 'images' in request.FILES:
            deal.images = request.FILES['images']
        deal.save()
        messages.success(request, "Deal has been updated successfully!")
        return redirect("/dashboard/")
    return render(request, 'edit_deal.html', {'deal': deal})

def delete_deal(request, deal_id):
    # Retrieve the deal object
    deal = Deal.objects.get(pk=deal_id)
    if deal.user == request.user:
        # Your delete logic here
        deal.delete()
    return redirect('dashboard')

def banner(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        # Handle form submission manually
        image = request.FILES.get('image')
        if image and url:
            banner = Banner.objects.create(image=image, url=url, user=request.user)
            # Optionally, you can perform additional validation or processing here
            return redirect('banner')  # Redirect to the same page after successful form submission
    
    user = request.user
    banners = Banner.objects.filter(user=user) 
     # Retrieve all uploaded banners
    return render(request, 'banner.html', {'banners': banners})

def delete_banner(request, banner_id):
    banner = get_object_or_404(Banner, pk=banner_id)
    banner.delete()
    return redirect('banner')  # Redirect to a relevant URL after deletion
