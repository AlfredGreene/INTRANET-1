from django.shortcuts import render, redirect
from django.contrib import auth

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
						'warning': 'Your account is disabled.',
						'title':'Iniciar Sesión',
					})
		else:
			return render(request, 'auth/login.html',{
					'warning': 'Invalid username or password',
					'title':'Iniciar Sesión',
				})

def logout(request):

	auth.logout(request)
	return redirect('/')


def register(request):

	if request.method == 'GET':
		return render(request, 'auth/register.html',{'title':'Registrarse'})
	elif request.method == 'POST' :
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		# LLamamos al formulario de usuario desde el ORM.
		auth.models.User.objects.create_user(username,email,password).save()
		user = auth.authenticate(username = username, password = password)
		auth.login(request, user)
		return render(request, 'frontend/index.html',{'title':'registro satisfactorio'})
