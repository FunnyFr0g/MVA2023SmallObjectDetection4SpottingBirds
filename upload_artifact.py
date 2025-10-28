from clearml import Task

task = Task.get_task(task_id='f2a541768d774634845430be688f5a4b')

task.started()

task.upload_artifact(
    name='val predictions json',
    artifact_object='/root/mva23/MVA2023SmallObjectDetection4SpottingBirds/results.bbox.json'
)
print('Артефакт загружен')

task.mark_completed()