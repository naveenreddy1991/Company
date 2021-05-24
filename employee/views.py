from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
from .forms import SignUpForm
# Create your views here. 



def home(request):
    return render(request, 'home.html')
	
def search_product(request):
    """ search function  """
    if request.method == "GET":
        query = request.GET.get('search')  # your input name is 'search'
        print('Search word:' + str(query))
        if query:
            results=Employee.objects.filter(ename__icontains=query)
            return render(request, 'show.html', {"results":results})

    return render(request, 'show.html')
	
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  