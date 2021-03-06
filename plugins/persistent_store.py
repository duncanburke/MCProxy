
AUTHOR = 'ekimekim'
CONTACT = 'mikelang3000@gmail.com'
DESCRIPTION = """A persistent data store for plugins.
Initialise your persistent object with Store(name, default).
name must be unique and identifies your object on disk.
default is the value to take if it does not exist on disk.
All values must be JSONable. That means strings, ints, floats, bools,
lists, tuples, dicts.
No action is required to save data. Data is synced every tick.
If you require a stronger guarentee, you can call sync() to force a sync early.
The top-level object itself must be either a list or a dict.
"""

import simplejson, os

JSON_FILE = 'persistent_data.json'
JSON_FILE_BACKUP = '.persistent_data.json~'


class Store():
	_key = None
	def __init__(self, _key, default):
		global data
		if type(default) not in (list, tuple, dict):
			raise ValueError("Default value must be list, tuple or dict")
		self.__dict__['_key'] = _key
		if _key not in data:
			data[_key] = default
	def __getattr__(self, attr):
		global data
		return getattr(data[self._key], attr)
	def __getitem__(self, item):
		return data[self._key][item]
	def __setattr__(self, attr, value):
		setattr(data[self._key], attr, value)
	def __setitem__(self, item, value):
		data[self._key][item] = value


def on_start():
	global data
	data = simplejson.load(open(JSON_FILE, 'rU'))
	if type(data) != dict:
		raise ValueError("Bad data in json store")


def on_packet(packet, user, to_server):
	return packet


def on_tick():
	sync()


def sync():
	global data
	os.rename(JSON_FILE, JSON_FILE_BACKUP)
	simplejson.dump(data, open(JSON_FILE, 'w'))
