from PIL import Image
import os

# Kaynak görüntünün yolu
input_path = "small_10x10.pgm"  # buraya kendi dosya adını yaz
image = Image.open(input_path)

# Hedef çözünürlükler (en boy oranı korunur)
resolutions = {
    "8k": (7680, 4320),
    "16k": (15360, 8640),
    "32k": (30720, 17280),
    "64k": (61440, 34560)
}

# Çıktı klasörü
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# Her çözünürlük için yeniden boyutlandırma
for label, (width, height) in resolutions.items():
    try:
        resized = image.resize((width, height), Image.LANCZOS)
        output_path = os.path.join(output_dir, f"image_{label}.png")
        resized.save(output_path)
        print(f"{label} çözünürlüklü görsel oluşturuldu: {output_path}")
    except Exception as e:
        print(f"{label} için hata oluştu: {e}")