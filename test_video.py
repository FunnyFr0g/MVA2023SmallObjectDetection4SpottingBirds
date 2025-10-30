import cv2
import mmcv
from mmdet.apis import inference_detector, init_detector, show_result_pyplot

# Конфигурация и веса модели
config_file = 'configs/mva2023_baseline_copy/simple_cfg.py'
checkpoint_file = 'work_dirs/centernet_resnet18_140e_coco_hard_negative_training/latest.pth'

# Инициализация модели
model = init_detector(config_file, checkpoint_file, device='cuda:0')  # или 'cpu'

# Входное и выходное видео
video_path = 'data/2025-06-05 14-31-20.mp4'
output_video = 'data/output.mp4'

video = mmcv.VideoReader(video_path)

# Настройки выходного видео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, video.fps, (video.width, video.height))

# Параметры обработки
frame_skip = 0  # Пропуск кадров (0 = обрабатывать все)
show_ui = False  # Показывать ли окно с результатом
score_thr = 0.2  # Порог уверенности

# Главный цикл обработки
for i, frame in enumerate(mmcv.track_iter_progress(video)):
    if i % (frame_skip + 1) != 0:
        continue
        
    # Детекция
    result = inference_detector(model, frame)
    
    # Визуализация
    vis_frame = model.show_result(
        frame, 
        result, 
        score_thr=score_thr,
        show=False
    )
    
    # Сохранение
    out.write(vis_frame)
    
    # Отображение (опционально)
    if show_ui:
        cv2.imshow('Detection', vis_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Завершение
out.release()
if show_ui:
    cv2.destroyAllWindows()
print(f'Обработка завершена. Результат сохранён в {output_video}')