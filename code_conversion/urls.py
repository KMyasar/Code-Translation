from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='Home.html'), name='home'),
    path('price/', TemplateView.as_view(template_name='price.html'), name='price'),
    path('overview/', TemplateView.as_view(template_name='overview.html'), name='overview'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('progress/', TemplateView.as_view(template_name='progress.html'), name='progress'),
    path('beginner-taskpage/', TemplateView.as_view(template_name='beginner-taskpage.html'), name='beginner_taskpage'),
    path('intermediate/', TemplateView.as_view(template_name='intermediate.html'), name='intermediate'),
    path('advanced/', TemplateView.as_view(template_name='advanced.html'), name='advanced'),
    path('solved/', TemplateView.as_view(template_name='solved.html'), name='solved'),

    # Auth Pages
    path('login/', TemplateView.as_view(template_name='loginpage.html'), name='login'),
    path('signup/', TemplateView.as_view(template_name='signuppage.html'), name='signup'),
    path('forgot-password/', TemplateView.as_view(template_name='forgotpassword.html'), name='forgot_password'),
    path('verification/', TemplateView.as_view(template_name='verification.html'), name='verification'),
    path('new-password/', TemplateView.as_view(template_name='newpassword.html'), name='new_password'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
