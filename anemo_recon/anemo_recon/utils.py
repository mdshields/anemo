import pandas as pd
import numpy as np
import config
from pathlib import Path

def data_loader(path_list):
    df = pd.concat([pd.read_csv(f) for f in path_list])
    df = df.reset_index(drop=True)
    return df

def intify(x):
    if np.isnan(x):
        return 0
    
    try:
        return int(x)
    except:
        return int(x, 0)

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def mk_temp_dir(kind):
    if not os.path.exists(config.data_interim / 'extracted'):
        print('Adding extracted folder.')
        os.makedirs('extracted')
    if not os.path.exists(config.data_interim / 'extracted/{kinde}'):
        print(f'Adding temp {kind} folder.')
        os.makedirs(config.data_interim / f'extracted/{kind}')