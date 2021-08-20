import paddlex as pdx
from paddlex import transforms as T


transforms = T.Compose([
    T.ResizeByShort(short_size=256), T.CenterCrop(crop_size=224), T.Normalize()
])

class HandClas():
    def __init__(self, params_path):
        self.model = pdx.load_model(params_path)

    def get_clas(self, img):
        result = self.model.predict(img, topk=5, transforms=transforms)
        return result