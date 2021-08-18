import paddlex as pdx


class HandDet():
    def __init__(self, params_path):
        self.model = pdx.load_model(params_path)

    def infer(self, img_path):
        result = self.model.predict(img_path)
        bbox = self.get_max(result)
        # bbox = result
        return pdx.det.visualize(img_path, bbox, threshold=0.7, save_dir=None)
    
    # 只获取一个最大可能的手
    def get_max(self, bboxs):
        if len(bboxs) == 0:
            return []
        max_score = bboxs[0]["score"]
        max_bbox = bboxs[0]
        for bbox in bboxs:
            if bbox["score"] > max_score:
                max_bbox = bbox
        return [max_bbox]