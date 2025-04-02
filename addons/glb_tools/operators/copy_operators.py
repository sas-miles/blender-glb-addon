import bpy
from ..utils import get_glb_position, get_glb_rotation

class OBJECT_OT_copy_glb_position(bpy.types.Operator):
    bl_idname = "object.copy_glb_position"
    bl_label = "Copy Position"
    bl_description = "Copy GLB position to clipboard"

    def execute(self, context):
        obj = context.active_object
        if obj:
            glb_pos = get_glb_position(obj)
            position_string = f"[{glb_pos.x:.6f}, {glb_pos.y:.6f}, {glb_pos.z:.6f}]"
            context.window_manager.clipboard = position_string
            self.report({'INFO'}, "Position copied to clipboard")
        return {'FINISHED'}

class OBJECT_OT_copy_glb_rotation(bpy.types.Operator):
    bl_idname = "object.copy_glb_rotation"
    bl_label = "Copy Rotation"
    bl_description = "Copy GLB rotation to clipboard"

    def execute(self, context):
        obj = context.active_object
        if obj:
            glb_rot = get_glb_rotation(obj)
            rotation_string = f"[{glb_rot.x:.6f}, {glb_rot.y:.6f}, {glb_rot.z:.6f}]"
            context.window_manager.clipboard = rotation_string
            self.report({'INFO'}, "Rotation copied to clipboard")
        return {'FINISHED'}

class OBJECT_OT_copy_r3f_transform(bpy.types.Operator):
    bl_idname = "object.copy_r3f_transform"
    bl_label = "Copy R3F Transform"
    bl_description = "Copy complete React Three Fiber transform"

    def execute(self, context):
        obj = context.active_object
        if obj:
            glb_pos = get_glb_position(obj)
            glb_rot = get_glb_rotation(obj)
            r3f_string = 'position={[' + f'{glb_pos.x:.6f}, {glb_pos.y:.6f}, {glb_pos.z:.6f}' + ']}\n' + \
                        'rotation={[' + f'{glb_rot.x:.6f}, {glb_rot.y:.6f}, {glb_rot.z:.6f}' + ']}'
            context.window_manager.clipboard = r3f_string
            self.report({'INFO'}, "R3F transform copied to clipboard")
        return {'FINISHED'} 