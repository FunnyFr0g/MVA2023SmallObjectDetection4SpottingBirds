from set_lib_dir import LIB_ROOT_DIR
import os
_base_ = './centernet_resnet18_140e_coco.py'
data_root = LIB_ROOT_DIR + '/data/'


data = dict(
    train=dict('drones_only/train_annotations.json',
        img_prefix=data_root + 'drones_only/images/train',
    ),
    val=dict(
        ann_file=data_root + 'drones_only/val_annotations.json',
        img_prefix=data_root + 'drones_only/images/val/',
    ),
    test=dict(
        ann_file=data_root + 'drones_only/val_annotations.json',
        img_prefix=data_root + 'drones_only/images/val/',
    )
)

lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=1000,
    warmup_ratio=1.0 / 1000,
    step=[15, 18])
runner = dict(max_epochs=20)
evaluation = dict(interval=20, metric='bbox')
load_from = LIB_ROOT_DIR + '/work_dirs/centernet_resnet18_140e_coco/latest.pth'
checkpoint_config = dict(interval=1)
