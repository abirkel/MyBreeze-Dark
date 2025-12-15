# MyBreeze-Dark

A modern, dark theme for KDE Plasma that combines the best of MyBreeze and Breeze design philosophies. Includes both window decoration and color scheme for a cohesive experience.

## Features

- **Dark, Professional Aesthetic**: Based on official Breeze Dark color scheme
- **Clean, Minimal Design**: No window borders by default
- **Consistent Inactive States**: Menu bar text matches window title when inactive
- **Smooth Animations**: Subtle transitions between window states
- **Accent Color Support**: Respects system accent color settings
- **Aurorae-Based**: Lightweight SVG-based window decoration
- **Modern Proportions**: 22px title bar with optimal spacing
- **Matching Color Scheme**: Custom colors for unified appearance

## Color Palette

All colors are derived from the official Breeze Dark color scheme:

- **Active Title Bar**: RGB(39, 44, 49) - Dark charcoal
- **Inactive Title Bar**: RGB(32, 36, 40) - Darker charcoal
- **Active Text**: RGB(252, 252, 252) - Off-white
- **Inactive Text**: RGB(161, 169, 177) - Muted gray-blue
- **Button Hover**: RGB(61, 174, 233) - Bright blue accent
- **Close Button Hover**: RGB(218, 68, 83) - Red

## Installation

### Window Decoration

1. Copy the `aurorae/MyBreeze-Dark` folder to:
   - `~/.local/share/aurorae/themes/` (user-wide)
   - Or `/usr/share/aurorae/themes/` (system-wide)

2. Open KDE System Settings
3. Navigate to: Appearance → Window Decorations
4. Select "MyBreeze-Dark" from the list
5. Click "Apply"

### Color Scheme (Optional but Recommended)

To get matching inactive menu bar text colors:

1. Copy `colors/MyBreeze-Dark.colors` to:
   - `~/.local/share/color-schemes/` (user-wide)
   - Or `/usr/share/color-schemes/` (system-wide)

2. Open KDE System Settings
3. Navigate to: Appearance → Colors
4. Select "MyBreeze-Dark" from the list
5. Click "Apply"

This will make the File/Edit/Help menu text match the window title color when the window is inactive (muted gray-blue instead of white).

## What's Included

### Window Decoration (Aurorae)
- Custom window frame with Breeze Dark colors
- Title bar: 22px height, centered text
- No window borders (clean, modern look)
- Breeze-style buttons with proper hover states
- Close button: Red on hover
- Other buttons: Blue accent on hover

### Color Scheme
- Based on Breeze Dark
- **Key difference**: Inactive window menu bar text is muted (RGB 161,169,177) instead of white
- Matches inactive window title text for visual consistency
- All other colors identical to Breeze Dark

## File Structure

```
MyBreeze-Dark/
├── aurorae/MyBreeze-Dark/
│   ├── metadata.json          # Plugin metadata (KDE 6)
│   ├── metadata.desktop       # Plugin metadata (KDE 5)
│   ├── MyBreeze-Darkrc        # Configuration file
│   ├── decoration.svg         # Main window frame
│   └── *.svg                  # Button icons (10 files)
├── colors/
│   └── MyBreeze-Dark.colors   # Color scheme
└── README.md
```

## Configuration

### Window Decoration Settings (MyBreeze-Darkrc)

- **Title Bar Height**: 22px
- **Button Size**: 19.7px × 19px
- **Button Spacing**: 6px
- **Window Borders**: Disabled (0px)
- **Text Alignment**: Center (horizontal and vertical)
- **Animations**: Enabled
- **Active Text Color**: RGB(252, 252, 252) - Off-white
- **Inactive Text Color**: RGB(161, 169, 177) - Muted gray-blue

To customize, edit `MyBreeze-Darkrc` and restart KDE Plasma.

### Color Scheme Customization

The color scheme can be edited at `~/.local/share/color-schemes/MyBreeze-Dark.colors`. Key customization:
- `[Colors:Header][Inactive]` → `ForegroundNormal=161,169,177` (inactive menu text)

## Design Philosophy

MyBreeze-Dark is a hybrid theme that combines:

1. **MyBreeze Layout**: 22px title bar, optimal button spacing, clean proportions
2. **Breeze Dark Colors**: Official KDE color palette from `[WM]` section
3. **No Blue Accents**: Removed blue border lines from original MyBreeze
4. **Consistent Inactive States**: Menu bar text matches window title when unfocused
5. **Aurorae Framework**: Lightweight SVG-based rendering
6. **Modern Aesthetics**: Flat design, minimal borders, smooth transitions

### Key Differences from Stock Themes

**vs. Breeze Dark:**
- Uses MyBreeze's superior spacing and proportions
- Includes matching color scheme with muted inactive menu text

**vs. MyBreeze:**
- Uses Breeze Dark colors instead of blue-gray tones
- Removes blue accent borders
- No window borders by default
- Includes coordinated color scheme

## Button Layout

- **Left Buttons**: Close (X), Minimize (I), Maximize (A)
- **Right Buttons**: None (standard configuration)

## Hover States

- **Standard Buttons**: Bright blue accent (RGB(61, 174, 233))
- **Close Button**: Red (RGB(218, 68, 83))
- **Transition**: Smooth 150-200ms fade

## License

GPLv3 - See LICENSE file for details

## Credits

- **Design**: Inspired by KDE Breeze and MyBreeze themes
- **Colors**: Based on official Breeze Dark color scheme
- **Framework**: Aurorae window decoration system

## Compatibility

- **KDE Plasma**: 5.x and 6.x
- **Window Manager**: KWin
- **Decoration System**: Aurorae

## Troubleshooting

### Theme not appearing in list
- Ensure files are in the correct directory
- Restart KDE Plasma: `kquitapp5 plasmashell && kstart5 plasmashell`

### Colors not applying correctly
- Clear KDE cache: `rm -rf ~/.cache/kde*`
- Restart KDE Plasma

### Buttons not responding
- Check that all SVG files are present
- Verify file permissions (should be readable)

## Changelog

### v1.0 (Current)
- Initial release
- Window decoration with Breeze Dark colors
- Removed blue accent borders from MyBreeze
- Custom color scheme with muted inactive menu text
- No window borders by default
- Proper metadata files for KDE 5 and 6

## Future Enhancements

- [ ] Light variant (MyBreeze-Light)
- [ ] Additional button layout options
- [ ] High-DPI scaling improvements
- [ ] Animation speed customization
- [ ] Optional window border variants

## Support

For issues or suggestions, please refer to the project repository.
