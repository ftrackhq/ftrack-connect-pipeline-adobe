# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from Qt import QtWidgets, QtCore

from ftrack_connect_pipeline_adobe.constants.asset import modes as load_const

from ftrack_connect_pipeline_qt.client import load
import ftrack_connect_pipeline.constants as constants
import ftrack_connect_pipeline_qt.constants as qt_constants
import ftrack_connect_pipeline_adobe.constants as adobe_constants
from ftrack_connect_pipeline_adobe.utils.custom_commands import get_main_window


class AdobeQtAssemblerClientWidget(load.QtAssemblerClientWidget):
    '''Adobe assembler dialog'''

    ui_types = [
        constants.UI_TYPE,
        qt_constants.UI_TYPE,
        adobe_constants.UI_TYPE,
    ]

    def __init__(self, event_manager, asset_list_model, parent=None):
        super(AdobeQtAssemblerClientWidget, self).__init__(
            event_manager,
            load_const.LOAD_MODES,
            asset_list_model,
        )

        # Make sure we stays on top of Adobe
        self.setWindowFlags(QtCore.Qt.Tool)
