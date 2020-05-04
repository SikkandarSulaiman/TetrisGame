import os
import json
from pathlib import Path

config_path = '../config'

for jsonfile in os.listdir(config_path):
	with open(Path(config_path) / jsonfile, 'r') as jf:
		jsondata = json.load(jf)

	for k,v in jsondata.items():
		if type(v) is int or type(v) is list:
			exec(f'{k.upper()} = {v}')
		elif type(v) is str:
			exec(f'{k.upper()} = "{v}"')

input_key_map = dict(zip(list(map(lambda k: ord(k), [KEY_ROTATE, KEY_LEFT, KEY_RIGHT, KEY_DOWN])), [CMD_ROTATE, CMD_LEFT, CMD_RIGHT, CMD_DOWN]))

def singleton(cls):
	objs = {}
	def get_object(*args, **kwargs):
		if cls not in objs:
			objs[cls] = cls(*args, **kwargs)
		return objs[cls]
	return get_object
