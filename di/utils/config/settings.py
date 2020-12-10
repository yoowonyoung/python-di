import json
import os

"""
How to use settings 
1. import sourcecode
from codegrok.indexer.utils.config.settings import config
2. use json(dict)
 config['LOG_PATH']
"""

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(FILE_DIR, '..', '..', '..', 'data', 'logger', 'config.json')

with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)
    config = {key: os.getenv(key) if os.getenv(key) else config[key] for key in config.keys()}
