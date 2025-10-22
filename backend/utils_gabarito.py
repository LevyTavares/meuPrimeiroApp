"""
Utilitários para geração de gabaritos em PNG
Adaptado do código fornecido
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os
from datetime import datetime

def generate_gabarito_png(
    filename: str = "gabarito.png",
    num_questions: int = 50,
    choices: tuple = ("A", "B", "C", "D", "E"),
    margin: int = 50,
    spacing_y: int = 20,
    bubble_diameter: int = 20,
    title: str = "GABARITO - PROVA",
    subtitle: str = "Nome: _________________________   Numero: ____   Turma: ______",
    font_path: str = None
) -> str:
    """
    Gera um gabarito em PNG com bolhas para preenchimento
    
    Args:
        filename: nome do arquivo de saída
        num_questions: número de questões
        choices: alternativas disponíveis
        margin: margem em pixels
        spacing_y: espaçamento vertical
        bubble_diameter: diâmetro das bolhas
        title: título do gabarito
        subtitle: subtítulo/instruções
        font_path: caminho para fonte TTF customizada
    
    Returns:
        Caminho do arquivo gerado
    """
    
    try:
        if font_path is None:
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        
        if not os.path.exists(font_path):
            # Fallback para Windows/Mac
            font_path = None
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            q_font = ImageFont.load_default()
            choice_font = ImageFont.load_default()
        else:
            title_font = ImageFont.truetype(font_path, 80)
            subtitle_font = ImageFont.truetype(font_path, 48)
            q_font = ImageFont.truetype(font_path, 36)
            choice_font = ImageFont.truetype(font_path, 48)
    except Exception:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        q_font = ImageFont.load_default()
        choice_font = ImageFont.load_default()

    # Calcular layout
    if num_questions > 10:
        columns = num_questions // 10
    else:
        columns = 1

    rows_per_col = math.ceil(num_questions / columns)
    page_size = (1240, 877)

    # Criar imagem
    img = Image.new("RGB", page_size, "white")
    draw = ImageDraw.Draw(img)

    w, h = page_size
    draw.text((margin, margin//2), title, font=title_font, fill="black")
    
    top = margin + 15
    bottom = h - margin
    usable_height = bottom - top
    col_width = (w - 2*margin) / columns
    row_height = min(spacing_y + bubble_diameter, usable_height / rows_per_col)

    q = 1
    for col in range(columns):
        x0 = margin + col * col_width
        x_question_num = x0
        
        temp_bbox = draw.textbbox((0, 0), f"{q:02d}.", font=q_font)
        q_text_width = temp_bbox[2] - temp_bbox[0]
        x_choices_start = x_question_num + q_text_width + 10

        for row in range(rows_per_col):
            if q > num_questions:
                break
            
            y = int(top + row * row_height)
            draw.text((x_question_num, y), f"{q:02d}.", font=q_font, fill="black")
            
            # Desenhar bolhas
            for i, ch in enumerate(choices):
                cx = int(x_choices_start + i * (bubble_diameter + 20))
                cy = int(y + (bubble_diameter/4) - bubble_diameter/2)
                
                # Desenhar círculo
                draw.ellipse(
                    [cx, cy, cx + bubble_diameter, cy + bubble_diameter],
                    outline="black",
                    width=1
                )
                
                # Adicionar letra
                bbox = draw.textbbox((0, 0), ch, font=choice_font)
                w_ch = bbox[2] - bbox[0]
                h_ch = bbox[3] - bbox[1]
                
                tx = cx + (bubble_diameter - w_ch) / 2
                ty = cy + (bubble_diameter - h_ch) / 2 - 1
                draw.text((tx, ty), ch, font=choice_font, fill="black")
            
            q += 1

    # Adicionar footer
    footer_text = "Assinale apenas uma opcao por questao. Use caneta preta ou azul."
    draw.text((w - margin - 500, h - margin - 15), subtitle, font=subtitle_font, fill="black")
    draw.text((w - margin - 500, h - margin), footer_text, font=subtitle_font, fill="black")

    # Salvar com qualidade
    img.save(filename, dpi=(300, 300))
    return filename

def create_gabaritos_directory():
    """Criar diretório para armazenar gabaritos gerados"""
    directory = "gabaritos_gerados"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

# Exemplo de uso
if __name__ == "__main__":
    gabarito_dir = create_gabaritos_directory()
    filename = os.path.join(gabarito_dir, f"gabarito_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    result = generate_gabarito_png(
        filename=filename,
        num_questions=50,
        title="GABARITO - PROVA DE MATEMÁTICA"
    )
    print(f"Gabarito gerado: {result}")
