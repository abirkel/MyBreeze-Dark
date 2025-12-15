#!/usr/bin/env python3
"""
Generate Breeze-style button icons for Aurorae theme.
Based on exact coordinates from breeze-official/kdecoration/breezebutton.cpp
"""

import os

# SVG template with proper structure
SVG_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   width="18"
   height="18"
   viewBox="0 0 18 18"
   version="1.1"
   xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style type="text/css">
      .ColorScheme-Text {{ fill:#fcfcfc; }}
      .ColorScheme-Background {{ fill:#292c30; }}
      .ColorScheme-Highlight {{ fill:#3daeea; }}
      .ColorScheme-NegativeText {{ fill:#da4453; }}
    </style>
  </defs>
  
  <!-- Normal state background (invisible, for hit area) -->
  <circle id="normal-bg" cx="9" cy="9" r="9" fill="none" opacity="0" />
  
  <!-- Icon paths -->
  <g id="icon-normal" class="ColorScheme-Text" fill="none" stroke="currentColor" stroke-width="1.01" stroke-linecap="round" stroke-linejoin="round">
{icon_paths}
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
            # Question mark path
            '<path d="M 5,6 A 4,2.5 0 0,1 13,6 C 13,8.5 12.5,9.5 9,11.5" fill="none" />',
            '<rect x="9" y="15" width="0.5" height="0.5" fill="currentColor" stroke="none" />',
        ]
    },
}

def generate_icon(name, icon_data):
    """Generate SVG for a single icon."""
    paths = '\n    '.join(icon_data['paths'])
    svg_content = SVG_TEMPLATE.format(icon_paths=paths)
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
