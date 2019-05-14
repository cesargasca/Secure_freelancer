'''vistas Usuarios '''
#from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from apps.users.forms import PublicationForm
from apps.users.models import Publication
from apps.users.models import User
from apps.users.forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponseRedirect


      
class RegisterView(CreateView):
   form_class = RegisterForm
   
   template_name = 'users/registrar.html'
   success_url = reverse_lazy('users:user_index')
   
   
   def form_valid(self,form_class):
      username = self.request.POST['username']
      password = self.request.POST['password1']
      user = form_class.save()
      #new_user = authenticate(username=username,password=password)
      login(self.request,user)
      return HttpResponseRedirect(self.success_url)

def get_user_profile(request,username):
   #current_user = User.objects.get(username=request.user.username)
   if request.user.type_of_user == 'C':
      publications = Publication.objects.filter(user_id = request.user.id)
      context = {
        'current_user': request.user,
        'publications':publications,
        }
      return render(request, 'users/ClientProfile.html',context)
   else:
      return render(request,'users/FreelancerProfile.html', {"current_user":request.user})       

def user_index(request):
   current_user = request.user.username
   return render(request,'users/userIndex.html',{"current_user":current_user})

def publication_new(request):
   context = {}
   #context['current_user'] = request.user
   if request.method == 'POST':
      form = PublicationForm(request.POST)
      context['form'] = form
      if form.is_valid():
         np = form.save(commit=False)
         np.user_id = request.user.id
         np.save()
      return HttpResponseRedirect(reverse('users:get_user_profile',kwargs={'username':request.user.username}))
   else:
      form = PublicationForm()
   return render(request,'users/publication_form.html/',{'form':form,'current_user':request.user})

def publication_list(request):
   publications = Publication.object.all()
   context =   {'publications':publications}
   return render(request, 'publicaciones/publicaciones_list.html', context)

def publication_edit(request,id_Publication):
   publication = Publication.object.get(id=id_Publication)
   if request.method == 'GET':
      form = PublicationForm()  
   else:
      form = PublicationForm(request.POST,instance=publication)
      if form.is_valid():
         form.save()
      return redirect('users:list_publication')
   return render(request,'users/publication_form.html',{'form':form})

def publication_delete(request, id_Publication):
   publication = Publication.object.get(id=id_Publication)
   if request.method == 'GET':
      publication.delete()  
      return redirect('users:list_publication')
   return render(request,'users/publication_delete.html',{'publication':publication})
