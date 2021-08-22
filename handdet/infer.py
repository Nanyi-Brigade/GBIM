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

    def get_hand(self, img):
        bbox = self._infer(img)
        hand_img = None
        vis_img = img.copy()
        if len(bbox) != 0 and img is not None:
            if bbox[0]["score"] >= self.threshold:
                hand_img = self._clip_img_by_bbox(img, bbox)
                vis_img = pdx.det.visualize(vis_img, bbox, save_dir=None)
        return hand_img, vis_img

    def _infer(self, img):
        result = self.model.predict(img, transforms=transforms)
        bbox = self._get_max(result)
        return bbox
    
    # 只获取一个最大可能的手
    def _get_max(self, bboxs):
        if len(bboxs) == 0:
            return []
        max_bbox = bboxs[0]
        max_score = max_bbox["score"]
        for bbox in bboxs:
            if bbox["score"] > max_score:
                max_bbox = bbox
        return [max_bbox]

    # 根据bbox裁剪图像
    def _clip_img_by_bbox(self, img, bbox):
        x, y, w, h = bbox[0]["bbox"]
        hand = img[int(y): int(y + h), int(x): int(x + w), :]
        return hand