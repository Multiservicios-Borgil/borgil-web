from PIL import Image, ImageChops

def trim(im):
    # Usar el color del primer píxel como fondo (debería ser blanco o transparente)
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    # Aumentar sensibilidad de la diferencia
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

for i in range(4):
    try:
        filename = f'logo_{i+1}.png'
        print(f'Procesando {filename}...')
        img = Image.open(filename)
        trimmed = trim(img)
        # Añadir un pequeño margen de 20px para que no quede pegado al borde
        final_w, final_h = trimmed.size
        margin = 20
        final_img = Image.new(img.mode, (final_w + margin*2, final_h + margin*2), img.getpixel((0,0)))
        final_img.paste(trimmed, (margin, margin))
        final_img.save(f'logo_final_{i+1}.png')
        print(f'Guardado logo_final_{i+1}.png')
    except Exception as e:
        print(f'Error con {filename}: {e}')
