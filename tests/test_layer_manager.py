import unittest
import os
from src.core.scene_builder import SceneBuilder
from src.core.layer_manager import LayerManager

class TestLayerManager(unittest.TestCase):
    def setUp(self):
        os.makedirs("usd_scenes",exist_ok=True)
        builder = SceneBuilder("usd_scenes/base.usda")
        builder.add_prim("Xform","/World")
        builder.add_prim("Sphere","/World/Ball",radius=1.0)
        builder.save()

    def test_layer_stack(self):
        lm = LayerManager("usd_scenes/base.usda", "usd_scenes/test_override.usda")
        stage = lm.get_composed_stage()
        layer_paths = [layer.identifier for layer in stage.GetLayerStack()]


        self.assertTrue(

            any("base.usda" in path for path in layer_paths),
            f"Expected base.usda in layer stack. Got:{layer_paths}"
        )

if __name__ == '__main__':
    unittest.main()