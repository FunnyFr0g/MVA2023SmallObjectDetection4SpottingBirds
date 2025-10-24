from clearml import Task

task = Task.get_task(task_id='defc556e31e8404184ecdfa0ed4dd9cb')

task.started()

task.upload_artifact(
    name='finetuning work dir',
    artifact_object='/root/mva23/MVA2023SmallObjectDetection4SpottingBirds/work_dirs/centernet_resnet18_140e_coco_finetune'
)
print('Артефакт загружен')

task.mark_completed()