# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from ftrack_connect_pipeline_qt.client.asset_manager import (
    QtAssetManagerClientWidget,
)
import ftrack_connect_pipeline.constants as constants
import ftrack_connect_pipeline_qt.constants as qt_constants
import ftrack_connect_pipeline_adobe.constants as adobe_constants


class AdobeQtAssetManagerClientWidget(QtAssetManagerClientWidget):
    ui_types = [
        constants.UI_TYPE,
        qt_constants.UI_TYPE,
        adobe_constants.UI_TYPE,
    ]
    '''Dockable adobe asset manager widget'''

    def __init__(self, event_manager, asset_list_model, parent=None):
        super(AdobeQtAssetManagerClientWidget, self).__init__(
            event_manager, asset_list_model, parent=parent
        )
        self.setWindowTitle('Adobe Pipeline Asset Manager')

    def get_theme_background_style(self):
        return 'adobe'