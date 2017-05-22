"""{{ app_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/


Make sure you've  add daovoice_urlpatterns  to  urlpatterns in the  project directory `urls.py`


"""

from django.conf.urls import url

from {{ app_name }} import views



daovoice_urlpatterns = [
	url(r'^plugin\.json$',views.daovoice_plugin_json),
	url(r'^hook/([^/]+)', views.daovoice_hook_api),
	url(r'^(?P<path>.*)', views.service_plugin_page),
	url(r'^plugin-setting', views.daovoice_plugin_setting_api)
]