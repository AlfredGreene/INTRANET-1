from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.mail import send_mail
from decouple import config
from django.contrib.auth.decorators import user_passes_test

def login(request):

	if request.method == 'GET':
		return render(request, 'auth/login.html',{'title':'Iniciar Sesión'})
	elif request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate( username = username, password = password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				next = ''

				if 'next' in request.GET:
					next = request.GET['next']

				if next == None or next == '':
					next = '/'
				return redirect(next)
			else:
				return render(request, 'auth/login.html', {
						'warning': 'Su cuenta ha caducado.',
						'title':'Iniciar Sesión',
					})
		else:
			return render(request, 'auth/login.html',{
					'warning': 'Usuario o contraseña erronea',
					'title':'Iniciar Sesión',
				})

def logout(request):

	auth.logout(request)
	return redirect('/')


def register(request):

	if request.method == 'GET':

		return render(request, 'auth/register.html',{
			'title':'Registro',
			'error':{
				'error':'hide',
			}
		})

	elif request.method == 'POST' :

		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		if not email.endswith('@phoenixwt.com.pa'):
			return render(request, 'auth/register.html',{
				'title':'Error de Registro',
				'error':{
					'error':'show',
					'email':'Su correo debe terminar en "@phoenixwt.com.pa"',
					'contacto':'Por favor contactar al administrador de sistemas, soporte@phoenixwt.com.pa'
				}
			})
		# LLamamos al formulario de usuario desde el ORM.
		auth.models.User.objects.create_user(username,email,password).save()
		user = auth.authenticate(username = username, password = password)
		auth.login(request, user)

		send_mail(
		            'Registro de usuario',
		            '%s, %s' % (username,email) ,
		            config("INTRA_EMAIL_HOST_USER",),
		            [config("INTRA_EMAIL_HOST_USER",)],
		            fail_silently=False,
		        )

		return render(request, 'auth/registered.html',{'title':'registro satisfactorio'})
