# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_qt import plugin as pluginWidget
from ftrack_connect_pipeline_adobe import constants as adobe_constants
from ftrack_connect_pipeline_adobe.utils import custom_commands as adobe_utils
from ftrack_connect_pipeline_adobe.asset import AdobeFtrackObjectManager
from ftrack_connect_pipeline_adobe.asset.dcc_object import AdobeDccObject


class AdobeBasePlugin(plugin.BasePlugin):

    host_type = adobe_constants.HOST_TYPE

    FtrackObjectManager = AdobeFtrackObjectManager
    '''FtrackObjectManager class to use'''
    DccObject = AdobeDccObject
    '''DccObject class to use'''

    @adobe_utils.run_in_main_thread
    def _run(self, event):
        return super(AdobeBasePlugin, self)._run(event)


class AdobeBasePluginWidget(AdobeBasePlugin, pluginWidget.BasePluginWidget):
    category = 'plugin.widget'
    ui_type = adobe_constants.UI_TYPE

    @adobe_utils.run_in_main_thread
    def _run(self, event):
        return super(AdobeBasePluginWidget, self)._run(event)


from ftrack_connect_pipeline_adobe.plugin.load import *
from ftrack_connect_pipeline_adobe.plugin.open import *
from ftrack_connect_pipeline_adobe.plugin.publish import *
from ftrack_connect_pipeline_adobe.plugin.asset_manager import *
