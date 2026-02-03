#!/usr/bin/env python3
"""
Inviting Modern STR8 Positive Thinking Design Generator
Clean, friendly, professional, and contemporary aesthetic
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

def create_inviting_modern_design():
    """
    Modern, inviting, professional design
    Clean white space, friendly layout, contemporary feel
    """
    width, height = 3000, 2000
    
    # Inviting modern color palette
    PURE_WHITE = (255, 255, 255)
    SOFT_WHITE = (252, 252, 252)
    WARM_GOLD = (255, 200, 87)
    BRIGHT_GOLD = (255, 215, 0)
    MODERN_NAVY = (28, 42, 82)
    FRIENDLY_BLUE = (65, 105, 225)
    LIGHT_BLUE = (173, 216, 230)
    SOFT_CREAM = (255, 253, 248)
    ACCENT_ORANGE = (255, 160, 70)
    
    # Create canvas with clean white background
    canvas = Image.new('RGB', (width, height), PURE_WHITE)
    draw = ImageDraw.Draw(canvas)
    
    # Very subtle gradient - barely noticeable, just adds warmth
    for y in range(height):
        alpha = (y / height) * 0.03
        color = tuple(int(PURE_WHITE[i] * (1 - alpha) + SOFT_CREAM[i] * alpha) for i in range(3))
        draw.rectangle([(0, y), (width, y + 1)], fill=color)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 280)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 70)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Simple, clean border - minimal and modern
    border_margin = 60
    draw.rectangle([border_margin, border_margin, width - border_margin, height - border_margin], 
                   outline=WARM_GOLD, width=8)
    
    # Title "STR8" - bold and friendly
    title_text = "STR8"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = 180
    
    # Soft shadow for depth
    draw.text((title_x + 4, title_y + 4), title_text, fill=(220, 220, 220), font=title_font)
    # Main title in navy
    draw.text((title_x, title_y), title_text, fill=MODERN_NAVY, font=title_font)
    
    # Simple decorative element - clean lines
    line_y = title_y + 320
    line_center = width // 2
    line_length = 500
    
    # Clean gold lines
    draw.rectangle([line_center - line_length, line_y, line_center - 100, line_y + 5], fill=WARM_GOLD)
    draw.rectangle([line_center + 100, line_y, line_center + line_length, line_y + 5], fill=WARM_GOLD)
    
    # Simple modern cross icon
    cross_size = 50
    cross_thickness = 14
    cross_x = line_center
    cross_y = line_y + 2
    
    # Gold cross - clean and simple
    draw.rectangle([cross_x - cross_thickness//2, cross_y - cross_size, 
                   cross_x + cross_thickness//2, cross_y + cross_size], fill=BRIGHT_GOLD)
    draw.rectangle([cross_x - cross_size, cross_y - cross_thickness//2, 
                   cross_x + cross_size, cross_y + cross_thickness//2], fill=BRIGHT_GOLD)
    
    # Subtitle "POSITIVE THINKING"
    subtitle_text = "POSITIVE THINKING"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = line_y + 100
    
    # Friendly gold color
    draw.text((subtitle_x + 2, subtitle_y + 2), subtitle_text, fill=(230, 230, 230), font=subtitle_font)
    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=WARM_GOLD, font=subtitle_font)
    
    # Inspirational text - friendly blue
    inspiration_text = "Transforming Lives Through Faith & Positivity"
    insp_bbox = draw.textbbox((0, 0), inspiration_text, font=text_font)
    insp_width = insp_bbox[2] - insp_bbox[0]
    insp_x = (width - insp_width) // 2
    insp_y = subtitle_y + 180
    
    draw.text((insp_x, insp_y), inspiration_text, fill=FRIENDLY_BLUE, font=text_font)
    
    # Tagline
    tagline = "aka STEVIE DA TROUBLEMAKER"
    tag_bbox = draw.textbbox((0, 0), tagline, font=small_font)
    tag_width = tag_bbox[2] - tag_bbox[0]
    tag_x = (width - tag_width) // 2
    tag_y = insp_y + 110
    
    draw.text((tag_x, tag_y), tagline, fill=MODERN_NAVY, font=small_font)
    
    # Load and arrange classroom images - clean, modern, minimal framing
    classroom_images = []
    for i in range(1, 4):
        try:
            img = Image.open(f'classroom_scene{i}.jpg')
            img.thumbnail((500, 400), Image.Resampling.LANCZOS)
            
            # Enhance for vibrancy
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.3)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.15)
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.1)
            
            classroom_images.append(img)
        except Exception as e:
            print(f"Could not load classroom_scene{i}.jpg: {e}")
    
    # Modern image layout - clean, minimal frames
    if classroom_images:
        spacing = 60
        total_width = sum(img.width for img in classroom_images) + spacing * (len(classroom_images) - 1)
        start_x = (width - total_width) // 2
        y_pos = height - 550
        
        for idx, img in enumerate(classroom_images):
            # Minimal modern frame - just a simple border
            border_width = 5
            
            # White border for clean separation
            white_border = Image.new('RGB', (img.width + 20, img.height + 20), PURE_WHITE)
            white_border.paste(img, (10, 10))
            
            # Simple gold accent border
            final = Image.new('RGB', (white_border.width + border_width*2, white_border.height + border_width*2), WARM_GOLD)
            final.paste(white_border, (border_width, border_width))
            
            # Soft, subtle shadow for depth
            shadow_size = 15
            shadow = Image.new('RGBA', (final.width + shadow_size*2, final.height + shadow_size*2), (0, 0, 0, 0))
            shadow_draw = ImageDraw.Draw(shadow)
            shadow_draw.rectangle([shadow_size, shadow_size, shadow.width - shadow_size, shadow.height - shadow_size], 
                                 fill=(0, 0, 0, 25))
            shadow = shadow.filter(ImageFilter.GaussianBlur(10))
            
            canvas.paste(shadow, (start_x - shadow_size, y_pos - shadow_size), shadow)
            canvas.paste(final, (start_x, y_pos))
            
            start_x += final.width + spacing
    
    # Modern corner accents - simple and clean
    accent_size = 60
    accent_width = 5
    
    corners = [(90, 90), (width - 90, 90), (90, height - 90), (width - 90, height - 90)]
    for idx, corner in enumerate(corners):
        if idx == 0:  # Top left
            draw.line([corner[0], corner[1], corner[0] + accent_size, corner[1]], fill=WARM_GOLD, width=accent_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] + accent_size], fill=WARM_GOLD, width=accent_width)
        elif idx == 1:  # Top right
            draw.line([corner[0], corner[1], corner[0] - accent_size, corner[1]], fill=WARM_GOLD, width=accent_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] + accent_size], fill=WARM_GOLD, width=accent_width)
        elif idx == 2:  # Bottom left
            draw.line([corner[0], corner[1], corner[0] + accent_size, corner[1]], fill=WARM_GOLD, width=accent_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] - accent_size], fill=WARM_GOLD, width=accent_width)
        else:  # Bottom right
            draw.line([corner[0], corner[1], corner[0] - accent_size, corner[1]], fill=WARM_GOLD, width=accent_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] - accent_size], fill=WARM_GOLD, width=accent_width)
    
    output_path = 'str8_inviting_modern_design.jpg'
    canvas.save(output_path, 'JPEG', quality=98, optimize=True)
    print(f"✓ Inviting Modern Design created: {output_path}")
    print(f"  Resolution: {width}x{height}")
    print(f"  Style: Inviting, Professional, Modern")
    
    return output_path

def create_inviting_modern_design_v2():
    """
    Alternative modern design - even more open and friendly
    """
    width, height = 3000, 2000
    
    # Fresh, inviting colors
    PURE_WHITE = (255, 255, 255)
    SUNSHINE_GOLD = (255, 193, 37)
    BRIGHT_NAVY = (41, 50, 65)
    SKY_BLUE = (100, 149, 237)
    SOFT_GRAY = (248, 248, 248)
    WARM_ORANGE = (255, 152, 51)
    
    # Clean white canvas
    canvas = Image.new('RGB', (width, height), PURE_WHITE)
    draw = ImageDraw.Draw(canvas)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 300)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 130)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 72)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 62)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Minimal border - just simple lines at edges
    margin = 80
    border_width = 6
    draw.rectangle([margin, margin, width - margin, height - margin], outline=SUNSHINE_GOLD, width=border_width)
    
    # Title "STR8" - big and bold
    title_text = "STR8"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = 160
    
    # Very subtle shadow
    draw.text((title_x + 3, title_y + 3), title_text, fill=(235, 235, 235), font=title_font)
    draw.text((title_x, title_y), title_text, fill=BRIGHT_NAVY, font=title_font)
    
    # Clean separator with cross
    sep_y = title_y + 350
    sep_center = width // 2
    
    # Simple horizontal line
    line_width = 1000
    draw.rectangle([sep_center - line_width//2, sep_y, sep_center + line_width//2, sep_y + 4], fill=SUNSHINE_GOLD)
    
    # Centered cross icon - simple and clean
    cross_size = 45
    cross_thick = 12
    
    # Circular background for cross
    circle_radius = 60
    draw.ellipse([sep_center - circle_radius, sep_y - circle_radius + 2, 
                  sep_center + circle_radius, sep_y + circle_radius + 2], 
                 fill=SUNSHINE_GOLD)
    
    # White cross on gold circle
    draw.rectangle([sep_center - cross_thick//2, sep_y - cross_size + 2, 
                   sep_center + cross_thick//2, sep_y + cross_size + 2], fill=PURE_WHITE)
    draw.rectangle([sep_center - cross_size, sep_y - cross_thick//2 + 2, 
                   sep_center + cross_size, sep_y + cross_thick//2 + 2], fill=PURE_WHITE)
    
    # Subtitle
    subtitle_text = "POSITIVE THINKING"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = sep_y + 120
    
    draw.text((subtitle_x + 2, subtitle_y + 2), subtitle_text, fill=(240, 240, 240), font=subtitle_font)
    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=SUNSHINE_GOLD, font=subtitle_font)
    
    # Inspirational text
    inspiration_text = "Transforming Lives Through Faith & Positivity"
    insp_bbox = draw.textbbox((0, 0), inspiration_text, font=text_font)
    insp_width = insp_bbox[2] - insp_bbox[0]
    insp_x = (width - insp_width) // 2
    insp_y = subtitle_y + 200
    
    draw.text((insp_x, insp_y), inspiration_text, fill=SKY_BLUE, font=text_font)
    
    # Tagline
    tagline = "aka STEVIE DA TROUBLEMAKER"
    tag_bbox = draw.textbbox((0, 0), tagline, font=small_font)
    tag_width = tag_bbox[2] - tag_bbox[0]
    tag_x = (width - tag_width) // 2
    tag_y = insp_y + 115
    
    draw.text((tag_x, tag_y), tagline, fill=BRIGHT_NAVY, font=small_font)
    
    # Load classroom images
    classroom_images = []
    for i in range(1, 4):
        try:
            img = Image.open(f'classroom_scene{i}.jpg')
            img.thumbnail((520, 420), Image.Resampling.LANCZOS)
            
            # Enhance
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.3)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.2)
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.15)
            
            classroom_images.append(img)
        except Exception as e:
            print(f"Could not load classroom_scene{i}.jpg: {e}")
    
    # Ultra-minimal image framing - barely there
    if classroom_images:
        spacing = 50
        total_width = sum(img.width for img in classroom_images) + spacing * (len(classroom_images) - 1)
        start_x = (width - total_width) // 2
        y_pos = height - 560
        
        for idx, img in enumerate(classroom_images):
            # Just a simple white space and thin border
            padding = 8
            
            # Thin gold border only
            bordered = Image.new('RGB', (img.width + padding*2, img.height + padding*2), PURE_WHITE)
            bordered.paste(img, (padding, padding))
            
            # Draw simple border
            border_draw = ImageDraw.Draw(bordered)
            border_draw.rectangle([0, 0, bordered.width-1, bordered.height-1], outline=SUNSHINE_GOLD, width=4)
            
            # Very subtle shadow
            shadow_offset = 12
            shadow = Image.new('RGBA', (bordered.width + shadow_offset*2, bordered.height + shadow_offset*2), (0, 0, 0, 0))
            shadow_draw = ImageDraw.Draw(shadow)
            shadow_draw.rectangle([shadow_offset, shadow_offset, shadow.width - shadow_offset, shadow.height - shadow_offset], 
                                 fill=(0, 0, 0, 20))
            shadow = shadow.filter(ImageFilter.GaussianBlur(8))
            
            canvas.paste(shadow, (start_x - shadow_offset, y_pos - shadow_offset), shadow)
            canvas.paste(bordered, (start_x, y_pos))
            
            start_x += bordered.width + spacing
    
    # Simple corner marks - minimal
    mark_size = 50
    mark_width = 4
    
    corners = [(100, 100), (width - 100, 100), (100, height - 100), (width - 100, height - 100)]
    for idx, corner in enumerate(corners):
        if idx == 0:  # Top left
            draw.line([corner[0], corner[1], corner[0] + mark_size, corner[1]], fill=SUNSHINE_GOLD, width=mark_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] + mark_size], fill=SUNSHINE_GOLD, width=mark_width)
        elif idx == 1:  # Top right
            draw.line([corner[0], corner[1], corner[0] - mark_size, corner[1]], fill=SUNSHINE_GOLD, width=mark_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] + mark_size], fill=SUNSHINE_GOLD, width=mark_width)
        elif idx == 2:  # Bottom left
            draw.line([corner[0], corner[1], corner[0] + mark_size, corner[1]], fill=SUNSHINE_GOLD, width=mark_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] - mark_size], fill=SUNSHINE_GOLD, width=mark_width)
        else:  # Bottom right
            draw.line([corner[0], corner[1], corner[0] - mark_size, corner[1]], fill=SUNSHINE_GOLD, width=mark_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] - mark_size], fill=SUNSHINE_GOLD, width=mark_width)
    
    output_path = 'str8_inviting_modern_design_v2.jpg'
    canvas.save(output_path, 'JPEG', quality=98, optimize=True)
    print(f"✓ Inviting Modern Design V2 created: {output_path}")
    print(f"  Resolution: {width}x{height}")
    print(f"  Style: Open, Friendly, Contemporary")
    
    return output_path

if __name__ == "__main__":
    print("=" * 60)
    print("Creating INVITING MODERN STR8 Designs")
    print("=" * 60)
    print()
    
    designs = []
    
    print("Creating Design V1: Inviting Professional Modern...")
    v1 = create_inviting_modern_design()
    designs.append(v1)
    print()
    
    print("Creating Design V2: Open & Friendly Contemporary...")
    v2 = create_inviting_modern_design_v2()
    designs.append(v2)
    print()
    
    print("=" * 60)
    print("✨ ALL INVITING MODERN DESIGNS COMPLETE! ✨")
    print("=" * 60)
    print(f"\nCreated {len(designs)} beautiful designs:")
    for design in designs:
        print(f"  • {design}")
    print("\nClean, inviting, professional, and modern!")
    print("Minimal frames, maximum impact!")
