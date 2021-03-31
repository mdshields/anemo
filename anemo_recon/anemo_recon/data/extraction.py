import glob
import os
import sys
from pathlib import Path
from collections import OrderedDict
import pandas as pd
from datetime import datetime
import re

def mk_temp_dir(kind):
    if not os.path.exists('temp'):
        print('Adding temp folder.')
        os.makedirs('temp')
    if not os.path.exists(f'temp/{kind}'):
        print(f'Adding temp {kind} folder.')
        os.makedirs(f'temp/{kind}')