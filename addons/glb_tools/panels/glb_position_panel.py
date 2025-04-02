import bpy
from ..utils import get_glb_position, get_glb_rotation, get_polygon_count

class VIEW3D_PT_glb_position(bpy.types.Panel):
    bl_label = "GLB Position"
    bl_idname = "VIEW3D_PT_glb_position"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'GLB Tools'

    def draw(self, context):
        layout = self.layout
        obj = context.active_object

        if obj:
            # Object Name
            layout.label(text=f"Object: {obj.name}")
            
            # Polygon Count
            poly_count = get_polygon_count(obj)
            layout.label(text=f"Polygons: {poly_count:,}")
            
            # Position
            layout.label(text="GLB Position:")
            glb_pos = get_glb_position(obj)
            layout.label(text=f"X: {glb_pos.x:.6f}")
            layout.label(text=f"Y: {glb_pos.y:.6f}")
            layout.label(text=f"Z: {glb_pos.z:.6f}")
            
            # Rotation
            layout.label(text="GLB Rotation (radians):")
            glb_rot = get_glb_rotation(obj)
            layout.label(text=f"X: {glb_rot.x:.6f}")
            layout.label(text=f"Y: {glb_rot.y:.6f}")
            layout.label(text=f"Z: {glb_rot.z:.6f}")
            
            # Copy Buttons
            layout.operator("object.copy_glb_position")
            layout.operator("object.copy_glb_rotation")
            layout.operator("object.copy_r3f_transform")
        else:
            layout.label(text="No object selected") 
            
        # Add separator before export button
        layout.separator()
        # Export JSON Button - make more prominent
        box = layout.box()
        box.label(text="Export Selected Objects:")
        box.operator("object.export_transforms_json", icon='EXPORT') 