from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Users
from django.views import generic
from .forms import UserForm
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'users'


    def get_queryset(self):
        return Users.objects.all()


class AddUserFormView(generic.FormView):
    form_class = UserForm
    initial = {'key': 'value'}
    template_name_get = 'add_user.html'
    template_name_post = 'show_user.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form': form,
        }
        return render(
            template_name=self.template_name_get,
            request=request,
            context=context,
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
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
                template_name=self.template_name_post,
                request=request,
                context=context,
            )


class GetUserView(generic.DetailView):
    model = Users
    template_name = 'show_user.html'
    context_object_name = 'user'



class UserUpdateView(generic.edit.UpdateView):
    template_name = 'add_user.html'
    model = Users
    fields = [
        'username',
        'email',
    ]

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Users, id=id_)

class UserDeleteView(generic.DeleteView):
    model = Users
    template_name = 'confirm_delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users:index')