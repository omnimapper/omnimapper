import ctypes
import glob
import os
import sys

bl_info = {
	"name": "omnimapper",
	"blender": (2, 80, 0),
	"category": "Object",
}

def loadmodule():
	if os.environ.get('OMNIMAPPER_DEV') == '1':
		newest_so = max(glob.glob(''.join([os.path.dirname(__file__), '/omnimappercpp-t*'])), key=os.path.getctime)
		so = ctypes.PyDLL(newest_so)
	else:
		so = ctypes.PyDLL('omnimappercpp')

	so.PyInit_omnimappercpp.argtypes = []
	so.PyInit_omnimappercpp.restype = ctypes.py_object
	return so.PyInit_omnimappercpp()

omnimappercpp = loadmodule()

def register():
	omnimappercpp.register()

def unregister():
	omnimappercpp.unregister()
