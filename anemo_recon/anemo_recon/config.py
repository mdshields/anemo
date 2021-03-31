from pathlib import Path
import os
import glob


#df = sns.load_dataset('iris')
#df.to_csv('data/test.csv')


data_dir = Path('../../data')

data_raw = data_dir / 'raw'
data_interim = data_dir / 'interim'
data_processed = data_dir / 'processed'
data_cleaned = data_dir / 'cleaned'

