

from pxr import UsdGeom


class PrimFactory:
    @staticmethod
    def create_prim(stage, prim_type,path):
        if prim_type == "Sphere":
            return UsdGeom.Sphere.Define(stage,path)
        elif prim_type == "Cube":
            return UsdGeom.Cube.Define(stage,path)
        elif prim_type == "Xform":
            return UsdGeom.Xform.Define(stage,path)
        else:
            raise ValueError(f"Unsupported prim type:{prim_type}")

    @staticmethod
    def get_attr_setter(prim, attr_name):
        # Map generic attribute names to schema specific methods
        type_to_attr_map  = {

            "Sphere":{
                "radius": lambda: prim.GetRadiusAttr
            },
            "Cube":{
                "size" : lambda: prim.GetSizeAttr
            },
            "Xform":{
                "xformOpOrder" : lambda :prim.GetXformOpOrderAttr
            },
        }
        type_name = prim.GetPrim().GetTypeName()
        attr_map = type_to_attr_map.get(type_name,{})
        getter_func = attr_map.get(attr_name)
        if not getter_func:
            raise AttributeError(f"{prim.GetPrim().GetTypeName()} does not support attribute '{attr_name}'")
        return getter_func()