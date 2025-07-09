from src.core.scene_builder import SceneBuilder
from src.core.layer_manager import LayerManager
from src.core.inspector import Inspector


# Step1: build the scene
builder = SceneBuilder("usd_scene/base.usda")
builder.add_prim("Xform","/World")
builder.add_prim("Sphere","/World/Ball",radius = 1.0)
builder.save()


# Step2: Add Override Layer

layer_mgr = LayerManager("usd_scene/base.usda","usd_scene/override.usda")
stage = layer_mgr.get_composed_stage()
prim = stage.GetPrimAtPath("/World/Ball")
prim.GetAttribute("radius").Set(3.0)
layer_mgr.save()


# Step3: Inspect
Inspector.print_prim_hierarchy(stage)
Inspector.print_layer_stack(stage)