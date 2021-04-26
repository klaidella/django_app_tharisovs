from django.shortcuts import render, HttpResponse
from .models import Users


def index(request):
    users = Users.objects.all()
    context = {
        'users': users,
    }

    return render(
        template_name='index.html',
        context=context,
        request=request,
    )


def add_user(request):
    if request.method == 'POST':
        user = Users(
            username=request.POST['username'],
            email=request.POST['email']
        )

        user.save()

        context = {
            'username': user.username,
            'email': user.email,
        }

        return render(
            template_name='show_user.html',
            request=request,
            context=context,
        )
    return render(
        template_name='add_user.html',
        request=request,
    )


def get_user(request, user_id):
    user = Users.objects.get(pk=user_id)

    context = {
        'username': user.username,
        'email': user.email,
    }

    return render(
        template_name='show_user.html',
        request=request,
        context=context,
    )



def edit_user(request, user_id):
    user = Users.objects.get(pk=user_id)

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        if len(username) != 0:
            user.username = username

        if len(email) != 0:
            user.email = email

        user.save()

        context = {
            'username': user.username,
            'email': user.email,
        }
        return render(
            template_name='show_user.html',
            context=context,
            request=request,
        )
    return render(
        template_name='add_user.html',
        request=request,
    )

def delete_user(request, user_id):
    user = Users.objects.get(pk=user_id)
    user.delete()

    return HttpResponse(f'Deleted user: {user.username}')