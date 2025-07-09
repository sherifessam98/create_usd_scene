from pxr import Usd, UsdGeom
from .prim_factory import PrimFactory

class SceneBuilder:
    def __init__(self, stage_path):
        self.stage = Usd.Stage.CreateNew(stage_path)
        self.stage_path = stage_path

    def add_prim(self,prim_type, path, **attributes):
        # accepting attributes as a dictionary to be looped over as keyword arguments
        prim = PrimFactory.create_prim(self.stage, prim_type, path)
        for attr_name , attr_value in attributes.items():
            attr = PrimFactory.get_attr_setter(prim,attr_name)()
            attr.Set(attr_value)

    def save(self):
        self.stage.GetRootLayer().Save()

