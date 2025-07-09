from typing import override

from pxr import Usd , Sdf

class LayerManager:
    def __init__(self,base_layer_path, override_layer_path):
        # New Layer with override
        self.root_layer = Sdf.Layer.CreateNew(override_layer_path)
        # base layer with original values
        self.base_layer = Sdf.Layer.FindOrOpen(base_layer_path)
        # making the override layer see the base layer and potentially override its data
        self.root_layer.subLayerPaths.append(self.base_layer.identifier)

    def get_composed_stage(self):
        return Usd.Stage.Open(self.root_layer)

    def save(self):
        self.root_layer.Save()

