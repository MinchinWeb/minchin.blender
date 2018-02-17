# https://blender.stackexchange.com/a/76124/30060
# https://docs.blender.org/api/blender_python_api_2_78_4/bpy.types.AddonPreferences.html
import sys

import bpy
from bpy.types import AddonPreferences, Operator
from bpy.props import StringProperty

bl_info = {
    "name": "System Python Libaries",
    "author": "William Minchin",
    "description": "Make libraries installed on system Python available to Blender.",
    "version": (0, 1, 0),
    "category": "System",
    "location": "User Preferences > Add-ons > User",
}


class SystemPythonAddonPreferences(AddonPreferences):
    # this must match the add-on name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __name__

    filepath = StringProperty(
            name="System 'site-packages' folder",
            subtype='FILE_PATH',
            )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "filepath")
        layout.label(text="Blender Python is {}".format(sys.version))
        layout.label(text="Restart Blender for changes to take effect.")


def _append_system_python():
    bl_idname = __name__
    addon = bpy.context.user_preferences.addons.get(bl_idname)

    if addon:
        prefs = addon.preferences
        filepath = prefs.filepath
        if filepath:
            sys.path.append(filepath)
            print("Added to Python path: {}".format(filepath))


def register():
    bpy.utils.register_class(SystemPythonAddonPreferences)
    _append_system_python()


def unregister():
    bpy.utils.unregister_class(SystemPythonAddonPreferences)
    print("Sorry, does nothing yet!")


if __name__ == "__main__":
    register()
