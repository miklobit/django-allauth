from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import Bitrix24Provider


urlpatterns = default_urlpatterns(Bitrix24Provider)
