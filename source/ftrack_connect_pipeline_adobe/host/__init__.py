# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

import logging
from ftrack_connect_pipeline.host import Host
from ftrack_connect_pipeline_qt import constants as qt_constants
from ftrack_connect_pipeline_adobe import constants as adobe_constants
from ftrack_connect_pipeline_adobe.host import engine as host_engine

logger = logging.getLogger(__name__)


class AdobeHost(Host):
    '''
    AdobeHost class.
    '''

    host_types = [qt_constants.HOST_TYPE, adobe_constants.HOST_TYPE]
    # Define the Adobe engines to be run during the run function
    engines = {
        'asset_manager': host_engine.AdobeAssetManagerEngine,
        'loader': host_engine.AdobeLoaderEngine,
        'opener': host_engine.AdobeOpenerEngine,
        'publisher': host_engine.AdobePublisherEngine,
    }

    def __init__(self, event_manager):
        '''
        Initialize AdobeHost with *event_manager*.

        *event_manager* instance of
        :class:`ftrack_connect_pipeline.event.EventManager`
        '''
        super(AdobeHost, self).__init__(event_manager)

    def run(self, event):
        runnerResult = super(AdobeHost, self).run(event)
        return runnerResult
