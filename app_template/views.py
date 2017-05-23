# -*- encoding:utf-8 -*-
import os
import json
import logging

from django.http import JsonResponse
from django.views.static import serve

from daovoice import models

LOG = logging.getLogger(__name__)


# Create your views here.


def __load_plugin_json():
    plugin_json_path = os.path.join(os.path.dirname(__name__), "plugin.json")
    assert os.path.exists(plugin_json_path), "Plugin Json `%s` Not Found " % str(plugin_json_path)
    with open(plugin_json_path, 'r') as f:
        return json.load(f)


PLUGIN_JSON = __load_plugin_json()

PLUGIN_HTML_DIR = os.path.join(os.path.dirname(__name__), "html")

assert os.path.exists(PLUGIN_HTML_DIR), "Plugin HTML directory %s not exists" % PLUGIN_HTML_DIR


def daovoice_hook_api(request, app_id):
    '''
     Open API Docs: http://docs.daovoice.io/api/#事件24
    :param request: django http request
    :param app_id: daovoice_app_id
    '''
    data = json.loads(request.body)
    topic = data.get("topic")
    if not topic:
        LOG.warn("Hook data has no topic ")
        return

    if str(topic).startswith("conversation"):
        conversation = models.Conversation.from_resp_json(data.get("data"))
        LOG.info("Handle daovoice webhook data Conversation %s", conversation)
        # do your stuffs with conversation object here


    elif str(topic).startswith("user"):
        user = models.User.from_resp_json(data.get("data"))
        LOG.info("Handle daovoice webhook data User %s", user)
        # do your stuffs with user object here .

    else:
        LOG.warn("Unknown topic %s hook received", topic)


def daovoice_plugin_setting_api(request):
    pass


def daovoice_plugin_json(request):
    return JsonResponse(PLUGIN_JSON)


def serve_plugin_page(request, path):
    serve(request, path, document_root=PLUGIN_HTML_DIR)


