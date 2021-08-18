def init_path():
    import sys
    import os.path as ops

    root = ops.dirname(ops.dirname(ops.abspath(__file__)))
    sys.path.append(root)
    return root