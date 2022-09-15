from django.contrib import admin
from django.urls import path
from accountapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 메인 홈 화면
    path('', views.home, name = 'home'),
    # 로그인 페이지
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    # 회원가입 페이지
    path('register/', views.register, name = 'register'),
]
