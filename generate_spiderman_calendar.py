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
    noise_colors = ["#161B22", "#161B22", "#161B22", "#1F4A96", "#3B82F6", "#161B22", "#161B22"]
    
    svg = []
    svg_width = 835
    svg_height = 160
    padding_left = 20
    padding_top = 28
    
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="100%" height="100%">')
    svg.append(f'  <rect width="100%" height="100%" fill="{color_bg}" rx="10" />')
    
    # CSS Animations for pop-in effect
    svg.append("""  <style>
    /* Subtle background grid fade-in */
    .cell {
      transform-origin: center;
      animation: fadeIn 1s ease-out both;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.8); }
      to { opacity: 1; transform: scale(1); }
    }
  </style>""")
    
    # Generate calendar cells
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
            
            delay_ms = col * 15 + row * 10
            svg.append(f'  <rect class="cell" x="{x}" y="{y}" width="11" height="11" rx="2" ry="2" fill="{cell_color}" style="animation-delay: {delay_ms}ms; transform-box: fill-box;" />')
            
    svg.append('</svg>')
    
    output = "\n".join(svg)
    with open("profile-spiderman.svg", "w", encoding="utf-8") as f:
        f.write(output)
    print("profile-spiderman.svg generated successfully with Spiderman face only!")

if __name__ == "__main__":
    generate_spiderman_graph()
