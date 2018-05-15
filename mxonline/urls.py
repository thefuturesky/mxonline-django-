"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from users.views import index, LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView
from django.views.static import serve
from mxonline.settings import MEDIA_ROOT

# from django.views.generic import TemplateView
# path('', TemplateView.as_view(template_name="index.html"),name="index"),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include("captcha.urls")),
    path('', index, name="index"),
    path('user_login/', LoginView.as_view(), name="user_login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('active/<str:active_code>', ActiveUserView.as_view(), name="user_active"),
    path('forget/', ForgetPwdView.as_view(), name="forgetpwd"),  # 忘记密码url
    path('reset/<str:reset_code>', ResetView.as_view(), name="reset_pwd"),  # 重置密码表单url
    path('modifypwd/', ModifyPwdView.as_view(), name="modify_pwd"),  # 修改密码url

    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 文件上传访问处理

    path('org/', include("organization.urls", namespace="org")),  # 课程机构url配置
    path('course/', include("courses.urls", namespace="course")),  # 课程url配置

]
