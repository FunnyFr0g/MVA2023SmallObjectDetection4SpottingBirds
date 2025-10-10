_base_ = './centernet_resnet18_140e_coco.py'
data_root = 'data/'

data = dict(
    test=dict(
        samples_per_gpu=4,
        ann_file='/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/train_annotations_class0.json',
        img_prefix='/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/images/train/',
    ) 
)

