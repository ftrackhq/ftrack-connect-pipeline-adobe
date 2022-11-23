# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_adobe.plugin import AdobeBasePlugin


class AdobeAssetManagerActionPlugin(
    plugin.AssetManagerActionPlugin, AdobeBasePlugin
):
    '''
    Class representing a Asset Manager Action Adobe Plugin
    '''
