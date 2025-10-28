_base_ = './centernet_resnet18_140e_coco.py'
data_root = 'data/'

data = dict(
    test=dict(
        samples_per_gpu=4,
        ann_file='/root/mva23/MVA2023SmallObjectDetection4SpottingBirds/anns/empty_val_annotations.json',
        img_prefix='/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/images/val/',
    ) 
)

