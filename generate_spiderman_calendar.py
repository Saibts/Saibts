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
    # B = Black (#111424)
    # W = White (#FFFFFF)
    # . = Background contribution block
    template = [
        ".....RRRRRRRRR.....",
        "...RRRRRRRRRRRRR...",
        "..RRRBBBRRRBBBRRR..",
        ".RRRBWWWB B BWWWB R R R.",
        ".RRRRBWWBRBWWB R R R R.",
        "..RRRRBBRRRBBRRRR..",
        "....RRRRRRRRRRR...."
    ]
    
    # Clean template strings
    template = [line.replace(" ", "") for line in template]
    
    # Colors
    color_bg = "#0D1117"
    color_red = "#EF4444"
    color_black = "#111424" # Dark slate/black for eyes outline
    color_white = "#FFFFFF"
    
    # Standard active contribution colors for the background noise
    noise_colors = ["#161B22", "#161B22", "#161B22", "#1F4A96", "#3B82F6", "#161B22"]
    
    svg = []
    # Adjust height since we removed headers (just need grid height + labels)
    svg_width = 835
    svg_height = 145
    padding_left = 35
    padding_top = 20
    
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="100%" height="100%">')
    svg.append(f'  <rect width="100%" height="100%" fill="{color_bg}" rx="10" />')
    
    # CSS Animations for the grid cells
    svg.append("""  <style>
    .cell {
      transform-origin: center;
      animation: popIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) both;
    }
    .spidey-cell {
      animation: popIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) both, glowPulse 3s infinite alternate;
    }
    @keyframes popIn {
      0% {
        opacity: 0;
        transform: scale(0.3);
      }
      100% {
        opacity: 1;
        transform: scale(1);
      }
    }
    @keyframes glowPulse {
      0% {
        filter: drop-shadow(0 0 0px rgba(239, 68, 68, 0));
      }
      100% {
        filter: drop-shadow(0 0 3px rgba(239, 68, 68, 0.8));
      }
    }
  </style>""")
    
    # Generate cells
    for col in range(cols):
        for row in range(rows):
            # Calculate coordinates
            x = padding_left + col * 15
            y = padding_top + row * 15
            
            # Default cell color
            cell_color = random.choice(noise_colors)
            is_spidey = False
            
            # Check if this cell falls within the Spiderman template coordinates
            if start_col <= col < start_col + 19:
                t_col = col - start_col
                char = template[row][t_col]
                
                if char == 'R':
                    cell_color = color_red
                    is_spidey = True
                elif char == 'B':
                    cell_color = color_black
                elif char == 'W':
                    cell_color = color_white
            
            # Delay calculations for wave animation effect (crawls from left to right)
            delay_ms = col * 25 + row * 15
            cls = "spidey-cell" if is_spidey else "cell"
            
            # Add rect element with inline delay
            svg.append(f'  <rect class="{cls}" x="{x}" y="{y}" width="11" height="11" rx="2" ry="2" fill="{cell_color}" style="animation-delay: {delay_ms}ms; transform-box: fill-box;" />')
            
    # Add calendar labels (months and days)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for i, month in enumerate(months):
        mx = padding_left + int(i * (cols * 15 / 12))
        svg.append(f'  <text x="{mx}" y="{padding_top - 6}" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9px">{month}</text>')
        
    days = ["Mon", "Wed", "Fri"]
    for i, day in enumerate(days):
        dy = padding_top + 10 + i * 30
        svg.append(f'  <text x="{padding_left - 28}" y="{dy}" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9px">{day}</text>')
        
    svg.append('</svg>')
    
    output = "\n".join(svg)
    with open("profile-spiderman.svg", "w", encoding="utf-8") as f:
        f.write(output)
    print("profile-spiderman.svg generated successfully with Spiderman animation!")

if __name__ == "__main__":
    generate_spiderman_graph()
