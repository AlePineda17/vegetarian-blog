from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect
from user.models import User
from django.views.generic import DetailView, UpdateView


def register(request):
    template = 'user/register.html'
    return render(request, template)


def process_register(request):
    if request.method == 'POST':
        new_user = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            username=request.POST['username'],
            date_of_birth=request.POST['date_of_birth'],
            gender=request.POST['gender'],
            picture=request.POST['picture'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        new_user.save()

        return HttpResponseRedirect(reverse('user:login'))
    return HttpResponse('Error:method not allowed.')


def login(request):
    template = 'user/login.html'
    return render(request, template)


def process_login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
        except User.DoesNotExist:
            return HttpResponse('User does not exist.')

        return HttpResponseRedirect(reverse('recipe:index', kwargs={'user_id': user.pk}))
    return HttpResponse('Error: method not allowed.')


class ProfileView(DetailView):
    model = User
    fields = [
        'picture',
        'username',
        'about',
    ]


class ProfileUpdate(UpdateView):
    model = User
    fields = '__all__'
    template_name = 'profile_update_form'
