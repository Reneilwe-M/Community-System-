# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from reports.models import Issue


# def register(request):

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('login')

#     else:
#         form = UserCreationForm()

#     return render(request, 'users/register.html', {'form': form})

# @login_required
# def staff_dashboard(request):

#     issues = Issue.objects.all()

#     return render(request, 'reports/staff_dashboard.html', {'issues': issues})


# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from reports.models import Issue

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             role = request.POST.get('role')
#             if role == 'staff':
#                 return redirect('staff_dashboard')
#             else:
#                 return redirect('report_issue')  # your resident page
#     else:
#         form = AuthenticationForm()
#     return render(request, 'users/login.html', {'form': form})

# @login_required
# def staff_dashboard(request):
#     issues = Issue.objects.all()
#     return render(request, 'reports/staff_dashboard.html', {'issues': issues})



from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from reports.models import Issue
from django.contrib.auth.models import User
from django.contrib.auth import logout

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             role = request.POST.get('role')
#             if role == 'staff':
#                 return redirect('staff_dashboard')
#             else:
#                 return redirect('report')   # residents go to report page
#     else:
#         form = AuthenticationForm()

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Staff or superuser → staff dashboard
            if user.is_staff or user.is_superuser:
                return redirect('reports/staff_dashboard.html')
            # Regular user → report page
            else:
                return redirect('reports/report_issue.html')
        # else:
        #     if User.objects.filter(username=username).exists():
        #         # Username exists but wrong password
        #         error = 'Incorrect password. Please try again.'
        #     else:
        #         # Username does not exist → send to register
        #         return redirect('/register/')
    return render(request, 'users/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password1)
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('login')
    return render(request, 'users/register.html')

@login_required
def staff_dashboard(request):
    issues = Issue.objects.all()
    return render(request, 'reports/staff_dashboard.html', {'issues': issues})

def logout_view(request):
    logout(request)
    return redirect('/login/')

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('reports/staff_dashboard.html')
        else:
            return reverse_lazy('home')