from django.shortcuts import render,redirect
from todo.models import Task
# Create your views here.
def add(request):
    if (request.method=='POST'):
        heading_=request.POST['heading']
        detail_=request.POST['detail']
        date_=request.POST['date']
        print(heading_)
        print(detail_)
        print(date_)
        insert_data=Task.objects.create(heading=heading_ ,detail=detail_ ,date=date_ ,is_deleted='n')
        insert_data.save()
        return redirect('/')
    return render(request,'todo/add.html')

def index(request):
    content={}
    content['data']=Task.objects.filter(is_deleted='n')
    return render(request,'todo/index.html',content)

def delete(request,tid):
    record_to_be_deleted=Task.objects.filter(id=tid)
    #record_to_be_deleted.delete()
    record_to_be_deleted.update(is_deleted='y')
    return redirect('/')


def update(request,tid):
    if (request.method=='POST'):
        heading_=request.POST['heading']
        detail_=request.POST['detail']
        date_=request.POST['date']
        record_to_be_update=Task.objects.filter(id=tid)
        record_to_be_update.update(heading=heading_ ,detail=detail_ ,date=date_ ,is_deleted='n')
        return redirect('/')
    else:
        content={}
        content['data']=Task.objects.get(id=tid)
        return render(request,'todo/update.html',content)
