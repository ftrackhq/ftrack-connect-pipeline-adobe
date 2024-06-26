# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from ftrack_connect_pipeline_qt.client import change_context
from ftrack_connect_pipeline_adobe.utils import custom_commands as adobe_utils

class AdobeQtChangeContextClientWidget(
    change_context.QtChangeContextClientWidget
):
    '''Adobe change context dialog'''

    def __init__(self, event_manager, parent=None):
        super(AdobeQtChangeContextClientWidget, self).__init__(
            event_manager, parent=parent
        )

    def show(self):
        if super(AdobeQtChangeContextClientWidget, self).show():
            # TODO: review this one, shouldn't call the init
            adobe_utils.init_adobe(self.context_id, self.session)
