# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

# Example DCC bootstrap script based on Maya userSetup.py
import os
import sys
import logging
import functools
import atexit

import ftrack_api
from Qt import QtWidgets, QtCore

from ftrack_connect_pipeline import constants as core_constants
from ftrack_connect_pipeline.configure_logging import configure_logging

from ftrack_connect_pipeline_qt import event
from ftrack_connect_pipeline_qt import constants as qt_constants
from ftrack_connect_pipeline_qt.ui.asset_manager.model import AssetListModel

from ftrack_connect_pipeline_adobe import host as adobe_host
from ftrack_connect_pipeline_adobe.client import (
    open as ftrack_open,
    load,
    asset_manager,
    publish,
    change_context,
    log_viewer,
)
from ftrack_connect_pipeline_qt.client import documentation

from ftrack_connect_pipeline_adobe.utils import custom_commands as adobe_utils

configure_logging(
    'ftrack_connect_pipeline_adobe',
    extra_modules=['ftrack_connect_pipeline', 'ftrack_connect_pipeline_qt'],
    propagate=False,
)


logger = logging.getLogger('ftrack_connect_pipeline_adobe')

logger.info('Initializing Adobe Framework POC')

class StandaloneApplication(QtWidgets.QApplication):

    openClient = QtCore.Signal(object, object, object, object)

    created_widgets = dict()

    def __init__(self, *args, **kwargs):
        super(StandaloneApplication, self).__init__(*args, **kwargs)
        self.openClient.connect(self._open_widget)


    def _open_widget(self, event_manager, asset_list_model, widgets, event):
        '''Open Adobe widget based on widget name in *event*, and create if not already
        exists'''

        widget_name = None
        widget_class = None
        for (_widget_name, _widget_class, unused_label) in widgets:
            if _widget_name == event['data']['pipeline']['name']:
                widget_name = _widget_name
                widget_class = _widget_class
                break
        if widget_name:
            ftrack_client = widget_class
            widget = None
            if widget_name in self.created_widgets:
                widget = self.created_widgets[widget_name]
                # Is it still visible?
                is_valid_and_visible = False
                try:
                    if widget is not None and widget.isVisible():
                        is_valid_and_visible = True
                except:
                    pass
                finally:
                    if not is_valid_and_visible:
                        del self.created_widgets[widget_name]  # Not active any more
                        if widget:
                            try:
                                widget.deleteLater()  # Make sure it is deleted
                            except:
                                pass
                            widget = None
            if widget is None:
                # Need to create
                if widget_name in [
                    qt_constants.ASSEMBLER_WIDGET,
                    core_constants.ASSET_MANAGER,
                ]:
                    # Create with asset model
                    widget = ftrack_client(event_manager, asset_list_model)
                else:
                    # Create without asset model
                    widget = ftrack_client(event_manager)
                self.created_widgets[widget_name] = widget
            widget.show()
            widget.raise_()
            widget.activateWindow()
        else:
            raise Exception(
                'Unknown widget {}!'.format(event['data']['pipeline']['name'])
            )


# Init QApplication
app = StandaloneApplication()


def get_ftrack_menu(menu_name='ftrack', submenu_name=None):
    '''Get the current ftrack menu, create it if does not exists.'''
    # TODO: We will send and event to photoshop to return the ftrack menu
    # gMainWindow = mm.eval('$temp1=$gMainWindow')
    #
    # if cmds.menu(menu_name, exists=True, parent=gMainWindow, label=menu_name):
    #     menu = menu_name
    #
    # else:
    #     menu = cmds.menu(
    #         menu_name, parent=gMainWindow, tearOff=True, label=menu_name
    #     )

    # if submenu_name:
        # if cmds.menuItem(
        #     submenu_name, exists=True, parent=menu, label=submenu_name
        # ):
        #     submenu = submenu_name
        # else:
        #     submenu = cmds.menuItem(
        #         submenu_name, subMenu=True, label=submenu_name, parent=menu
        #     )
    #     return submenu
    # else:
    #     return menu
    pass


def _open_widget_async(event_manager, asset_list_model, widgets, event):
    app.openClient.emit(event_manager, asset_list_model, widgets, event)


def initialise(adobe_id):

    logger.debug('Setting up the menu')
    session = ftrack_api.Session(auto_connect_event_hub=False)

    event_manager = event.QEventManager(
        session=session, mode=core_constants.LOCAL_EVENT_MODE
    )

    host = adobe_host.AdobeHost(event_manager)

    # Shared asset manager model
    asset_list_model = AssetListModel(event_manager)

    widgets = list()
    widgets.append(
        (
            core_constants.OPENER,
            ftrack_open.AdobeQtOpenerClientWidget,
            'Open',
        )
    )
    widgets.append(
        (
            qt_constants.ASSEMBLER_WIDGET,
            load.AdobeQtAssemblerClientWidget,
            'Assembler',
        )
    )
    widgets.append(
        (
            core_constants.ASSET_MANAGER,
            asset_manager.AdobeQtAssetManagerClientWidget,
            'Asset Manager',
        )
    )
    widgets.append(
        (
            core_constants.PUBLISHER,
            publish.AdobeQtPublisherClientWidget,
            'Publisher',
        )
    )
    widgets.append(
        (
            qt_constants.CHANGE_CONTEXT_WIDGET,
            change_context.AdobeQtChangeContextClientWidget,
            'Change context',
        )
    )
    widgets.append(
        (
            core_constants.LOG_VIEWER,
            log_viewer.AdobeQtLogViewerClientWidget,
            'Log Viewer',
        )
    )
    widgets.append(
        (
            qt_constants.DOCUMENTATION_WIDGET,
            documentation.QtDocumentationClientWidget,
            'Documentation',
        )
    )

    ftrack_menu = get_ftrack_menu()
    # Register and hook the dialog in ftrack menu
    # for item in widgets:
        # if item == 'divider':
        #     cmds.menuItem(divider=True)
        #     continue
        #
        # widget_name, unused_widget_class, label, image = item
        #
        # cmds.menuItem(
        #     parent=ftrack_menu,
        #     label=label,
        #     command=(functools.partial(host.launch_client, widget_name)),
        #     image=":/{}.png".format(image),
        # )

    # Listen to widget launch events
    session.event_hub.subscribe(
        'topic={} and data.pipeline.host_id={}'.format(
            core_constants.PIPELINE_CLIENT_LAUNCH, host.host_id
        ),
        functools.partial(
            _open_widget_async, event_manager, asset_list_model, widgets
        ),
    )

    remote_event_manager = adobe_utils.init_adobe(adobe_id)
    host.remote_events_listener(remote_event_manager, adobe_id)


def on_exit():
    logger.info('Adobe pipeline exit')

atexit.register(on_exit)

adobe_id = os.environ['FTRACK_ADOBE_SESSION_ID']

try:
    initialise(adobe_id)
except:
    import traceback
    logger.warning(traceback.format_exc())

# Run until it's closed
sys.exit(app.exec_())