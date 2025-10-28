import json
from datetime import datetime

def create_images_only_coco():
    """
    Создает COCO JSON файл только с информацией об изображениях
    """
    
    # УКАЖИТЕ ВАШИ ПУТИ К ФАЙЛАМ ЗДЕСЬ
    input_file = '/clearml_agent_cache/storage_manager/datasets/ds_ae8c12c33b324947af9ae6379d920eb8/val_annotations_class0.json'  # Путь к исходному COCO JSON файлу
    output_file = "/root/mva23/MVA2023SmallObjectDetection4SpottingBirds/anns/empty_val_annotations.json"  # Путь для сохранения нового JSON файла
    
    try:
        # Загружаем исходный COCO файл
        print(f"Загружаем файл: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            coco_data = json.load(f)
        
        # Создаем новую структуру только с изображениями
        new_coco = {
            "info": coco_data.get("info", {}),
            "licenses": coco_data.get("licenses", []),
            "images": coco_data.get("images", []),
            "categories": [{"name": "bird", "supercategory": "bird", "id": 0}],  # Пустой список категорий
        }
        
        # Добавляем информацию о том, что файл был модифицирован
        if "info" in new_coco and new_coco["info"]:
            new_coco["info"]["description"] = "COCO dataset with images only"
            new_coco["info"]["year"] = datetime.now().year
            new_coco["info"]["date_created"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            # Создаем базовую информацию, если её не было
            new_coco["info"] = {
                "description": "COCO dataset with images only",
                "year": datetime.now().year,
                "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        
        # Сохраняем новый файл
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(new_coco, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Успешно создан файл: {output_file}")
        print(f"📊 Статистика:")
        print(f"   - Изображений: {len(new_coco['images'])}")
        print(f"   - Лицензий: {len(new_coco['licenses'])}")
        print(f"   - Категорий: {len(new_coco['categories'])}")
        
    except FileNotFoundError:
        print(f"❌ Ошибка: Файл {input_file} не найден")
        print("   Проверьте путь к файлу и его наличие")
    except json.JSONDecodeError:
        print(f"❌ Ошибка: Файл {input_file} не является валидным JSON")
    except Exception as e:
        print(f"❌ Произошла ошибка: {str(e)}")

# Запуск скрипта
if __name__ == "__main__":
    print("🚀 Запуск создания COCO файла только с изображениями...")
    create_images_only_coco()
    print("✅ Готово!")