print("20230520")

print("재근")


class OperatorWithFileSelect(bpy.types.Operator):
    bl_idname = "my.fileselector"
    bl_label = ""
    bl_description = "Opens file selector, after executes"
    bl_options = {"REGISTER"}

    filepath = bpy.props.StringProperty(subtype='FILE_PATH')
    filename = bpy.props.StringProperty(subtype='FILE_NAME')
    directory = bpy.props.StringProperty(subtype='DIR_PATH')
    files = bpy.props.CollectionProperty(
        type=bpy.types.OperatorFileListElement)

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        # execute after invoking fileselect
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}wef
