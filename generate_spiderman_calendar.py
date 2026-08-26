import random

def generate_spiderman_graph():
    # Grid config
    cols = 53
    rows = 7
    
    # Define the 19-column Spiderman face template centered in the 53 columns
    # We will offset it horizontally so it centers perfectly: start_col = (53 - 19) // 2 = 17
    start_col = 17
    
    # 19x7 Template for Spiderman mask:
    # R = Red (#EF4444)
    # B = Black (#1F1F1F)
    # W = White (#FFFFFF)
    # . = Background contribution block
    template = [
        # Row 0
        ".....RRRRRRRRR.....",
        # Row 1
        "...RRRRRRRRRRRRR...",
        # Row 2
        "..RRRBBBRRRBBBRRR..",
        # Row 3
        ".RRRBWWWB B BWWWB R R R.",
        # Row 4
        ".RRRRBWWBRBWWB R R R R.",
        # Row 5
        "..RRRRBBRRRBBRRRR..",
        # Row 6
        "....RRRRRRRRRRR...."
    ]
    
    # Clean template strings (remove spaces)
    template = [line.replace(" ", "") for line in template]
    
    # Colors
    color_bg = "#0D1117"
    color_empty = "#161B22"
    color_red = "#EF4444"
    color_black = "#111424" # Dark slate/black for eyes outline
    color_white = "#FFFFFF"
    
    # Standard active contribution colors for the background noise
    # Mix of level 1, 2, 3 blues and grays to blend nicely with Spiderman theme
    noise_colors = ["#161B22", "#161B22", "#161B22", "#1F4A96", "#3B82F6", "#161B22"]
    
    svg = []
    svg_width = 860
    svg_height = 240
    padding_left = 40
    padding_top = 70
    
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="100%" height="100%">')
    svg.append(f'  <rect width="100%" height="100%" fill="{color_bg}" rx="10" />')
    
    # Headers
    svg.append(f'  <text x="25" y="35" fill="{color_red}" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="16px" font-weight="bold">🕷️ Spiderman Contribution Calendar</text>')
    svg.append(f'  <text x="25" y="52" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11px">A custom-rendered contribution graph layout representing the web-slinger.</text>')
    
    # Generate cells
    for col in range(cols):
        for row in range(rows):
            # Calculate coordinates
            x = padding_left + col * 15
            y = padding_top + row * 15
            
            # Default cell color
            cell_color = random.choice(noise_colors)
            
            # Check if this cell falls within the Spiderman template coordinates
            if start_col <= col < start_col + 19:
                t_col = col - start_col
                char = template[row][t_col]
                
                if char == 'R':
                    cell_color = color_red
                elif char == 'B':
                    cell_color = color_black
                elif char == 'W':
                    cell_color = color_white
            
            # Add rect element
            svg.append(f'  <rect x="{x}" y="{y}" width="11" height="11" rx="2" ry="2" fill="{cell_color}" />')
            
    # Add calendar labels (months and days)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for i, month in enumerate(months):
        mx = padding_left + int(i * (cols * 15 / 12))
        svg.append(f'  <text x="{mx}" y="{padding_top - 8}" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9px">{month}</text>')
        
    days = ["Mon", "Wed", "Fri"]
    for i, day in enumerate(days):
        dy = padding_top + 10 + i * 30
        svg.append(f'  <text x="{padding_left - 28}" y="{dy}" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9px">{day}</text>')
        
    svg.append('</svg>')
    
    output = "\n".join(svg)
    with open("profile-spiderman.svg", "w", encoding="utf-8") as f:
        f.write(output)
    print("profile-spiderman.svg generated successfully with Spiderman pixel art!")

if __name__ == "__main__":
    generate_spiderman_graph()
