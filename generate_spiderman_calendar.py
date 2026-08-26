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
    
    # CSS Animations
    svg.append("""  <style>
    /* Swinging Animation */
    .swing-container {
      transform-origin: 417px -120px;
      animation: swing 5s infinite ease-in-out;
    }
    @keyframes swing {
      0% { transform: rotate(-25deg); }
      50% { transform: rotate(25deg); }
      100% { transform: rotate(-25deg); }
    }
    
    /* Web line styling */
    .web-line {
      stroke: #EAEAEA;
      stroke-width: 1.2;
      stroke-opacity: 0.6;
      stroke-dasharray: 3 3;
    }
    
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
            
    # Add swinging Spiderman (hanging from a web pivot above the grid)
    # The pivot point is centered horizontally at x=417 and y=-120
    svg.append('  <g class="swing-container">')
    # Web line from pivot down to Spiderman
    svg.append('    <line x1="417" y1="-120" x2="417" y2="85" class="web-line" />')
    
    # Spiderman character group (centered at local coordinate x=417, y=85)
    svg.append('    <g transform="translate(417, 85) scale(1.1)">')
    # Torso
    svg.append('      <ellipse cx="0" cy="14" rx="7" ry="11" fill="#EF4444" />')
    svg.append('      <path d="M-7,10 L-4,25 L4,25 L7,10 Z" fill="#1F4A96" />')
    svg.append('      <line x1="0" y1="9" x2="0" y2="15" stroke="#000000" stroke-width="1" />')
    svg.append('      <path d="M-3,10 L3,14 M-3,14 L3,10" stroke="#000000" stroke-width="0.8" />')
    
    # Head
    svg.append('      <circle cx="0" cy="0" r="9" fill="#EF4444" stroke="#B91C1C" stroke-width="0.8" />')
    # Spiderman eyes
    svg.append('      <path d="M-6,-2 Q-3,-5 -1,-2 Q-3,1 -6,-2 Z" fill="#FFFFFF" stroke="#111424" stroke-width="1.2" />')
    svg.append('      <path d="M6,-2 Q3,-5 1,-2 Q3,1 6,-2 Z" fill="#FFFFFF" stroke="#111424" stroke-width="1.2" />')
    
    # Arms
    svg.append('      <path d="M-5,8 Q-12,-5 0,-85" stroke="#FFFFFF" stroke-width="1.2" fill="none" opacity="0.6" />')
    svg.append('      <path d="M5,8 Q12,3 15,-5" stroke="#EF4444" stroke-width="2.2" fill="none" stroke-linecap="round" />')
    
    # Legs
    svg.append('      <path d="M-3,24 Q-9,33 -4,39" stroke="#1F4A96" stroke-width="2.5" fill="none" stroke-linecap="round" />')
    svg.append('      <path d="M3,24 Q9,33 4,39" stroke="#1F4A96" stroke-width="2.5" fill="none" stroke-linecap="round" />')
    
    svg.append('    </g>')
    svg.append('  </g>')
    
    svg.append('</svg>')
    
    output = "\n".join(svg)
    with open("profile-spiderman.svg", "w", encoding="utf-8") as f:
        f.write(output)
    print("profile-spiderman.svg generated successfully with Spiderman face and swing animation!")

if __name__ == "__main__":
    generate_spiderman_graph()
