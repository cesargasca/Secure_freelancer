'''URLS'''
from django.urls import path

from apps.users import views
from django.contrib.auth.decorators import login_required
app_name = 'users'
urlpatterns = [
    path('registrar/', views.RegisterView.as_view(), name='registrar'),
    path('publication_form/', login_required(views.publication_new), name='new_publication'),
    path('publication_list/', login_required(views.publication_list), name='list_publication'),
    path('publication_edit/<int:id_publication>/', login_required(views.publication_edit), name='edit_publication'),
    path('publication/<int:id_publication>/', login_required(views.publication_show), name='publication'),
    path('publication_delete/<int:id_publication>/', login_required(views.publication_delete), name='delete_publication'),
    path('perfil/<username>/', login_required(views.get_user_profile), name='get_user_profile'),
    path('index/',login_required(views.user_index),name='user_index'),
    path('postularse/<int:id_publication>/',login_required(views.postularse),name='postularse'),
    path('aceptar_rechazar/<int:id_publication>/<username>/<value>/',login_required(views.aceptar_rechazar),name='aceptar_rechazar'),
    path('contract_form/<int:id_publication>/<username>/', login_required(views.contract_new), name='new_contract'),
    path('contract_show/<int:id_publication>/<username>/', login_required(views.contract_show), name='show_contract'),
    path('contract_sign/<int:id_contrato>/<username>/<value>/', login_required(views.contract_client_sign), name='sign_contract'),
    path('terminosycondiciones/', views.terminosycondiciones, name='terminosycondiciones'),

]
