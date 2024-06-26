# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

import os
import subprocess
import sys
import ftrack_api
import logging
import functools
import traceback

logger = logging.getLogger('ftrack_connect_pipeline_adobe.discover')

plugin_base_dir = os.path.normpath(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
)
python_dependencies = os.path.join(plugin_base_dir, 'dependencies')
sys.path.append(python_dependencies)

def on_discover_pipeline_adobe(session, event):
    try:
        logger.warning("on_discover_pipeline_adobe")

        from ftrack_connect_pipeline_adobe import __version__ as integration_version

        data = {
            'integration': {
                "name": 'ftrack-connect-pipeline-adobe',
                'version': integration_version,
            }
        }

        return data
    except:
        logger.error(traceback.format_exc())

def on_launch_pipeline_adobe(session, event):
    '''Handle application launch and add environment to *event*.'''

    try:
        logger.warning("on_launch_pipeline_adobe")

        pipeline_adobe_base_data = on_discover_pipeline_adobe(session, event)
        adobe_plugins_path = os.path.join(plugin_base_dir, 'resource', 'plug_ins')
        adobe_script_path = os.path.join(plugin_base_dir, 'resource', 'scripts')

        # Discover plugins from definitions
        definitions_plugin_hook = os.getenv("FTRACK_DEFINITION_PLUGIN_PATH")
        plugin_hook = os.path.join(definitions_plugin_hook, 'adobe', 'python')

        import uuid
        adobe_id = '1234'#uuid.uuid4()

        pipeline_adobe_base_data['integration']['env'] = {
            'FTRACK_EVENT_PLUGIN_PATH.prepend': plugin_hook,
            'PYTHONPATH.prepend': os.path.pathsep.join(
                [python_dependencies, adobe_script_path]
            ),
            'FTRACK_ADOBE_SESSION_ID': adobe_id
        }

        selection = event['data'].get('context', {}).get('selection', [])

        if selection:
            task = session.get('Context', selection[0]['entityId'])
            pipeline_adobe_base_data['integration']['env'][
                'FTRACK_CONTEXTID.set'
            ] = task['id']
            parent = session.query(
                'select custom_attributes from Context where id={}'.format(
                    task['parent']['id']
                )
            ).first()  # Make sure updated custom attributes are fetched

        #cmd = 'python "{}/bootstrap.py" {}'.format(adobe_script_path, adobe_id)
        #os.system(cmd)

        #subprocess.Popen(['/bin/bash', '-c', cmd], env=)

        return pipeline_adobe_base_data
    except:
        logger.error(traceback.format_exc())

def register(session):
    '''Subscribe to application launch events on *registry*.'''
    if not isinstance(session, ftrack_api.session.Session):
        return

    logger.warning("Registering adobe")

    handle_discovery_event = functools.partial(
        on_discover_pipeline_adobe, session
    )

    session.event_hub.subscribe(
        'topic=ftrack.connect.application.discover and '
        'data.application.identifier=adobe-*'
        ' and data.application.version >= 2021',
        handle_discovery_event,
        priority=40,
    )

    handle_launch_event = functools.partial(on_launch_pipeline_adobe, session)

    session.event_hub.subscribe(
        'topic=ftrack.connect.application.launch and '
        'data.application.identifier=adobe-*'
        ' and data.application.version >= 2021',
        handle_launch_event,
        priority=40,
    )
