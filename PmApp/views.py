from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from . models import Passwd
from . forms import PmForm



# Create your views here.
@login_required(login_url='login')
def add(request):
    frm=PmForm
    if request.POST:
        frm=PmForm(request.POST)
        if frm.is_valid:
            inst = frm.save(commit=False)
            inst.userid = request.user
            inst.save()
            return redirect('dashboard')
        else:
            frm=PmForm
    return render(request,'PM.html',{'frm':frm})

# def edit(request,pk):
#     inst_to_edit=PmForm.objects.get(pk=pk)
#     frm=PmForm(inst_to_edit)
#     return render(request,'PM.html',{'frm':frm})
@login_required(login_url='login')
def edit(request, pk):
    inst_to_edit = Passwd.objects.get(pk=pk)
    if request.method == "POST":
        frm = PmForm(request.POST, instance=inst_to_edit)
        if frm.is_valid():
            frm.save() 
            return redirect('dashboard')    
    else: 
        frm = PmForm(instance=inst_to_edit)
    return render(request, 'PM.html', {'frm': frm})



from django.contrib import messages
@login_required(login_url='login')
def view(request):
    if request.user.is_authenticated:
        print(request.user.id)
        visits = int(request.COOKIES.get('visits',0))
        visits = visits + 1
        passwords=Passwd.objects.all()
        print(passwords)
        respo = render(request,'view.html',{'passwords':passwords,'visits':visits})
        respo.set_cookie('visits',visits)
        return respo



@login_required(login_url='login')
def delete(request,pk):
    inst=Passwd.objects.get(pk=pk)
    inst.delete()
    passwords=Passwd.objects.all()
    return render(request,'view.html',{'passwords':passwords})

""" def dashboard(request):

    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
        user = request.user
        user_pass = Passwd.objects.filter(userid=user)

    
    return render(request,'dashboard.html',{'user_pass':user_pass} ) """

@login_required(login_url='login') # Redirect to login if not authenticated
def dashboard(request):
    messages.success(request, f"Logged in as {request.user}")
    user_pass = Passwd.objects.filter(userid=request.user)
    return render(request, 'dashboard.html', {'user_pass': user_pass})



    
    
 