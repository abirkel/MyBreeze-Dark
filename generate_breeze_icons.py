#!/usr/bin/env python3
"""
Generate Breeze-style button icons for Aurorae theme.
Based on exact coordinates from breeze-official/kdecoration/breezebutton.cpp
"""

import os

# SVG template with proper Aurorae state structure
SVG_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   width="18"
   height="18"
   viewBox="0 0 72 18"
   version="1.1"
   xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style type="text/css">
      .icon-normal {{ fill:none; stroke:#fcfcfc; stroke-width:1.01; stroke-linecap:round; stroke-linejoin:round; }}
      .icon-hover {{ fill:none; stroke:#ffffff; stroke-width:1.01; stroke-linecap:round; stroke-linejoin:round; }}
      .bg-hover {{ fill:#3daeea; }}
      .bg-hover-close {{ fill:#da4453; }}
      .bg-pressed {{ fill:#33a4e0; }}
      .bg-pressed-close {{ fill:#c63d47; }}
    </style>
  </defs>
  
  <!-- Active state (normal) -->
  <g id="active-center" transform="translate(0,0)">
    <rect x="0" y="0" width="18" height="18" fill="none" opacity="0.01" />
{icon_paths_normal}
  </g>
  
  <!-- Inactive state -->
  <g id="inactive-center" transform="translate(18,0)">
    <rect x="18" y="0" width="18" height="18" fill="none" opacity="0.01" />
{icon_paths_inactive}
  </g>
  
  <!-- Hover state -->
  <g id="hover-center" transform="translate(36,0)">
    <rect x="36" y="0" width="18" height="18" fill="none" opacity="0.01" />
    <circle cx="45" cy="9" r="9" class="{hover_bg_class}" />
{icon_paths_hover}
  </g>
  
  <!-- Pressed state -->
  <g id="pressed-center" transform="translate(54,0)">
    <rect x="54" y="0" width="18" height="18" fill="none" opacity="0.01" />
    <circle cx="63" cy="9" r="9" class="{pressed_bg_class}" />
{icon_paths_pressed}
  </g>
</svg>'''

# Icon definitions based on Breeze C++ code
ICONS = {
    'close': {
        'paths': [
            '<line x1="5" y1="5" x2="13" y2="13" />',
            '<line x1="13" y1="5" x2="5" y2="13" />',
        ]
    },
    'minimize': {
        'paths': [
            '<polyline points="4,7 9,12 14,7" />',
        ]
    },
    'maximize': {
        'paths': [
            '<polyline points="4,11 9,6 14,11" />',
        ]
    },
    'restore': {
        'paths': [
            '<polygon points="4,9 9,4 14,9 9,14" fill="none" />',
        ]
    },
    'alldesktops': {
        'paths': [
            # Unchecked state - pin icon
            '<polygon points="6.5,8.5 12,3 15,6 9.5,11.5" fill="currentColor" stroke="none" />',
            '<line x1="5.5" y1="7.5" x2="10.5" y2="12.5" />',
            '<line x1="12" y1="6" x2="4.5" y2="13.5" />',
        ]
    },
    'shade': {
        'paths': [
            # Unshaded state
            '<line x1="4" y1="5.5" x2="14" y2="5.5" />',
            '<polyline points="4,13 9,8 14,13" />',
        ]
    },
    'keepbelow': {
        'paths': [
            '<polyline points="4,5 9,10 14,5" />',
            '<polyline points="4,9 9,14 14,9" />',
        ]
    },
    'keepabove': {
        'paths': [
            '<polyline points="4,9 9,4 14,9" />',
            '<polyline points="4,13 9,8 14,13" />',
        ]
    },
    'help': {
        'paths': [
            # Question mark - exact Breeze path
            # path.moveTo(5, 6); path.arcTo(QRectF(5, 3.5, 8, 5), 180, -180); path.cubicTo(QPointF(12.5, 9.5), QPointF(9, 7.5), QPointF(9, 11.5));
            # Arc: QRectF(5, 3.5, 8, 5) = x,y,w,h so center at (5+4, 3.5+2.5) = (9, 6), radii 4x2.5
            # Start angle 180° (left), sweep -180° (clockwise to right)
            '<path d="M 5,6 A 4,2.5 0 0 1 13,6 C 12.5,9.5 9,7.5 9,11.5" fill="none" stroke-width="1.01" />',
            # Dot at bottom - painter->drawRect(QRectF(9, 15, 0.5, 0.5))
            '<rect x="9" y="15" width="0.5" height="0.5" fill="#fcfcfc" stroke="none" />',
        ]
    },
}

def generate_icon(name, icon_data):
    """Generate SVG for a single icon with all states."""
    paths = icon_data['paths']
    
    # Determine background classes (close button uses red)
    hover_bg = 'bg-hover-close' if name == 'close' else 'bg-hover'
    pressed_bg = 'bg-pressed-close' if name == 'close' else 'bg-pressed'
    
    # Generate paths for each state with proper transforms
    def make_paths(x_offset, css_class):
        result = []
        for path in paths:
            # Adjust x coordinates in the path
            adjusted = path
            if x_offset > 0:
                # Simple string replacement for common attributes
                import re
                # Replace x1, x2, x, cx attributes
                adjusted = re.sub(r'x1="(\d+\.?\d*)"', lambda m: f'x1="{float(m.group(1)) + x_offset}"', adjusted)
                adjusted = re.sub(r'x2="(\d+\.?\d*)"', lambda m: f'x2="{float(m.group(1)) + x_offset}"', adjusted)
                adjusted = re.sub(r' x="(\d+\.?\d*)"', lambda m: f' x="{float(m.group(1)) + x_offset}"', adjusted)
                adjusted = re.sub(r'cx="(\d+\.?\d*)"', lambda m: f'cx="{float(m.group(1)) + x_offset}"', adjusted)
                # Adjust points in polyline/polygon
                adjusted = re.sub(r'points="([^"]+)"', lambda m: adjust_points(m.group(1), x_offset), adjusted)
                # Adjust path d attribute
                if 'd="' in adjusted:
                    adjusted = re.sub(r'd="([^"]+)"', lambda m: f'd="{adjust_path_d(m.group(1), x_offset)}"', adjusted)
            result.append(f'    <g class="{css_class}">{adjusted}</g>')
        return '\n'.join(result)
    
    def adjust_points(points_str, offset):
        """Adjust x coordinates in points attribute."""
        pairs = points_str.split()
        adjusted = []
        for pair in pairs:
            if ',' in pair:
                x, y = pair.split(',')
                adjusted.append(f"{float(x) + offset},{y}")
        return ' '.join(adjusted)
    
    def adjust_path_d(d_str, offset):
        """Adjust x coordinates in path d attribute."""
        import re
        # Parse and adjust SVG path commands - process in order
        result = d_str
        # M command: M x,y
        result = re.sub(r'M\s*(\d+\.?\d*),(\d+\.?\d*)', lambda m: f'M {float(m.group(1)) + offset},{m.group(2)}', result)
        # A command: A rx,ry rotation large-arc sweep x,y
        # Format: A 4,2.5 0 0 1 13,6 (spaces between flags, comma between x,y)
        result = re.sub(r'A\s+(\d+\.?\d*),(\d+\.?\d*)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+\.?\d*),(\d+\.?\d*)', 
                       lambda m: f'A {m.group(1)},{m.group(2)} {m.group(3)} {m.group(4)} {m.group(5)} {float(m.group(6)) + offset},{m.group(7)}', result)
        # C command: C x1,y1 x2,y2 x,y
        result = re.sub(r'C\s*(\d+\.?\d*),(\d+\.?\d*)\s+(\d+\.?\d*),(\d+\.?\d*)\s+(\d+\.?\d*),(\d+\.?\d*)', 
                       lambda m: f'C {float(m.group(1)) + offset},{m.group(2)} {float(m.group(3)) + offset},{m.group(4)} {float(m.group(5)) + offset},{m.group(6)}', result)
        return result
    
    paths_normal = make_paths(0, 'icon-normal')
    paths_inactive = make_paths(18, 'icon-normal')
    paths_hover = make_paths(36, 'icon-hover')
    paths_pressed = make_paths(54, 'icon-hover')
    
    svg_content = SVG_TEMPLATE.format(
        icon_paths_normal=paths_normal,
        icon_paths_inactive=paths_inactive,
        icon_paths_hover=paths_hover,
        icon_paths_pressed=paths_pressed,
        hover_bg_class=hover_bg,
        pressed_bg_class=pressed_bg
    )
    return svg_content

def main():
    """Generate all icon SVG files."""
    output_dir = 'aurorae/MyBreeze-Dark'
    
    if not os.path.exists(output_dir):
        print(f"Error: Directory {output_dir} not found!")
        return
    
    print("Generating Breeze-style icons...")
    
    for name, icon_data in ICONS.items():
        svg_content = generate_icon(name, icon_data)
        output_path = os.path.join(output_dir, f'{name}.svg')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"  ✓ Generated {name}.svg")
    
    print(f"\nSuccessfully generated {len(ICONS)} icon files!")
    print("\nNote: These icons are based on exact Breeze coordinates:")
    print("  - 18x18 viewBox")
    print("  - 1.01px stroke width")
    print("  - Round line caps and joins")
    print("  - Exact coordinates from breeze-official/kdecoration/breezebutton.cpp")

if __name__ == '__main__':
    main()
