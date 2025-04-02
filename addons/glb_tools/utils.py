import bpy
import mathutils

def get_glb_position(obj):
    """
    Convert Blender object position to GLB coordinate system
    """
    world_matrix = obj.matrix_world
    location = world_matrix.to_translation()
    glb_position = mathutils.Vector((
        location.x,
        location.z,
        -location.y
    ))
    return glb_position

def get_glb_rotation(obj):
    """
    Convert Blender object rotation to GLB coordinate system
    """
    # Get world rotation in radians
    rotation = obj.rotation_euler
    # Convert to GLB coordinate system
    return mathutils.Vector((
        rotation.x,
        rotation.z,
        -rotation.y
    ))

def get_polygon_count(obj):
    """
    Get polygon count of a mesh object
    """
    if obj.type == 'MESH':
        return len(obj.data.polygons)
    return 0 