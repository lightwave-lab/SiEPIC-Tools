''' SiEPIC tools

    Batch mode compiling is useful for server side compile.
    It does not launch a GUI. It needs a -b flag.
    Also, SiEPIC tools utils.py will check for an environment variable to prevent any Qt functions from being called.

    To run without GUI in batch mode::

        export KLAYOUT_BATCH_MODE=1
        klayout -b -e -r your_mask.py $(FLAGS)

    To run with GUI (default behavior)::

        export KLAYOUT_BATCH_MODE=0
        klayout -e -r your_mask.py $(FLAGS)

    or just don't set this environment variable.
'''

__version__ = '0.3.38'
#from . import install, extend, _globals, core, examples, github, lumerical, scripts, utils, setup
from . import install, extend, _globals, core, examples, github, scripts, utils, setup
