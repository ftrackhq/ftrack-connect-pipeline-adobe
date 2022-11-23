# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from Qt import QtWidgets, QtCore

from ftrack_connect_pipeline_qt.client import log_viewer

from ftrack_connect_pipeline_adobe.utils.custom_commands import get_main_window


class AdobeQtLogViewerClientWidget(log_viewer.QtLogViewerClientWidget):
    '''Adobe log viewer dialog'''

    def __init__(self, event_manager, parent=None):
        super(AdobeQtLogViewerClientWidget, self).__init__(event_manager)

        # Make sure we stays on top of Adobe
        self.setWindowFlags(QtCore.Qt.Tool)
