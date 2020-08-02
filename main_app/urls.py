from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.base, name='base'),
	path('owner/',views.owner,name="owner"),
	path('error/', views.errorPage, name="error"),
	path('patients/', views.patients, name='patients'),
	path('patientDonations/', views.patientDonation, name='patientDonations'),
	path('sign/<str:pid>', views.sign, name="sign"),
	path('addPatients/', views.addPatients, name="addPatients"),
	path('addDoctor/', views.addDoctor, name="addDoctor"),
	path('donate/<str:pid>',views.donate, name="donate"),
	path('patientData/',views.patientDatabase,name="patientDatabase"),
	path('donationData/', views.donationData, name="donationData"),
	path('donationPage/',views.donationPage,name="donationPage"),
	path('withdrawData/', views.withdrawData, name="withdrawData"),
	path('withdrawAmount/<str:pid>',views.withdrawAmount,name="withdrawAmount"),
	path('transferDonation/<str:pid>', views.transferDonation,name="transferDonation")
]
