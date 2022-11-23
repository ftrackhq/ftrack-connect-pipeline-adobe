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

    def remote_events_listener(self, remote_event_manager, adobe_id):
        # remote_event_manager.subscribe(
        #     'topic=ftrack.pipeline.host.run and data.pipeline.app_id={}'.format(
        #         adobe_id
        #     ),
        #     # TODO: we can call run or something like emit remote run, which emits a qt signal
        #     self.run,
        # )

        remote_event_manager.subscribe(
            'topic=ftrack.pipeline.client.launch and data.pipeline.app_id={}'.format(
                adobe_id
            ),
            self.remote_launch_client_coverter,
        )

    def remote_launch_client_coverter(self, event):
        name = event['data']['pipeline']['name']
        source = event['data']['pipeline']['source']
        self.launch_client(name, source)


