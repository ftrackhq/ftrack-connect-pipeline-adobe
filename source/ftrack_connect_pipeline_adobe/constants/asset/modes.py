# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

from ftrack_connect_pipeline_adobe.utils import custom_commands as adobe_utils

# Load Modes
IMPORT_MODE = 'import'
REFERENCE_MODE = 'reference'
OPEN_MODE = 'open'

LOAD_MODES = {
    OPEN_MODE: adobe_utils.open_file,
    IMPORT_MODE: adobe_utils.import_file,
    REFERENCE_MODE: adobe_utils.reference_file,
}
