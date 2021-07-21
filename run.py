import os
from check_goods import check_obsolete,convert_to_json

file_path = os.path.dirname(os.path.realpath('__file__'))

df = check_obsolete(os.path.join(file_path,'python hands-on - dataset.csv'))
convert_to_json(df, 'obsolete',file_path)