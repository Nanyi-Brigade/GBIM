import paddlex as pdx


class HandClas():
    def __init__(self, params_path):
        self.model = pdx.load_model(params_path)

    def get_clas(self, img):
        result = model.predict(img)
        return result