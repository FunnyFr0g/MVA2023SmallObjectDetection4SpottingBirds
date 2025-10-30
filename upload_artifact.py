from clearml import Task

task = Task.get_task(task_id='9f2b543b673e40e7839964e053f3e31f')

task.started()

task.upload_artifact(
    name='val predictions json',
    artifact_object='/root/mva23/MVA2023SmallObjectDetection4SpottingBirds/results.bbox.json'
)
print('Артефакт загружен')

task.mark_completed()