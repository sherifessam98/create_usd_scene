class Inspector:
    @staticmethod
    def print_prim_hierarchy(stage):
        def recurse(prim, indent=0):
            print(" " * indent + prim.GetName())
            for child in prim.GetChildren():
                recurse(child, indent + 1)
        recurse(stage.GetPseudoRoot())

    @staticmethod
    def print_layer_stack(stage):
        print("Layer Stack:")
        for layer in stage.GetLayerStack():
            print(' -', layer.identifier)