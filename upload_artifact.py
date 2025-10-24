from clearml import Task

task = Task.get_task(task_id='defc556e31e8404184ecdfa0ed4dd9cb')

task.upload_artifact(
    name='finetuning work dir',
    artifact_object='/root/mva23/MVA2023SmallObjectDetection4SpottingBirds/work_dirs'
)
print('Артефакт загружен')