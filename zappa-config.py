#!/usr/bin/env python

import os
import json

MANDATORY_VARS = [
    'ZAPPA_REGION',
    'ZAPPA_DJANGO_SETTINGS',
    'ZAPPA_PROJECT_NAME',
    'ZAPPA_S3_BUCKET',
]

ZAPPA_SETTINGS_FILE = 'zappa_settings.json'


def write_zappa_config():
    missing_vars = []
    for var_name in MANDATORY_VARS:
        if not os.environ.get(var_name):
            missing_vars.append(var_name)

    if missing_vars:
        raise Exception('Missing mandatory var(s): %s' % ', '.join(missing_vars))

    zappa_config_dict = {
        'dev': {
            'aws_region': os.environ.get('ZAPPA_REGION'),
            'django_settings': os.environ.get('ZAPPA_DJANGO_SETTINGS'),
            'runtime': 'python3.6',
            's3_bucket': os.environ.get('ZAPPA_S3_BUCKET')
        }
    }

    with open(ZAPPA_SETTINGS_FILE, 'w') as fh:
        fh.write(json.dumps(zappa_config_dict, indent=4))
    fh.close()


if __name__ == "__main__":
    if not os.path.isfile(ZAPPA_SETTINGS_FILE):
        write_zappa_config()
