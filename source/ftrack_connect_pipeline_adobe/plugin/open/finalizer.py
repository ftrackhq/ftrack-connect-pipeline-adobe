# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_qt import plugin as pluginWidget
from ftrack_connect_pipeline_adobe.plugin import (
    AdobeBasePlugin,
    AdobeBasePluginWidget,
)


class AdobeOpenerFinalizerPlugin(plugin.OpenerFinalizerPlugin, AdobeBasePlugin):
    '''Class representing a Finalizer Plugin

    .. note::

        _required_output is a dictionary containing the 'context_id',
        'asset_name', 'asset_type_name', 'comment' and 'status_id' of the
        current asset
    '''


class AdobeOpenerFinalizerPluginWidget(
    pluginWidget.OpenerFinalizerPluginWidget, AdobeBasePluginWidget
):
    '''Class representing a Finalizer Widget

    .. note::

        _required_output is a dictionary containing the 'context_id',
        'asset_name', 'asset_type_name', 'comment' and 'status_id' of the
        current asset
    '''
