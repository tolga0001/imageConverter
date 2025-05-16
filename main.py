from PIL import Image
import os

# Kaynak görüntünün yolu
input_path = "small_10x10.pgm"
image = Image.open(input_path).convert("L")  # Gri tonlamaya çevir

# Hedef çözünürlükler
resolutions = {
    "8k": (7680, 4320),
    "16k": (15360, 8640),
    "32k": (30720, 17280),
    "64k": (61440, 34560)
}

# Çıktı klasörü
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)


# P2 formatında dosya yazan fonksiyon
def save_as_p2(image, path):
    width, height = image.size
    pixels = list(image.getdata())

    with open(path, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")  # Maksimum grayscale değeri

        # Her satıra width kadar piksel yaz
        for y in range(height):
            row = pixels[y * width:(y + 1) * width]
            f.write(' '.join(map(str, row)) + '\n')


# Her çözünürlük için yeniden boyutlandırma ve kaydetme
for label, (width, height) in resolutions.items():
    try:
        resized = image.resize((width, height), Image.LANCZOS)
        output_path = os.path.join(output_dir, f"image_{label}_P2.pgm")
        save_as_p2(resized, output_path)
        print(f"{label} çözünürlüklü P2 PGM görsel oluşturuldu: {output_path}")
    except Exception as e:
        print(f"{label} için hata oluştu: {e}")
