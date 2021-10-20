"""BudgetProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as authViews

urlpatterns = [
    # accounts url referring for authentication views
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', authViews.LoginView.as_view(), name='login'),
    path('accounts/logout/', authViews.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', authViews.PasswordChangeView.as_view(
        template_name='registration/password_change.html'), name='password_change'),
    path('accounts/password_change/done/', authViews.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset/done/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
