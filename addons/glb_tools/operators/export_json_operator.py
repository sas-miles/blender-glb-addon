import bpy
import json
import os
from bpy_extras.io_utils import ExportHelper
from ..utils import get_glb_position, get_glb_rotation

class OBJECT_OT_export_transforms_json(bpy.types.Operator, ExportHelper):
    bl_idname = "object.export_transforms_json"
    bl_label = "Export Transforms to JSON"
    bl_description = "Export position, rotation, and scale of selected objects to JSON file"
    
    filename_ext = ".json"
    filter_glob: str = bpy.props.StringProperty(
        default="*.json",
        options={'HIDDEN'},
    )
    
    def execute(self, context):
        selected_objects = context.selected_objects
        
        if not selected_objects:
            self.report({'ERROR'}, "No objects selected")
            return {'CANCELLED'}
        
        transforms_data = []
        
        for obj in selected_objects:
            if obj.type != 'MESH':
                continue
                
            glb_pos = get_glb_position(obj)
            glb_rot = get_glb_rotation(obj)
            scale = obj.scale
            
            obj_data = {
                "name": obj.name,
                "position": [glb_pos.x, glb_pos.y, glb_pos.z],
                "rotation": [glb_rot.x, glb_rot.y, glb_rot.z],
                "scale": [scale.x, scale.y, scale.z]
            }
            
            transforms_data.append(obj_data)
        
        # Write data to JSON file
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(transforms_data, f, indent=4)
        
        self.report({'INFO'}, f"Exported transforms for {len(transforms_data)} objects to {self.filepath}")
        return {'FINISHED'} 