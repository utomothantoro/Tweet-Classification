"""Sentiment_Analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from Sentiment_Classification import views as Sentiment_Classification_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', Sentiment_Classification_views.home),
	url(r'^home/$', Sentiment_Classification_views.home),
	#url(r'^about/$', Sentiment_Classification_views.about),
	url(r'^sentiment_analysis/$', Sentiment_Classification_views.sentiment_analysis),
	url(r'^help/$', Sentiment_Classification_views.help),
	url(r'^login/', Sentiment_Classification_views.login_view),
	url(r'^logout/', Sentiment_Classification_views.logout_view),
	url(r'^tweets/', Sentiment_Classification_views.get_tweets),
	#url(r'^choose_file/', Sentiment_Classification_views.get_file),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)