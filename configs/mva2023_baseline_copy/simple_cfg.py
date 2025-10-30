# Упрощённый конфиг для инференса (только модель и runtime)
_base_ = './centernet_resnet18_140e_coco_inference.py'

model = dict(
    bbox_head=dict(
        num_classes=1,  
        test_cfg=dict(score_thr=0.3)  
    )
)