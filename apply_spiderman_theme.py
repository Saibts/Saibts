import os
import re

def main():
    # Look for the generated 3D contribution graph SVGs
    svg_path = 'profile-3d-contrib/profile-night-view.svg'
    if not os.path.exists(svg_path):
        svg_path = 'profile-3d-contrib/profile-green.svg'
        if not os.path.exists(svg_path):
            print("No 3D SVG files found. Make sure the 3D contribution action runs first.")
            return

    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define color mappings from standard GitHub Green palette to Spiderman theme
    # GitHub colors:
    # #161b22 -> Level 0 (Dark Gray plate)
    # #0e4429 -> Level 1 (Dark Green)
    # #006d32 -> Level 2 (Medium Green)
    # #26a641 -> Level 3 (Light Green)
    # #39d353 -> Level 4 (Bright Green)
    #
    # Spiderman colors (Deep Blue & Red):
    # #161b22 -> #111424 (Darker blue-gray plate)
    # #0e4429 -> #1F4A96 (Classic Spiderman Blue)
    # #006d32 -> #3B82F6 (Light/Bright Spiderman Blue)
    # #26a641 -> #991B1B (Spiderman Dark Red)
    # #39d353 -> #EF4444 (Classic Spiderman Red)
    
    replacements = {
        # Dark mode colors
        '#161b22': '#111424',
        '#0e4429': '#1F4A96',
        '#006d32': '#3B82F6',
        '#26a641': '#991B1B',
        '#39d353': '#EF4444',
        
        # Light mode colors (in case the fallback is used)
        '#ebedf0': '#111424',
        '#9be9a8': '#1F4A96',
        '#40c463': '#3B82F6',
        '#30a14e': '#991B1B',
        '#216e39': '#EF4444',
    }

    # Perform case-insensitive replacement
    for src, dst in replacements.items():
        content = re.sub(src, dst, content, flags=re.IGNORECASE)

    # Save the modified SVG
    with open('profile-spiderman.svg', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Spiderman 3D theme applied successfully to profile-spiderman.svg!")

if __name__ == '__main__':
    main()
