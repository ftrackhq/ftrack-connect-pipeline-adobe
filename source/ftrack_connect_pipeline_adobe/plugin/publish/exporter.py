# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_qt import plugin as pluginWidget
from ftrack_connect_pipeline_adobe.plugin import (
    AdobeBasePlugin,
    AdobeBasePluginWidget,
)


class AdobePublisherExporterPlugin(
    plugin.PublisherExporterPlugin, AdobeBasePlugin
):
    '''Class representing an Exporter Plugin
    .. note::

        _required_output a Dictionary
    '''


class AdobePublisherExporterPluginWidget(
    pluginWidget.PublisherExporterPluginWidget, AdobeBasePluginWidget
):
    '''Class representing an Eporter Widget
    .. note::

        _required_output a Dictionary
    '''
