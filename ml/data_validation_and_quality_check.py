import os
from pathlib import Path
from PIL import Image
import numpy as np

# Папка с обработанными фото
PROCESSED_DIR = Path("C:\\Users\\79616\\master-2025-team-2-0\\processed_images")

IMG_SIZE = (512, 512)
EXPECTED_FORMAT = "JPEG"

def validate_images():
    issues = []
    files = [f for f in os.listdir(PROCESSED_DIR) if f.lower().endswith(".jpg")]
    files.sort(key=lambda x: int(Path(x).stem))

    for idx, file in enumerate(files, start=1):
        expected_name = f"{idx}.jpg"
        if file != expected_name:
            issues.append((file, f"Ожидалось имя {expected_name}"))

    for file in files:
        path = PROCESSED_DIR / file
        try:
            img = Image.open(path)
            if img.mode != "RGB":
                issues.append((file, f"Неверный цветовой режим: {img.mode}"))
            if img.size != IMG_SIZE:
                issues.append((file, f"Неверный размер: {img.size}"))
            arr = np.array(img)
            if arr.min() == arr.max():
                issues.append((file, "Изображение однотонное"))
        except Exception as e:
            issues.append((file, f"Ошибка при чтении: {e}"))

    return issues

if __name__ == "__main__":
    problems = validate_images()
    if problems:
        print("[WARNING] Проблемы:")
        for p in problems:
            print(" -", p)
    else:
        print("[OK] Все изображения прошли валидацию и проверки качества")
