import json



def update_coco_files(file_paths):
    """
    Обновляет COCO JSON файлы:
    1. Заменяет category_id с 1 на 0
    2. Изменяет нумерацию изображений и аннотаций начинаться с 0
    
    Args:
        file_paths: список кортежей (input_file, output_file)
    """
    
    for input_file, output_file in file_paths:
        try:
            # Читаем JSON файл
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Счетчики изменений
            annotations_updated = 0
            categories_updated = 0
            images_renumbered = 0
            annotations_renumbered = 0
            
            # Создаем словари для переиндексации
            image_id_mapping = {}
            annotation_id_mapping = {}
            
            # 1. Обновляем нумерацию изображений (начинаем с 0)
            if 'images' in data:
                for new_id, image in enumerate(data['images']):
                    old_id = image['id']
                    image_id_mapping[old_id] = new_id
                    image['id'] = new_id
                    images_renumbered += 1
            
            # 2. Обновляем category_id в categories
            if 'categories' in data:
                for category in data['categories']:
                    if category.get('id') == 1:
                        category['id'] = 0
                        categories_updated += 1
            
            # 3. Обновляем нумерацию аннотаций и category_id
            if 'annotations' in data:
                for new_id, annotation in enumerate(data['annotations']):
                    # Обновляем id аннотации
                    old_annotation_id = annotation['id']
                    annotation_id_mapping[old_annotation_id] = new_id
                    annotation['id'] = new_id
                    annotations_renumbered += 1
                    
                    # Обновляем category_id
                    if annotation.get('category_id') == 1:
                        annotation['category_id'] = 0
                        annotations_updated += 1
                    
                    # Обновляем image_id в аннотациях согласно новой нумерации
                    if annotation.get('image_id') in image_id_mapping:
                        annotation['image_id'] = image_id_mapping[annotation['image_id']]
            
            # Сохраняем обновленный файл
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"Файл: {input_file} -> {output_file}")
            print(f"  Category_id обновлено: {annotations_updated} аннотаций, {categories_updated} категорий")
            print(f"  Изображений перенумеровано: {images_renumbered}")
            print(f"  Аннотаций перенумеровано: {annotations_renumbered}")
            print(f"  Всего изображений: {len(data.get('images', []))}")
            print(f"  Всего аннотаций: {len(data.get('annotations', []))}")
            
        except Exception as e:
            print(f"Ошибка при обработке файла {input_file}: {e}")


# Пример использования
if __name__ == "__main__":
    # Укажите пути к вашим файлам
    input_file1 = "/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/train_annotations.json" 
    input_file2 = "/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/val_annotations.json"  
    output_file1 = "/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/train_annotations_class0.json"  
    output_file2 = "/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/val_annotations_class0.json"  

    files2process = [
        (input_file1, output_file1),
        (input_file2, output_file2)
    ]
    
    update_coco_files(files2process )
    print("Оба файла успешно обработаны!")