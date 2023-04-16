import shutil
import datetime
import os
import glob
import sys

extension = sys.argv[1]

os.makedirs("timestamped", exist_ok=True)

files_to_delete = glob.glob("timestamped/omnimappercpp-t*")

if files_to_delete:
	os.remove(*files_to_delete)

shutil.copy(''.join(['omnimappercpp', extension]), ''.join(['timestamped/omnimappercpp-t', str(datetime.datetime.now().timestamp()), extension]))
