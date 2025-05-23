from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('landing/', views.landing, name='landing'),
    path('base/', views.base, name='base'),
    path('drbase/', views.drbase, name='drbase'),
    path('patientbase/', views.patientbase, name='patientbase'),
    path('patient_list/',views.patient_list, name='patient_list'),
    path('patient_record/',views.patient_record, name='patient_record'),
    path('patient_record2/',views.patient_record2, name='patient_record2'),
    path('booking/',views.booking, name='booking'),
    path('booking_table/',views.booking_table, name='booking_table'),
    # path('drtable/',views.drtable, name='drtable'),
    path('drtable2/<int:pk>/',views.drtable2, name='drtable2'),
    path('appoiment/<int:pk>/',views.appoiment, name='appoiment'),
    path('appoiment_data/<int:pk>/',views.appoiment_data,name='appoiment_data'),
    path('appoiment_list/',views.appoiment_list, name='appoiment_list'),
    path('patient_registration/',views.patient_registration, name='patient_registration'),
    path('success/', views.success, name='success'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('payment/<int:pk>/',views.payment,name='payment'),
    path('payment-status/<int:pk>',views.payment_status,name='payment-status'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)