import os
from pathlib import Path
from PIL import Image

# Папка с исходными фото
DATA_DIR = Path(r"C:\Users\79616\master-2025-team-2-0\images")

# Папка для сохранённых обработанных фото
OUTPUT_DIR = Path("C:\\Users\\79616\\master-2025-team-2-0\\processed_images")
OUTPUT_DIR.mkdir(exist_ok=True)

IMG_SIZE = (512, 512)   
IMG_FORMAT = "JPEG"

def preprocess_and_save(img_path, out_path):
    """Приведение изображения к единому формату и размеру"""
    try:
        img = Image.open(img_path).convert("RGB")
        img = img.resize(IMG_SIZE)
        img.save(out_path, format=IMG_FORMAT, quality=95)
        print(f"[OK] {img_path.name} → {out_path.name}")
    except Exception as e:
        print(f"[WARN] Ошибка с {img_path.name}: {e}")

def run_pipeline():
    files = [f for f in os.listdir(DATA_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    files.sort()  

    for idx, file in enumerate(files, start=1):
        img_path = DATA_DIR / file
        out_path = OUTPUT_DIR / f"{idx}.jpg"   
        preprocess_and_save(img_path, out_path)

    print("[DONE] Все изображения обработаны и сохранены в папке processed_images/")

if __name__ == "__main__":
    run_pipeline()
