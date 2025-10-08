from set_lib_dir import LIB_ROOT_DIR
import os
_base_ = './centernet_resnet18_140e_coco.py'
data_root = LIB_ROOT_DIR + '/data/'


data = dict(
    train=dict(
        ann_file='/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/train_annotations.json',
        img_prefix='/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/images/train/',
        ),
    val=dict(
        ann_file='/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/val_annotations.json',
        img_prefix='/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/images/val/',
       ),
    test=dict(
        ann_file='/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/val_annotations.json',
        img_prefix='/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/images/val/',
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
