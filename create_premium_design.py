#!/usr/bin/env python3
"""
Premium STR8 Positive Thinking Design Generator
Creates multiple high-quality, professional designs with exceptional aesthetics
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

def create_premium_design_v1():
    """
    Version 1: Elegant Minimalist with Golden Accents
    Clean, sophisticated, with perfect balance
    """
    width, height = 3000, 2000
    
    # Premium color palette
    PURE_WHITE = (255, 255, 255)
    CHAMPAGNE_GOLD = (240, 220, 130)
    ROYAL_GOLD = (212, 175, 55)
    NAVY_BLUE = (0, 32, 63)
    DEEP_ROYAL_BLUE = (25, 55, 109)
    LIGHT_CREAM = (255, 251, 240)
    ACCENT_GOLD = (255, 215, 0)
    SOFT_GRAY = (245, 245, 245)
    
    # Create canvas with gradient background
    canvas = Image.new('RGB', (width, height), PURE_WHITE)
    draw = ImageDraw.Draw(canvas)
    
    # Subtle radial gradient from center
    for y in range(height):
        for x in range(width):
            # Distance from center
            dx = (x - width/2) / (width/2)
            dy = (y - height/2) / (height/2)
            distance = min(1.0, (dx*dx + dy*dy) ** 0.5)
            
            # Blend from white to very light cream
            alpha = distance * 0.15
            color = tuple(int(PURE_WHITE[i] * (1 - alpha) + LIGHT_CREAM[i] * alpha) for i in range(3))
            draw.point((x, y), fill=color)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 220)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Premium border with multiple layers
    border_margin = 40
    # Outer gold border
    draw.rectangle([border_margin, border_margin, width - border_margin, height - border_margin], 
                   outline=ROYAL_GOLD, width=15)
    # Inner navy border
    draw.rectangle([border_margin + 25, border_margin + 25, width - border_margin - 25, height - border_margin - 25], 
                   outline=NAVY_BLUE, width=8)
    # Innermost thin gold accent
    draw.rectangle([border_margin + 40, border_margin + 40, width - border_margin - 40, height - border_margin - 40], 
                   outline=CHAMPAGNE_GOLD, width=3)
    
    # Main title "STR8" with premium styling
    title_text = "STR8"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = 250
    
    # Multi-layer shadow for depth
    for offset in range(8, 0, -2):
        shadow_alpha = 30 + (8 - offset) * 10
        draw.text((title_x + offset, title_y + offset), title_text, 
                  fill=(100, 100, 100), font=title_font)
    
    # Main title in navy
    draw.text((title_x, title_y), title_text, fill=NAVY_BLUE, font=title_font)
    
    # Decorative line under title
    line_y = title_y + 250
    line_center = width // 2
    line_length = 600
    
    # Gold decorative line with center ornament
    draw.rectangle([line_center - line_length, line_y, line_center - 80, line_y + 6], fill=ROYAL_GOLD)
    draw.rectangle([line_center + 80, line_y, line_center + line_length, line_y + 6], fill=ROYAL_GOLD)
    
    # Center diamond ornament
    diamond_size = 40
    diamond_points = [
        (line_center, line_y - diamond_size),
        (line_center + diamond_size, line_y + 3),
        (line_center, line_y + diamond_size + 6),
        (line_center - diamond_size, line_y + 3)
    ]
    draw.polygon(diamond_points, fill=ROYAL_GOLD, outline=NAVY_BLUE, width=3)
    
    # Subtitle "POSITIVE THINKING"
    subtitle_text = "POSITIVE THINKING"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = line_y + 80
    
    # Gradient effect on subtitle (gold)
    draw.text((subtitle_x + 4, subtitle_y + 4), subtitle_text, fill=(150, 150, 150), font=subtitle_font)
    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=ROYAL_GOLD, font=subtitle_font)
    
    # Premium cross with ornate design
    cross_y = subtitle_y + 180
    cross_x = width // 2
    cross_size = 80
    cross_thickness = 20
    
    # Cross shadow
    draw.rectangle([cross_x - cross_thickness//2 + 4, cross_y - cross_size + 4, 
                   cross_x + cross_thickness//2 + 4, cross_y + cross_size + 4], fill=(180, 180, 180))
    draw.rectangle([cross_x - cross_size + 4, cross_y - cross_thickness//2 + 4, 
                   cross_x + cross_size + 4, cross_y + cross_thickness//2 + 4], fill=(180, 180, 180))
    
    # Cross main body in gold
    draw.rectangle([cross_x - cross_thickness//2, cross_y - cross_size, 
                   cross_x + cross_thickness//2, cross_y + cross_size], fill=ACCENT_GOLD)
    draw.rectangle([cross_x - cross_size, cross_y - cross_thickness//2, 
                   cross_x + cross_size, cross_y + cross_thickness//2], fill=ACCENT_GOLD)
    
    # Cross outline in navy
    draw.rectangle([cross_x - cross_thickness//2 - 3, cross_y - cross_size - 3, 
                   cross_x + cross_thickness//2 + 3, cross_y + cross_size + 3], 
                   outline=NAVY_BLUE, width=4)
    draw.rectangle([cross_x - cross_size - 3, cross_y - cross_thickness//2 - 3, 
                   cross_x + cross_size + 3, cross_y + cross_thickness//2 + 3], 
                   outline=NAVY_BLUE, width=4)
    
    # Ornate circles at cross ends
    for pos in [(cross_x, cross_y - cross_size), (cross_x, cross_y + cross_size),
                (cross_x - cross_size, cross_y), (cross_x + cross_size, cross_y)]:
        draw.ellipse([pos[0] - 15, pos[1] - 15, pos[0] + 15, pos[1] + 15], 
                     fill=NAVY_BLUE, outline=ACCENT_GOLD, width=3)
    
    # Inspirational text
    inspiration_text = "Transforming Lives Through Faith & Positivity"
    insp_bbox = draw.textbbox((0, 0), inspiration_text, font=text_font)
    insp_width = insp_bbox[2] - insp_bbox[0]
    insp_x = (width - insp_width) // 2
    insp_y = cross_y + 140
    
    draw.text((insp_x + 2, insp_y + 2), inspiration_text, fill=(200, 200, 200), font=text_font)
    draw.text((insp_x, insp_y), inspiration_text, fill=DEEP_ROYAL_BLUE, font=text_font)
    
    # Tagline
    tagline = "aka STEVIE DA TROUBLEMAKER"
    tag_bbox = draw.textbbox((0, 0), tagline, font=small_font)
    tag_width = tag_bbox[2] - tag_bbox[0]
    tag_x = (width - tag_width) // 2
    tag_y = insp_y + 100
    
    draw.text((tag_x, tag_y), tagline, fill=NAVY_BLUE, font=small_font)
    
    # Load and arrange classroom images in premium style
    classroom_images = []
    for i in range(1, 4):
        try:
            img = Image.open(f'classroom_scene{i}.jpg')
            img.thumbnail((450, 350), Image.Resampling.LANCZOS)
            
            # Enhance image quality
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.3)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.1)
            
            classroom_images.append(img)
        except Exception as e:
            print(f"Could not load classroom_scene{i}.jpg: {e}")
    
    # Position images at bottom with premium frames
    if classroom_images:
        spacing = 80
        total_width = sum(img.width for img in classroom_images) + spacing * (len(classroom_images) - 1)
        start_x = (width - total_width) // 2
        y_pos = height - 500
        
        for idx, img in enumerate(classroom_images):
            # Create premium frame
            frame_padding = 15
            frame_border = 8
            
            # Create white matte
            matte = Image.new('RGB', (img.width + frame_padding * 2, img.height + frame_padding * 2), PURE_WHITE)
            matte.paste(img, (frame_padding, frame_padding))
            
            # Add gold frame
            framed = Image.new('RGB', (matte.width + frame_border * 2, matte.height + frame_border * 2), ROYAL_GOLD)
            framed.paste(matte, (frame_border, frame_border))
            
            # Add outer navy border
            final_frame = Image.new('RGB', (framed.width + 6, framed.height + 6), NAVY_BLUE)
            final_frame.paste(framed, (3, 3))
            
            # Add subtle shadow
            shadow = Image.new('RGBA', (final_frame.width + 20, final_frame.height + 20), (0, 0, 0, 0))
            shadow_draw = ImageDraw.Draw(shadow)
            shadow_draw.rectangle([10, 10, shadow.width - 10, shadow.height - 10], fill=(0, 0, 0, 40))
            shadow = shadow.filter(ImageFilter.GaussianBlur(10))
            
            # Composite shadow and frame
            canvas.paste(shadow, (start_x - 10, y_pos - 10), shadow)
            canvas.paste(final_frame, (start_x, y_pos))
            
            start_x += final_frame.width + spacing
    
    # Add elegant corner flourishes
    flourish_size = 120
    flourish_thickness = 4
    
    for corner in [(100, 100), (width - 100, 100), (100, height - 100), (width - 100, height - 100)]:
        if corner[0] < width // 2 and corner[1] < height // 2:  # Top left
            draw.line([corner[0], corner[1] + flourish_size, corner[0], corner[1]], fill=ROYAL_GOLD, width=flourish_thickness)
            draw.line([corner[0], corner[1], corner[0] + flourish_size, corner[1]], fill=ROYAL_GOLD, width=flourish_thickness)
            # Inner accent
            draw.line([corner[0] + 15, corner[1] + 60, corner[0] + 15, corner[1] + 15], fill=NAVY_BLUE, width=2)
            draw.line([corner[0] + 15, corner[1] + 15, corner[0] + 60, corner[1] + 15], fill=NAVY_BLUE, width=2)
        elif corner[0] > width // 2 and corner[1] < height // 2:  # Top right
            draw.line([corner[0], corner[1] + flourish_size, corner[0], corner[1]], fill=ROYAL_GOLD, width=flourish_thickness)
            draw.line([corner[0], corner[1], corner[0] - flourish_size, corner[1]], fill=ROYAL_GOLD, width=flourish_thickness)
            draw.line([corner[0] - 15, corner[1] + 60, corner[0] - 15, corner[1] + 15], fill=NAVY_BLUE, width=2)
            draw.line([corner[0] - 15, corner[1] + 15, corner[0] - 60, corner[1] + 15], fill=NAVY_BLUE, width=2)
        elif corner[0] < width // 2 and corner[1] > height // 2:  # Bottom left
            draw.line([corner[0], corner[1] - flourish_size, corner[0], corner[1]], fill=ROYAL_GOLD, width=flourish_thickness)
            draw.line([corner[0], corner[1], corner[0] + flourish_size, corner[1]], fill=ROYAL_GOLD, width=flourish_thickness)
            draw.line([corner[0] + 15, corner[1] - 60, corner[0] + 15, corner[1] - 15], fill=NAVY_BLUE, width=2)
            draw.line([corner[0] + 15, corner[1] - 15, corner[0] + 60, corner[1] - 15], fill=NAVY_BLUE, width=2)
        else:  # Bottom right
            draw.line([corner[0], corner[1] - flourish_size, corner[0], corner[1]], fill=ROYAL_GOLD, width=flourish_thickness)
            draw.line([corner[0], corner[1], corner[0] - flourish_size, corner[1]], fill=ROYAL_GOLD, width=flourish_thickness)
            draw.line([corner[0] - 15, corner[1] - 60, corner[0] - 15, corner[1] - 15], fill=NAVY_BLUE, width=2)
            draw.line([corner[0] - 15, corner[1] - 15, corner[0] - 60, corner[1] - 15], fill=NAVY_BLUE, width=2)
    
    # Save with maximum quality
    output_path = 'str8_premium_design_v1.jpg'
    canvas.save(output_path, 'JPEG', quality=98, optimize=True)
    print(f"✓ Premium Design V1 created: {output_path}")
    print(f"  Resolution: {width}x{height}")
    print(f"  Style: Elegant Minimalist with Golden Accents")
    
    return output_path

def create_premium_design_v2():
    """
    Version 2: Bold Modern with Dynamic Layout
    Striking, contemporary, high-impact
    """
    width, height = 3000, 2000
    
    # Modern color palette
    PURE_WHITE = (255, 255, 255)
    BRIGHT_GOLD = (255, 215, 0)
    METALLIC_GOLD = (212, 175, 55)
    MIDNIGHT_BLUE = (10, 25, 47)
    ELECTRIC_BLUE = (0, 71, 171)
    CREAM = (254, 250, 245)
    SILVER = (192, 192, 192)
    
    # Create canvas
    canvas = Image.new('RGB', (width, height), PURE_WHITE)
    draw = ImageDraw.Draw(canvas)
    
    # Modern gradient background - diagonal sweep
    for x in range(width):
        for y in range(height):
            progress = (x + y) / (width + height)
            alpha = progress * 0.08
            color = tuple(int(PURE_WHITE[i] * (1 - alpha) + CREAM[i] * alpha) for i in range(3))
            draw.point((x, y), fill=color)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 240)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 110)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 65)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 55)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Modern geometric border
    margin = 60
    # Gold outer frame
    for i in range(3):
        draw.rectangle([margin + i*5, margin + i*5, width - margin - i*5, height - margin - i*5], 
                       outline=METALLIC_GOLD, width=2)
    
    # Navy accent lines
    draw.rectangle([margin + 20, margin + 20, width - margin - 20, height - margin - 20], 
                   outline=MIDNIGHT_BLUE, width=12)
    
    # Title "STR8" with bold modern styling
    title_text = "STR8"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = 200
    
    # Bold shadow
    draw.text((title_x + 6, title_y + 6), title_text, fill=(150, 150, 150), font=title_font)
    draw.text((title_x + 3, title_y + 3), title_text, fill=(100, 100, 100), font=title_font)
    # Main title
    draw.text((title_x, title_y), title_text, fill=MIDNIGHT_BLUE, font=title_font)
    
    # Modern accent bars
    bar_y = title_y + 280
    bar_width = 800
    bar_height = 8
    
    # Left bar - gold
    draw.rectangle([width//2 - bar_width - 100, bar_y, width//2 - 100, bar_y + bar_height], fill=BRIGHT_GOLD)
    # Right bar - gold
    draw.rectangle([width//2 + 100, bar_y, width//2 + bar_width + 100, bar_y + bar_height], fill=BRIGHT_GOLD)
    
    # Center icon - modern cross
    icon_size = 70
    icon_x = width // 2
    icon_y = bar_y + 4
    
    # Cross in circle
    draw.ellipse([icon_x - icon_size, icon_y - icon_size, icon_x + icon_size, icon_y + icon_size], 
                 fill=BRIGHT_GOLD, outline=MIDNIGHT_BLUE, width=6)
    
    cross_size = 35
    cross_thick = 12
    draw.rectangle([icon_x - cross_thick//2, icon_y - cross_size, 
                   icon_x + cross_thick//2, icon_y + cross_size], fill=MIDNIGHT_BLUE)
    draw.rectangle([icon_x - cross_size, icon_y - cross_thick//2, 
                   icon_x + cross_size, icon_y + cross_thick//2], fill=MIDNIGHT_BLUE)
    
    # Subtitle "POSITIVE THINKING"
    subtitle_text = "POSITIVE THINKING"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = bar_y + 120
    
    # Subtitle with metallic effect
    draw.text((subtitle_x + 3, subtitle_y + 3), subtitle_text, fill=(180, 180, 180), font=subtitle_font)
    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=METALLIC_GOLD, font=subtitle_font)
    
    # Inspirational text
    inspiration_text = "Transforming Lives Through Faith & Positivity"
    insp_bbox = draw.textbbox((0, 0), inspiration_text, font=text_font)
    insp_width = insp_bbox[2] - insp_bbox[0]
    insp_x = (width - insp_width) // 2
    insp_y = subtitle_y + 180
    
    draw.text((insp_x + 2, insp_y + 2), inspiration_text, fill=(200, 200, 200), font=text_font)
    draw.text((insp_x, insp_y), inspiration_text, fill=ELECTRIC_BLUE, font=text_font)
    
    # Tagline
    tagline = "aka STEVIE DA TROUBLEMAKER"
    tag_bbox = draw.textbbox((0, 0), tagline, font=small_font)
    tag_width = tag_bbox[2] - tag_bbox[0]
    tag_x = (width - tag_width) // 2
    tag_y = insp_y + 110
    
    draw.text((tag_x, tag_y), tagline, fill=MIDNIGHT_BLUE, font=small_font)
    
    # Load classroom images with modern presentation
    classroom_images = []
    for i in range(1, 4):
        try:
            img = Image.open(f'classroom_scene{i}.jpg')
            img.thumbnail((480, 380), Image.Resampling.LANCZOS)
            
            # Enhance
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.4)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.15)
            
            classroom_images.append(img)
        except Exception as e:
            print(f"Could not load classroom_scene{i}.jpg: {e}")
    
    # Modern image layout with dynamic frames
    if classroom_images:
        spacing = 70
        total_width = sum(img.width for img in classroom_images) + spacing * (len(classroom_images) - 1)
        start_x = (width - total_width) // 2
        y_pos = height - 530
        
        for idx, img in enumerate(classroom_images):
            # Modern frame design
            padding = 12
            border = 10
            
            # White inner matte
            matte = Image.new('RGB', (img.width + padding * 2, img.height + padding * 2), PURE_WHITE)
            matte.paste(img, (padding, padding))
            
            # Gold accent frame
            framed = Image.new('RGB', (matte.width + border * 2, matte.height + border * 2), BRIGHT_GOLD)
            framed.paste(matte, (border, border))
            
            # Navy outer border
            final = Image.new('RGB', (framed.width + 8, framed.height + 8), MIDNIGHT_BLUE)
            final.paste(framed, (4, 4))
            
            # Drop shadow
            shadow = Image.new('RGBA', (final.width + 30, final.height + 30), (0, 0, 0, 0))
            shadow_draw = ImageDraw.Draw(shadow)
            shadow_draw.rectangle([15, 15, shadow.width - 15, shadow.height - 15], fill=(0, 0, 0, 50))
            shadow = shadow.filter(ImageFilter.GaussianBlur(12))
            
            canvas.paste(shadow, (start_x - 15, y_pos - 15), shadow)
            canvas.paste(final, (start_x, y_pos))
            
            start_x += final.width + spacing
    
    # Modern corner accents - angular design
    accent_size = 80
    accent_width = 6
    
    corners = [(120, 120), (width - 120, 120), (120, height - 120), (width - 120, height - 120)]
    for idx, corner in enumerate(corners):
        if idx == 0:  # Top left
            # L-shape
            draw.line([corner[0], corner[1], corner[0] + accent_size, corner[1]], fill=BRIGHT_GOLD, width=accent_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] + accent_size], fill=BRIGHT_GOLD, width=accent_width)
            # Inner accent
            draw.line([corner[0] + 20, corner[1] + 20, corner[0] + 60, corner[1] + 20], fill=MIDNIGHT_BLUE, width=3)
            draw.line([corner[0] + 20, corner[1] + 20, corner[0] + 20, corner[1] + 60], fill=MIDNIGHT_BLUE, width=3)
        elif idx == 1:  # Top right
            draw.line([corner[0], corner[1], corner[0] - accent_size, corner[1]], fill=BRIGHT_GOLD, width=accent_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] + accent_size], fill=BRIGHT_GOLD, width=accent_width)
            draw.line([corner[0] - 20, corner[1] + 20, corner[0] - 60, corner[1] + 20], fill=MIDNIGHT_BLUE, width=3)
            draw.line([corner[0] - 20, corner[1] + 20, corner[0] - 20, corner[1] + 60], fill=MIDNIGHT_BLUE, width=3)
        elif idx == 2:  # Bottom left
            draw.line([corner[0], corner[1], corner[0] + accent_size, corner[1]], fill=BRIGHT_GOLD, width=accent_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] - accent_size], fill=BRIGHT_GOLD, width=accent_width)
            draw.line([corner[0] + 20, corner[1] - 20, corner[0] + 60, corner[1] - 20], fill=MIDNIGHT_BLUE, width=3)
            draw.line([corner[0] + 20, corner[1] - 20, corner[0] + 20, corner[1] - 60], fill=MIDNIGHT_BLUE, width=3)
        else:  # Bottom right
            draw.line([corner[0], corner[1], corner[0] - accent_size, corner[1]], fill=BRIGHT_GOLD, width=accent_width)
            draw.line([corner[0], corner[1], corner[0], corner[1] - accent_size], fill=BRIGHT_GOLD, width=accent_width)
            draw.line([corner[0] - 20, corner[1] - 20, corner[0] - 60, corner[1] - 20], fill=MIDNIGHT_BLUE, width=3)
            draw.line([corner[0] - 20, corner[1] - 20, corner[0] - 20, corner[1] - 60], fill=MIDNIGHT_BLUE, width=3)
    
    output_path = 'str8_premium_design_v2.jpg'
    canvas.save(output_path, 'JPEG', quality=98, optimize=True)
    print(f"✓ Premium Design V2 created: {output_path}")
    print(f"  Resolution: {width}x{height}")
    print(f"  Style: Bold Modern with Dynamic Layout")
    
    return output_path

if __name__ == "__main__":
    print("=" * 60)
    print("Creating PREMIUM STR8 Positive Thinking Designs")
    print("=" * 60)
    print()
    
    designs = []
    
    print("Creating Design V1: Elegant Minimalist...")
    v1 = create_premium_design_v1()
    designs.append(v1)
    print()
    
    print("Creating Design V2: Bold Modern...")
    v2 = create_premium_design_v2()
    designs.append(v2)
    print()
    
    print("=" * 60)
    print("✨ ALL PREMIUM DESIGNS COMPLETE! ✨")
    print("=" * 60)
    print(f"\nCreated {len(designs)} high-quality designs:")
    for design in designs:
        print(f"  • {design}")
    print("\nEach design is 3000x2000 pixels at 98% JPEG quality")
    print("Professional, print-ready, and absolutely stunning!")
