import paddlex as pdx
from paddlex import transforms as T


transforms = T.Compose([
    T.Resize(
        target_size=320, interp='CUBIC'), T.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

class HandDet():
    def __init__(self, params_path, threshold=0.7):
        self.model = pdx.load_model(params_path)
        self.threshold = threshold

    def get_vis(self, img):
        bbox = self._infer(img)
        return pdx.det.visualize(
            img, bbox, threshold=self.threshold, save_dir=None)

    def get_hand(self, img):
        bbox = self._infer(img)
        hand_img = None
        if len(bbox) != 0 and img is not None:
            hand_img = self._clip_img_by_bbox(img, bbox)
        return hand_img

    def _infer(self, img):
        result = self.model.predict(img, transforms=transforms)
        bbox = self._get_max(result)
        return bbox
    
    # 只获取一个最大可能的手
    def _get_max(self, bboxs):
        if len(bboxs) == 0:
            return []
        max_score = bboxs[0]["score"]
        max_bbox = bboxs[0]
        for bbox in bboxs:
            if bbox["score"] > max_score:
                max_bbox = bbox
        return [max_bbox]

    # 根据bbox裁剪图像
    def _clip_img_by_bbox(self, img, bbox):
        x, y, w, h = bbox[0]["bbox"]
        hand = img[int(y): int(y + w), int(x): int(x + h), :]
        return hand