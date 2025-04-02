import bpy


def is_extension():
    # Blender extension package starts with "bl_ext."
    # https://docs.blender.org/manual/en/latest/advanced/extensions/addons.html#extensions-and-namespace
    return str(__package__).startswith("bl_ext.")


# This is a helper base class for you to expand native Blender UI
class ExpandableUi:
    # ID of the target panel.menu to be expanded to
    target_id: str
    # mode of expansion, either "PREPEND" or "APPEND"
    expand_mode: str = "APPEND"

    def draw(self, context: bpy.types.Context):
        raise NotImplementedError("draw method must be implemented")


def reg_order(order_value: int):
    """
    This decorator is used to specify the relative registration order of classes.
    Classes with lower order values will be registered first, and classes without this decorator will be registered last.
    Note that it still respects dependencies between classes. Only classes without dependencies will be sorted by order value.
    Note: For UI classes, updating the order won't take effect in real-time during testing. You need to also update
    the bl_idname of the class to let Blender clean up the drawing cache.
    """

    def class_decorator(cls):
        cls._reg_order = order_value
        return cls

    return class_decorator
