HERO_ID = "mmd"

import bpy
import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
export_dir = os.path.join(os.path.dirname(bpy.data.filepath), f"{HERO_ID}_{timestamp}")
os.makedirs(export_dir)

arm = next(obj for obj in bpy.data.objects if (obj.type == 'ARMATURE'))

for action in bpy.data.actions:
    arm.animation_data.action = action
    start, end = map(int, action.frame_range)
    bpy.context.scene.frame_start = start
    bpy.context.scene.frame_end = end

    export_path = os.path.join(export_dir, f"{HERO_ID}@{action.name}.fbx")
    bpy.ops.export_scene.fbx(
        filepath=export_path,
        add_leaf_bones=False,
        use_armature_deform_only=True,
        object_types={'MESH', 'ARMATURE'},
        bake_anim=True,
        bake_anim_use_all_actions=False,
        bake_anim_use_nla_strips=False,
        use_selection=False,
        use_visible=True,
    )