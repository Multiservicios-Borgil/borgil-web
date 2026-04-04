import os
import sys
from PIL import Image, ImageEnhance, ImageOps
try:
    from rembg import remove
except ImportError:
    print("Error: La librería 'rembg' no está instalada.")
    print("Por favor, ejecuta: pip install rembg pillow")
    sys.exit(1)

def procesar_imagen(ruta_entrada, ruta_salida):
    """
    Procesa una imagen de producto: quita fondo, mejora luz/contraste y optimiza para web.
    """
    try:
        print(f"Procesando: {os.path.basename(ruta_entrada)}...")
        
        # 1. Abrir imagen
        img = Image.open(ruta_entrada).convert("RGBA")

        # 2. Quitar fondo con IA (rembg)
        # Esto dejará el producto sobre un fondo transparente
        img_sin_fondo = remove(img)

        # 3. Crear un fondo blanco puro (estilo profesional e-commerce)
        # Algunos prefieren transparencia, pero el blanco es estándar para uniformidad
        fondo_blanco = Image.new("RGBA", img_sin_fondo.size, (255, 255, 255, 255))
        img_final = Image.alpha_composite(fondo_blanco, img_sin_fondo).convert("RGB")

        # 4. Mejorar Brillo y Contraste (para resaltar detalles y taras)
        # Aumentamos un poco el contraste para que los defectos estéticos sean más visibles
        enhancer_contraste = ImageEnhance.Contrast(img_final)
        img_final = enhancer_contraste.enhance(1.15) 
        
        enhancer_brillo = ImageEnhance.Brightness(img_final)
        img_final = enhancer_brillo.enhance(1.05)

        # 5. Nitidez (Sharpening) para ver mejor los detalles
        enhancer_nitidez = ImageEnhance.Sharpness(img_final)
        img_final = enhancer_nitidez.enhance(1.2)

        # 6. Recortar bordes vacíos automáticamente
        # No aplicamos recorte agresivo para mantener el aire alrededor del producto
        
        # 7. Guardar en formato WebP (máxima optimización para tu web)
        nombre_base = os.path.splitext(os.path.basename(ruta_entrada))[0]
        ruta_webp = os.path.join(ruta_salida, f"{nombre_base}_pro.webp")
        
        img_final.save(ruta_webp, "WEBP", quality=85)
        print(f"✓ Guardada como: {os.path.basename(ruta_webp)}")

    except Exception as e:
        print(f"✗ Error al procesar {ruta_entrada}: {e}")

def main():
    # Carpetas por defecto
    input_folder = "fotos_originales"
    output_folder = "fotos_listas_web"

    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"He creado la carpeta '{input_folder}'. Mete ahí tus fotos originales.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    archivos = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not archivos:
        print(f"No hay fotos en '{input_folder}'.")
        return

    print(f"--- Iniciando Procesamiento de {len(archivos)} fotos ---")
    for archivo in archivos:
        ruta_in = os.path.join(input_folder, archivo)
        procesar_imagen(ruta_in, output_folder)
    
    print("\n--- ¡Procesamiento Completado! ---")
    print(f"Encuentra tus fotos listas para la web en: '{output_folder}'")

if __name__ == "__main__":
    main()
