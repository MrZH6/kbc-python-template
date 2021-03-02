'''
Template Component main class.

'''

import logging
# import os
import sys
# from pathlib import Path

from keboola.component import CommonInterface

# configuration variables
KEY_API_TOKEN = '#api_token'
KEY_PRINT_HELLO = 'print_hello'

# #### Keep for debug
KEY_DEBUG = 'debug'

# list of mandatory parameters => if some is missing,
# component will fail with readable message on initialization.
REQUIRED_PARAMETERS = [KEY_DEBUG]
REQUIRED_IMAGE_PARS = []

APP_VERSION = '0.0.1'


# class Component(KBCEnvHandler):
#
#     def __init__(self, debug=False):
#         # for easier local project setup
#         default_data_dir = Path(__file__).resolve()
#         .parent.parent.joinpath('data').as_posix() \
#             if not os.environ.get('KBC_DATADIR') else None
#
#         KBCEnvHandler.__init__(self, MANDATORY_PARS,
#         log_level=logging.DEBUG if debug else logging.INFO,
#                                data_path=default_data_dir)
#         # override debug from config
#         if self.cfg_params.get(KEY_DEBUG):
#             debug = True
#         if debug:
#             logging.getLogger().setLevel(logging.DEBUG)
#         logging.info('Running version %s', APP_VERSION)
#         logging.info('Loading configuration...')
#
#         try:
#             # validation of mandatory parameters. Produces ValueError
#             self.validate_config(MANDATORY_PARS)
#             self.validate_image_parameters(MANDATORY_IMAGE_PARS)
#         except ValueError as e:
#             logging.exception(e)
#             exit(1)
#         # ####### EXAMPLE TO REMOVE
#         #         # intialize instance parameteres
#         #
#         #         # ####### EXAMPLE TO REMOVE END
#
#     def run(self):
#         '''
#         Main execution code
#         '''
#         params = self.cfg_params  # noqa
#
#         # ####### EXAMPLE TO REMOVE
#         if params.get(KEY_PRINT_HELLO):
#             logging.info("Hello World")
#
#         # ####### EXAMPLE TO REMOVE END


"""
        Main entrypoint
"""
if __name__ == "__main__":
    if len(sys.argv) > 1:
        debug_arg = sys.argv[1]
    else:
        debug_arg = False
    try:
        # initialize the library
        ci = CommonInterface()

        # ci = CommonInterface(data_folder_path='../data')

        # Checks for required parameters and
        # throws ValueError if any is missing.
        ci.validate_configuration(REQUIRED_PARAMETERS)

        # print KBC Project ID from the environment variable if present:
        logging.info(ci.environment_variables.project_id)

        # comp = Component(debug_arg)
        # comp.run()
        print("Running")
    except Exception as exc:
        logging.exception(exc)
        exit(1)
