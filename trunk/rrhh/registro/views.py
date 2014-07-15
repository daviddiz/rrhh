#encoding:utf-8
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from registro.models import Check, IndexForm, CheckForm
import xmlrpclib
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from datetime import *

@csrf_protect
def index(request):
	if request.method=='POST':
		formulario = IndexForm(request.POST)
		if formulario.is_valid():
			usuari = formulario.cleaned_data['usuari']
			contrasenya = formulario.cleaned_data['contrasenya']
			dbname = 'prevencontroltest'
			sock_common = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
			if sock_common.login(dbname, usuari, contrasenya):
				return HttpResponseRedirect(reverse('registro.views.checks', kwargs={'usuari':usuari,'contrasenya':contrasenya}))
			else:
				return HttpResponseRedirect('/rrhh/registro/')
	else:
		formulario = IndexForm()
	return render_to_response('registro/index.html', {'formulario':formulario}, context_instance=RequestContext(request)) 	
			
@csrf_protect
def checks(request, **kwargs):
	print "Request: %s"%request
	print "Files: %s"%request.FILES
	usuari = kwargs.get('usuari')
	contrasenya = kwargs.get('contrasenya')
	if request.method=='POST':
		lat = request.POST.get('lat')
		lng = request.POST.get('lng')
#		foto = request.POST.get('foto')
#		photo = request.FILES['photo']
#		return HttpResponseRedirect(reverse('registro.views.done', kwargs={'usuari':usuari,'contrasenya':contrasenya,'lat':lat,'lng':lng}))
#		return HttpResponseRedirect("registro/done/%s/%s/%s/%s/"%(usuari,contrasenya,lat,lng))
		return HttpResponseRedirect("/rrhh/registro/done/%s/%s/%s/%s/"%(usuari,contrasenya,lat,lng))
	else:
		formulario2 = CheckForm()
	return render_to_response('registro/check.html', {'formulario2':formulario2}, context_instance=RequestContext(request)) 	


#def done(request):
def done(request, **kwargs):
	print "Request: %s"%request
	usuari = kwargs.get('usuari')
	contrasenya = kwargs.get('contrasenya')
	lat = kwargs.get('lat')
	lng = kwargs.get('lng')
	hora = datetime.today()
#	foto = kwargs.get('foto')
#	photo = kwargs.get('photo')
	print "Usuari: %s"%usuari
	print "Contrasenya: %s"%contrasenya
	print "Latitude: %s"%lat
	print "Longitude: %s"%lng
	print "Hora: %s"%hora
#	print "Foto: %s"%foto
#	print "Photo: %s"%photo
#	if request.method=='POST':
#		formulario2 = CheckForm(request.POST, request.FILES)
#		if formulario2.is_valid():
#			nuevafoto = Check(foto = request.FILES['foto'])
#			nuevafoto.save()
#			usuari = formulario2.cleaned_data['usuari']
#			contrasenya = formulario2.cleaned_data['contrasenya']
#			lat = formulario2.cleaned_data['lat']
#			lng = formulario2.cleaned_data['lng']
#			hora = formulario2.cleaned_data['hora']
#			if lat and lng and usuari and contrasenya and hora and nuevafoto:
##				return HttpResponseRedirect('/rrhh/registro/done/')
#				return HttpResponseRedirect(reverse('registro.views.done', kwargs={'usuari':usuari,'contrasenya':contrasenya,'lat':lat,'lng':lng,'hora':hora,'foto':nuevafoto}))
#			else:
#				return HttpResponseRedirect(reverse('registro.views.checks', kwargs={'usuari':usuari,'contrasenya':contrasenya,'lat':lat,'lng':lng,'hora':hora,'foto':foto}))
#	else:
#		formulario2 = CheckForm()
###		formulario2 = ''
#	documents = Check.objects.all()
#	return render_to_response('registro/check.html', {'documents': documents,'formulario2':formulario2}, context_instance=RequestContext(request))
	t = loader.get_template('registro/done.html')
	c = Context({})
	return HttpResponse(t.render(c))

def error_check(request):
    t = loader.get_template('registro/error_check.html')
    c = Context({})
    return HttpResponse(t.render(c))

#def dietas(request):
#	t1 = loader.get_template('registro/index.html')
#	t2 = loader.get_template('registro/index.html')
#    c = Context({})
#    return HttpResponse(t.render(c))

#def index(request):
#    t = loader.get_template('registro/index.html')
#    c = Context({})
#    return HttpResponse(t.render(c))

