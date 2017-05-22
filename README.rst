daovoice-plugin-template
-------------------------------

DaoVoice 插件 Django 应用模版， 帮您快速创建第一个插件。




**使用指南**::


	- ``git clone git@github.com:yowenter/daovoice-plugin-template.git``
	- ``django-admin startapp --template={daovoice-plugin-template repo directory }/template myapp``




**模块详解**::

	- ``plugin.json``, 您的插件 Schema 。
	- ``html``, 您的插件页面
	- ``views.py``, 插件逻辑代码。 包含 处理 Daovoice WebHook 逻辑和插件设置保存逻辑。
	- ``models.py``, DaoVoice 插件数据模型。




