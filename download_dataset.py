from clearml import Task, Dataset



from clearml import Dataset
import os
import shutil


print('Скачиваем датасет')

dataset_folder = p = Dataset.get(dataset_id="ae8c12c33b324947af9ae6379d920eb8").get_local_copy()

print(f"Датасет скачан в: {dataset_folder}")

# Копируем в нужную папку репозитория
# target_folder = r"/root/mva23/MVA2023SmallObjectDetection4SpottingBirds/data/drones_only"  
# if os.path.exists(target_folder):
#     shutil.rmtree(target_folder)  

# shutil.copytree(dataset_folder, target_folder)
# print(f"Датасет перемещен в: {target_folder}")