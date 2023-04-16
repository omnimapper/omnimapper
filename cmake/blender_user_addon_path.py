import os
import subprocess

blender_output = subprocess.check_output(['blender', '-b', '--python-expr', 'import bpy; print("".join(["blender_user_addon_path=", bpy.utils.user_resource("SCRIPTS", path="addons")]))']).decode('utf-8')
addon_path_line = [line for line in blender_output.split('\n') if line.startswith('blender_user_addon_path=')][0]

print(addon_path_line.replace('blender_user_addon_path=', ''))
