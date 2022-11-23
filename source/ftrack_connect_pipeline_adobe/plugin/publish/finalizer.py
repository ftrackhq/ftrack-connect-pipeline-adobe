# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

# import maya.cmds as cmds

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_qt import plugin as pluginWidget
from ftrack_connect_pipeline_adobe.plugin import (
    AdobeBasePlugin,
    AdobeBasePluginWidget,
)

from ftrack_connect_pipeline_adobe.utils import custom_commands as adobe_utils
from ftrack_connect_pipeline_adobe.constants import asset as asset_const


class AdobePublisherFinalizerPlugin(
    plugin.PublisherFinalizerPlugin, AdobeBasePlugin
):
    '''Class representing a Finalizer Plugin

    .. note::

        _required_output is a dictionary containing the 'context_id',
        'asset_name', 'asset_type_name', 'comment' and 'status_id' of the
        current asset
    '''

    def _run(self, event):
        '''Run the current plugin with the settings form the *event*.

        .. note::

           We are not committing the changes here to ftrack, as they should be
           committed in the finalizer plugin itself. This way we avoid
           publishing the dependencies if the plugin fails.
        '''
        self.version_dependencies = []
        ftrack_asset_nodes = adobe_utils.get_ftrack_nodes()
        for dependency in ftrack_asset_nodes:
            # dependency_version_id = cmds.getAttr(
            #     '{}.{}'.format(dependency, asset_const.VERSION_ID)
            # )
            self.logger.debug(
                'Adding dependency_asset_version_id: {}'.format(
                    dependency_version_id
                )
            )
            if dependency_version_id:

                dependency_version = self.session.query(
                    'select version from AssetVersion where id is "{}"'.format(
                        dependency_version_id
                    )
                ).one()

                if dependency_version not in self.version_dependencies:
                    self.version_dependencies.append(dependency_version)

        super_result = super(AdobePublisherFinalizerPlugin, self)._run(event)

        return super_result


class AdobePublisherFinalizerPluginWidget(
    pluginWidget.PublisherFinalizerPluginWidget, AdobeBasePluginWidget
):
    '''Class representing a Finalizer Widget

    .. note::

        _required_output is a dictionary containing the 'context_id',
        'asset_name', 'asset_type_name', 'comment' and 'status_id' of the
        current asset
    '''
