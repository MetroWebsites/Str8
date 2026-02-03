#!/usr/bin/env python3
"""
Professional STR8 Positive Thinking Design Generator
Creates a clean, godly design with white background and professional colors
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

def create_professional_design():
    # Canvas size (landscape orientation for better layout)
    width, height = 2400, 1600
    
    # Professional godly color palette
    WHITE = (255, 255, 255)
    GOLD = (212, 175, 55)  # Rich gold
    ROYAL_BLUE = (65, 105, 225)  # Royal blue
    DEEP_BLUE = (25, 25, 112)  # Midnight blue
    CREAM = (255, 253, 245)  # Soft cream
    LIGHT_GOLD = (255, 215, 0)  # Bright gold accent
    
    # Create canvas with white background
    canvas = Image.new('RGB', (width, height), WHITE)
    draw = ImageDraw.Draw(canvas)
    
    # Add subtle gradient overlay (cream to white)
    for y in range(height):
        alpha = y / height
        color = tuple(int(WHITE[i] * alpha + CREAM[i] * (1 - alpha)) for i in range(3))
        draw.rectangle([(0, y), (width, y + 1)], fill=color)
    
    # Add elegant border frame
    border_width = 20
    draw.rectangle([border_width, border_width, width - border_width, height - border_width], 
                   outline=GOLD, width=10)
    draw.rectangle([border_width + 15, border_width + 15, width - border_width - 15, height - border_width - 15], 
                   outline=ROYAL_BLUE, width=3)
    
    # Load and prepare classroom images
    classroom_images = []
    for i in range(1, 4):
        try:
            img = Image.open(f'classroom_scene{i}.jpg')
            # Resize to consistent size
            img.thumbnail((400, 300), Image.Resampling.LANCZOS)
            classroom_images.append(img)
        except Exception as e:
            print(f"Could not load classroom_scene{i}.jpg: {e}")
    
    # Position classroom images at the bottom
    if classroom_images:
        spacing = 50
        total_width = sum(img.width for img in classroom_images) + spacing * (len(classroom_images) - 1)
        start_x = (width - total_width) // 2
        y_pos = height - 400
        
        for idx, img in enumerate(classroom_images):
            # Add white border to images
            bordered_img = Image.new('RGB', (img.width + 20, img.height + 20), WHITE)
            bordered_img.paste(img, (10, 10))
            
            # Add gold frame
            bordered_draw = ImageDraw.Draw(bordered_img)
            bordered_draw.rectangle([0, 0, bordered_img.width - 1, bordered_img.height - 1], 
                                   outline=GOLD, width=5)
            
            canvas.paste(bordered_img, (start_x, y_pos))
            start_x += img.width + 20 + spacing
    
    # Add main title with shadow effect
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 140)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    # Main title "STR8"
    title_text = "STR8"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = 150
    
    # Title shadow
    shadow_offset = 5
    draw.text((title_x + shadow_offset, title_y + shadow_offset), title_text, 
              fill=(200, 200, 200, 128), font=title_font)
    
    # Title gradient effect (gold to royal blue)
    draw.text((title_x, title_y), title_text, fill=DEEP_BLUE, font=title_font)
    
    # Subtitle "POSITIVE THINKING"
    subtitle_text = "POSITIVE THINKING"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = title_y + 160
    
    # Subtitle with gold color
    draw.text((subtitle_x + 3, subtitle_y + 3), subtitle_text, fill=(180, 180, 180), font=subtitle_font)
    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=GOLD, font=subtitle_font)
    
    # Add decorative cross symbol
    cross_size = 60
    cross_x = width // 2
    cross_y = subtitle_y + 120
    cross_thickness = 15
    
    # Gold cross
    draw.rectangle([cross_x - cross_thickness//2, cross_y - cross_size, 
                   cross_x + cross_thickness//2, cross_y + cross_size], fill=GOLD)
    draw.rectangle([cross_x - cross_size, cross_y - cross_thickness//2, 
                   cross_x + cross_size, cross_y + cross_thickness//2], fill=GOLD)
    
    # Royal blue outline on cross
    draw.rectangle([cross_x - cross_thickness//2 - 2, cross_y - cross_size - 2, 
                   cross_x + cross_thickness//2 + 2, cross_y + cross_size + 2], 
                   outline=ROYAL_BLUE, width=3)
    draw.rectangle([cross_x - cross_size - 2, cross_y - cross_thickness//2 - 2, 
                   cross_x + cross_size + 2, cross_y + cross_thickness//2 + 2], 
                   outline=ROYAL_BLUE, width=3)
    
    # Add inspirational text
    inspiration_text = "Transforming Lives Through Faith & Positivity"
    insp_bbox = draw.textbbox((0, 0), inspiration_text, font=text_font)
    insp_width = insp_bbox[2] - insp_bbox[0]
    insp_x = (width - insp_width) // 2
    insp_y = cross_y + 100
    
    draw.text((insp_x, insp_y), inspiration_text, fill=ROYAL_BLUE, font=text_font)
    
    # Add tagline
    tagline = "aka STEVIE DA TROUBLEMAKER"
    tag_bbox = draw.textbbox((0, 0), tagline, font=text_font)
    tag_width = tag_bbox[2] - tag_bbox[0]
    tag_x = (width - tag_width) // 2
    tag_y = insp_y + 80
    
    draw.text((tag_x, tag_y), tagline, fill=DEEP_BLUE, font=text_font)
    
    # Add decorative corner elements (golden rays)
    for corner in [(100, 100), (width - 100, 100), (100, height - 100), (width - 100, height - 100)]:
        for i in range(8):
            angle = i * 45
            if corner[0] < width // 2 and corner[1] < height // 2:  # Top left
                end_x = corner[0] + 60 * (1 if angle % 90 == 0 else 0.7)
                end_y = corner[1] + 60 * (1 if angle % 90 == 0 else 0.7)
            elif corner[0] > width // 2 and corner[1] < height // 2:  # Top right
                end_x = corner[0] - 60 * (1 if angle % 90 == 0 else 0.7)
                end_y = corner[1] + 60 * (1 if angle % 90 == 0 else 0.7)
            elif corner[0] < width // 2 and corner[1] > height // 2:  # Bottom left
                end_x = corner[0] + 60 * (1 if angle % 90 == 0 else 0.7)
                end_y = corner[1] - 60 * (1 if angle % 90 == 0 else 0.7)
            else:  # Bottom right
                end_x = corner[0] - 60 * (1 if angle % 90 == 0 else 0.7)
                end_y = corner[1] - 60 * (1 if angle % 90 == 0 else 0.7)
            
            draw.line([corner, (end_x, end_y)], fill=LIGHT_GOLD, width=3)
    
    # Save the image
    output_path = 'str8_positive_thinking_professional.jpg'
    canvas.save(output_path, 'JPEG', quality=95)
    print(f"✓ Professional design created: {output_path}")
    print(f"  Resolution: {width}x{height}")
    print(f"  Style: White background with gold and royal blue accents")
    
    return output_path

if __name__ == "__main__":
    print("Creating professional STR8 Positive Thinking design...")
    output_file = create_professional_design()
    print(f"\nDesign complete! File saved as: {output_file}")
