import bpy
import subprocess


class WM_OT_Restart(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "wm.restart_blender"
    bl_label = "Restart Blender"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        file_path = bpy.data.filepath
        binary_path = bpy.app.binary_path

        process = subprocess.Popen([binary_path, file_path])
        bpy.ops.wm.quit_blender()
        return {'FINISHED'}


def wm_operator(self, context): 
    self.layout.operator("wm.restart_blender", icon='FILE_REFRESH')

def register():
    bpy.utils.register_class(WM_OT_Restart)
    bpy.types.INFO_MT_file.append(wm_operator)


def unregister():
    bpy.utils.unregister_class(WM_OT_Restart)
    bpy.types.INFO_MT_file.remove(wm_operator)


register()
