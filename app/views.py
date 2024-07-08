from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def group_index(request, group_name):
    print('Group', group_name)
    return render(request, 'group_index.html', {'groupname':group_name}) 
