from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from .models import Post, UserProfile, Report
from .telegram_utils import send_telegram_message


# Create your views here.

def load_large_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def index(request):
    text_head = 'Добро пожаловать в салон красоты «Hair Aprel»!'
    text_body = load_large_text('static/texts/text_6.txt')
    context = {'text_head': text_head, 'text_body': text_body}
    return render(request, 'index.html', context)


def about(request):
    text_head = 'Сведения о компании'
    text_about = load_large_text('static/texts/text_5.txt')
    context = {'text_head': text_head, 'text_about': text_about}
    return render(request, 'about.html', context)


def contacts(request):
    text_head = 'Контакты'
    name = 'Студия наращивания волос "HairAprel"'
    address = 'Санкт-Петербург, ул.Социалистическая, д.21'
    tel = '+7(812) 227-23-24'
    email = 'example@mail.ru'
    context = {'text_head': text_head, 'name': name, 'address': address, 'tel': tel, 'email': email}
    return render(request, 'contacts.html', context)


def services(request):
    name = 'Мы предоставляем следующие услуги:"'
    service1 = load_large_text('static/texts/text_1.txt')
    service2 = load_large_text('static/texts/text_2.txt')
    service3 = load_large_text('static/texts/text_3.txt')
    service4 = load_large_text('static/texts/text_4.txt')
    context = {'name': name, 'service1': service1,
               'service2': service2, 'service3': service3, 'service4': service4}
    return render(request, 'services.html', context)


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            UserProfile.objects.create(
                user=user,
                phone_number=form.cleaned_data.get('phone_number'),
                requested_service=form.cleaned_data.get('requested_service')
            )
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('service_response')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def service_response(request):
    return render(request, 'service_response.html')


def reg_auth(request):
    return render(request, 'reg_auth.html')


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'logged_out.html', {})


class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'


def send_post_to_telegram_view(request):
    report = Report.objects.all()
    send_telegram_message(chat_id='settings/CHAT_ID', report=report)
    return redirect('service_response')
