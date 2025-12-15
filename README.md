# MyBreeze-Dark Window Decoration

A modern, dark window decoration theme for KDE Plasma that combines the best of MyBreeze and Breeze design philosophies.

## Features

- **Dark, Professional Aesthetic**: Based on Breeze Dark color scheme
- **Clean, Minimal Design**: No window borders by default
- **Smooth Animations**: Subtle transitions between window states
- **Accent Color Support**: Respects system accent color settings
- **Aurorae-Based**: Lightweight SVG-based implementation
- **Modern Proportions**: 22px title bar with optimal spacing

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

## File Structure

```
aurorae/MyBreeze-Dark/
├── metadata.json              # Plugin metadata
├── MyBreeze-Dark.rc          # Configuration file
├── decoration.svg            # Main window frame
├── close.svg                 # Close button
├── minimize.svg              # Minimize button
├── maximize.svg              # Maximize button
├── restore.svg               # Restore button
├── help.svg                  # Help button
├── shade.svg                 # Shade button
├── keepabove.svg             # Keep above button
├── keepbelow.svg             # Keep below button
└── alldesktops.svg           # All desktops button
```

## Configuration

The theme is configured via `MyBreeze-Dark.rc`:

- **Title Bar Height**: 22px
- **Button Size**: 19.7px × 19px
- **Button Spacing**: 6px
- **Window Borders**: Disabled (0px)
- **Text Alignment**: Center
- **Animations**: Enabled

To customize, edit the `.rc` file and restart KDE Plasma.

## Design Philosophy

MyBreeze-Dark is a hybrid theme that:

1. **Uses Aurorae Framework**: For quick customization and lightweight rendering
2. **Adopts Breeze Colors**: For system consistency and modern aesthetics
3. **Maintains Clean Design**: Minimal borders and flat surfaces
4. **Supports Theming**: Respects system color schemes and accent colors
5. **Provides Smooth Interactions**: Subtle animations and transitions

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

## Future Enhancements

- [ ] Light variant (MyBreeze-Light)
- [ ] Custom accent color support
- [ ] Additional button styles
- [ ] High-DPI scaling improvements
- [ ] Animation customization options

## Support

For issues or suggestions, please refer to the project repository.
