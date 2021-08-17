import paddlex as pdx


class HandDet():
    def __init__(self, params_path):
        self.model = pdx.load_model(params_path)

    def infer(self, img_path):
        result = self.model.predict(img_path)
        # TODO: 改为返回值的
        pdx.det.visualize(img_path, result, threshold=0.5, save_dir='./output/ppyolotiny')