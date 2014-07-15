#encoding:utf-8
from django.db import models
from django.forms import ModelForm
from django import forms

class Check(models.Model):
    foto = models.FileField(upload_to='documents/%d/%m/%Y')
    
    def __unicode__(self):
        return self.question

class IndexForm(forms.Form):
    usuari = forms.CharField(widget=forms.TextInput, required=True, max_length=30)
    contrasenya = forms.CharField(widget=forms.PasswordInput, required=True, max_length=30)

class CheckForm(forms.Form):
    usuari = forms.CharField(widget=forms.TextInput, max_length=30, label='Usuari')
    hora = forms.DateTimeField(widget=forms.DateTimeInput, label='Check Time', input_formats=('%H:%M %d/%m/%y', '%H:%M:%S %d/%m/%y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y','%d/%m/%y %H:%M:%S', '%d/%m/%y %H:%M', '%d/%m/%y'))
    contrasenya = forms.CharField(widget=forms.TextInput, max_length=25, label='Contrasenya')
    lat = forms.CharField(widget=forms.TextInput, max_length=30, label='Latitude')
    lng = forms.CharField(widget=forms.TextInput, max_length=30, label='Longitude')
    foto = forms.FileField(label='Foto', help_text='max. 42 MB')
#    photo = forms.ImageField(widget=forms.FileInput)
#    tipo = forms.CharField(max_length=25)
#    error = forms.FloatField()

#    def __unicode__(self):
#        return self.question

#class Check(models.Model):
#    usuari = models.CharField(max_length=25)
#    hora = models.DateTimeField('Check Time')
#    contrasenya = models.CharField(max_length=25)
#    latitude = models.CharField(max_length=200)
#    longitude = models.CharField(max_length=200)
#    foto = models.ImageField(upload_to='/tmp')
#    tipo = models.CharField(max_length=25)
#    error = models.FloatField()
#
#    def __unicode__(self):
#        return self.question

#class Dieta(models.Model):
#    usuari = models.CharField(max_length=25)
#    hora = models.DateTimeField('Check Time')
#    contrasenya = models.CharField(max_length=25)
#    concepto = models.CharField(max_length=200)
#    error = models.FloatField()

#    def __unicode__(self):
#        return self.question
