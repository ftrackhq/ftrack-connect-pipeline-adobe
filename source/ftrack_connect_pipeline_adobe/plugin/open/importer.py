# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

import adobe

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_qt import plugin as pluginWidget
from ftrack_connect_pipeline_adobe.plugin import (
    AdobeBasePlugin,
    AdobeBasePluginWidget,
)

from ftrack_connect_pipeline_adobe.utils import custom_commands as adobe_utils
from ftrack_connect_pipeline_adobe.constants.asset import modes as load_const
from ftrack_connect_pipeline_adobe.constants import asset as asset_const


class AdobeOpenerImporterPlugin(plugin.OpenerImporterPlugin, AdobeBasePlugin):
    '''Class representing a Collector Plugin

    .. note::

        _required_output a List
    '''

    load_modes = {
        load_const.OPEN_MODE: load_const.LOAD_MODES[load_const.OPEN_MODE]
    }

    dependency_load_mode = load_const.OPEN_MODE

    @adobe_utils.run_in_main_thread
    def get_current_objects(self):
        return adobe_utils.get_current_scene_objects()


class AdobeOpenerImporterPluginWidget(
    pluginWidget.OpenerImporterPluginWidget, AdobeBasePluginWidget
):
    '''Class representing a Collector Widget

    .. note::

        _required_output a List
    '''
