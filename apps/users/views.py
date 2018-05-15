from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email


# 重写登陆验证类
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 首页
def index(request):
    return render(request, 'index.html')


# 用户登陆
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", '')
            password = request.POST.get("password", '')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request, 'login.html', {"msg": "邮箱未激活，请激活后再登陆！"})
            else:
                return render(request, 'login.html', {"msg": "账号或密码错误，请重新输入！"})
        else:
            return render(request, 'login.html', {"login_form": login_form})


# 用户登陆
# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username", '')
#         password = request.POST.get("password", '')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect('/')
#         else:
#             return render(request, 'login.html', {"msg": "账号或密码错误，请重新输入！"})
#     return render(request, 'login.html')


# 用户注册
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get("email")
            password = request.POST.get("password")
            have_user = UserProfile.objects.filter(email=username)
            if not have_user:
                user_profile = UserProfile(
                    username=username,
                    email=username,
                    password=make_password(password),
                    is_active=False
                )
                user_profile.save()

                send_register_email(username, "register")
                return render(request, 'login.html')
            else:
                return render(request, 'register.html', {"msg": "邮箱已经注册！"})
        else:
            return render(request, "register.html", {"register_form": register_form})


# 用户激活
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.filter(email=email).first()
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, 'login.html')


# 用户忘记密码
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm(request.POST)
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, 'send_success.html')
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})

#重置密码表单
class ResetView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "active_fail.html")
        return render(request, 'login.html')


# 修改密码逻辑实现
class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"msg": "两次密码不一致！", "email": email})
            else:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd2)
                user.save()
                return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"modify_form": modify_form, "email": email})


