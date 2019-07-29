class CLAHE(object):
    def __init__(self, clip_limit):
        assert isinstance(clip_limit, float) or isinstance(clip_limit, int)
        self.clip_limit = clip_limit
    
    def __call__(self, sample):
        image, diagnosis = sample['image'], sample['diagnosis']
        
        clahe = cv2.createCLAHE(clipLimit=self.clip_limit)
        img = clahe.apply(image)
        return {"image": img, "diagnosis": diagnosis}