import random

def generate_spiderman_graph():
    # Grid config
    cols = 53
    rows = 7
    
    # Colors
    color_bg = "#0D1117"
    
    # Standard active contribution colors for the background noise
    # Mix of dark slate, spiderman blue, and light blue blocks
    noise_colors = ["#161B22", "#161B22", "#161B22", "#1F4A96", "#3B82F6", "#161B22", "#EF4444", "#161B22"]
    
    svg = []
    svg_width = 835
    svg_height = 160
    padding_left = 20
    padding_top = 35
    
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
      0% { transform: rotate(-28deg); }
      50% { transform: rotate(28deg); }
      100% { transform: rotate(-28deg); }
    }
    
    /* Web shooter dynamic line */
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
    
    # Generate calendar cells (without any text headers/labels)
    for col in range(cols):
        for row in range(rows):
            # Calculate coordinates
            x = padding_left + col * 15
            y = padding_top + row * 15
            
            # Choose random color for background noise
            cell_color = random.choice(noise_colors)
            delay_ms = col * 15 + row * 10
            
            svg.append(f'  <rect class="cell" x="{x}" y="{y}" width="11" height="11" rx="2" ry="2" fill="{cell_color}" style="animation-delay: {delay_ms}ms; transform-box: fill-box;" />')
            
    # Add swinging Spiderman (hanging from a web pivot above the grid)
    # The pivot point is centered horizontally at x=417 (middle of 835 width) and y=-120
    svg.append('  <g class="swing-container">')
    # Web line from pivot down to Spiderman
    svg.append('    <line x1="417" y1="-120" x2="417" y2="85" class="web-line" />')
    
    # Spiderman character group (centered at local coordinate x=417, y=85)
    svg.append('    <g transform="translate(417, 85)">')
    # Torso (Blue and Red suit details)
    svg.append('      <ellipse cx="0" cy="14" rx="7" ry="11" fill="#EF4444" />')
    svg.append('      <path d="M-7,10 L-4,25 L4,25 L7,10 Z" fill="#1F4A96" />')
    # Spider emblem on chest
    svg.append('      <line x1="0" y1="9" x2="0" y2="15" stroke="#000000" stroke-width="1" />')
    svg.append('      <path d="M-3,10 L3,14 M-3,14 L3,10" stroke="#000000" stroke-width="0.8" />')
    
    # Head
    svg.append('      <circle cx="0" cy="0" r="9" fill="#EF4444" stroke="#B91C1C" stroke-width="0.8" />')
    # Spiderman eyes
    svg.append('      <path d="M-6,-2 Q-3,-5 -1,-2 Q-3,1 -6,-2 Z" fill="#FFFFFF" stroke="#111424" stroke-width="1.2" />')
    svg.append('      <path d="M6,-2 Q3,-5 1,-2 Q3,1 6,-2 Z" fill="#FFFFFF" stroke="#111424" stroke-width="1.2" />')
    
    # Arms holding the web (climbing/swinging pose)
    svg.append('      <path d="M-5,8 Q-12,-5 0,-85" stroke="#FFFFFF" stroke-width="1.2" fill="none" opacity="0.6" />')
    svg.append('      <path d="M5,8 Q12,3 15,-5" stroke="#EF4444" stroke-width="2.2" fill="none" stroke-linecap="round" />')
    
    # Legs (hanging/bent in motion)
    svg.append('      <path d="M-3,24 Q-9,33 -4,39" stroke="#1F4A96" stroke-width="2.5" fill="none" stroke-linecap="round" />')
    svg.append('      <path d="M3,24 Q9,33 4,39" stroke="#1F4A96" stroke-width="2.5" fill="none" stroke-linecap="round" />')
    
    svg.append('    </g>')
    svg.append('  </g>')
    
    svg.append('</svg>')
    
    output = "\n".join(svg)
    with open("profile-spiderman.svg", "w", encoding="utf-8") as f:
        f.write(output)
    print("profile-spiderman.svg generated successfully with swinging Spiderman!")

if __name__ == "__main__":
    generate_spiderman_graph()
