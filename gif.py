import os
from PIL import Image
import glob

# Список для хранения кадров.
files = glob.glob("gif_frames/*.png")
files.sort(key=os.path.getmtime)
# print(files)
frames = []

for file in files:
    # Открываем изображение каждого кадра.
    frame = Image.open(file)
    # Добавляем кадр в список с кадрами.
    frames.append(frame)
 
# Берем первый кадр и в него добавляем оставшееся кадры.
frames[0].save(
    'rastrigin.gif',
    save_all=True,
    append_images=frames,  # [1:] Срез который игнорирует первый кадр.
    optimize=True,
    duration=20,
    loop=0
)