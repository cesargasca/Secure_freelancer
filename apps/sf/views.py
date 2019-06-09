'''views.py '''
from django.shortcuts import render


# Create your views here.
from .models import Test

def index(request):
    '''index controller'''
    algo = Test.objects.get(pk=1)
    current_user = request.user.username
    context = {
        'current_user': current_user,
        }
    print("------->" + str(request.user.is_authenticated))
    if not request.user.is_authenticated:
        return render(request, 'sf:index.html', context)
    else:
        return render(request,'users:user_index.html',context)
    
  