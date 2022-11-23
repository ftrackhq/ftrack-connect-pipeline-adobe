# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from ftrack_connect_pipeline.asset import FtrackObjectManager
from ftrack_connect_pipeline_adobe.asset.dcc_object import AdobeDccObject


class AdobeFtrackObjectManager(FtrackObjectManager):
    '''
    AdobeFtrackObjectManager class.
    Mantain the syncronization between asset_info and the ftrack information of
    the objects in the scene.
    '''

    DccObject = AdobeDccObject

    def __init__(self, event_manager):
        '''
        Initialize AdobeFtrackObjectManager with *event_manager*.

        *event_manager* instance of
        :class:`ftrack_connect_pipeline.event.EventManager`
        '''
        super(AdobeFtrackObjectManager, self).__init__(event_manager)
