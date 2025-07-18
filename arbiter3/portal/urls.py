"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
]

if 'mozilla_django_oidc' in settings.INSTALLED_APPS:
    OIDC_PATHS = (
        path("accounts/login/", lambda request: redirect("/oidc/authenticate/")),
        path("accounts/", include("django.contrib.auth.urls")),
        path("oidc/", include("mozilla_django_oidc.urls")),
    )

    urlpatterns.extend(OIDC_PATHS)
else:
    urlpatterns.append(path("accounts/", include("django.contrib.auth.urls"))),

if 'arbiter3.arbiter' in settings.INSTALLED_APPS:
    urlpatterns.append(path('', include('arbiter3.arbiter.urls')))

urlpatterns += staticfiles_urlpatterns()
