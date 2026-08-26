def generate_spiderman_only():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 220" width="100%" height="100%">
  <style>
    .bg { fill: #0D1117; rx: 10px; }
    
    /* Web swinging keyframes */
    .swing-container {
      transform-origin: 400px -120px;
      animation: swing 4.5s infinite ease-in-out;
    }
    @keyframes swing {
      0% { transform: rotate(-28deg); }
      50% { transform: rotate(28deg); }
      100% { transform: rotate(-28deg); }
    }
    
    .web-line {
      stroke: #EAEAEA;
      stroke-width: 1.5;
      stroke-opacity: 0.7;
      stroke-dasharray: 4 4;
    }
    
    /* Web shooter particle elements */
    .web-shoot {
      stroke: #FFFFFF;
      stroke-width: 1;
      opacity: 0.8;
      stroke-dasharray: 2 4;
    }
  </style>
  
  <rect width="100%" height="100%" class="bg" />
  
  <!-- Web swinging Spiderman group -->
  <g class="swing-container">
    <!-- Main web line to pivot -->
    <line x1="400" y1="-120" x2="400" y2="120" class="web-line" />
    
    <!-- Spiderman Character (centered at local x=400, y=120) -->
    <g transform="translate(400, 120) scale(1.4)">
      <!-- Torso / suit -->
      <ellipse cx="0" cy="14" rx="7" ry="11" fill="#EF4444" />
      <path d="M-7,10 L-4,25 L4,25 L7,10 Z" fill="#1F4A96" />
      
      <!-- Spider logo on chest -->
      <line x1="0" y1="9" x2="0" y2="15" stroke="#000000" stroke-width="1" />
      <path d="M-3,10 L3,14 M-3,14 L3,10" stroke="#000000" stroke-width="0.8" />
      
      <!-- Head -->
      <circle cx="0" cy="0" r="9" fill="#EF4444" stroke="#B91C1C" stroke-width="0.8" />
      <path d="M-6,-2 Q-3,-5 -1,-2 Q-3,1 -6,-2 Z" fill="#FFFFFF" stroke="#111424" stroke-width="1.2" />
      <path d="M6,-2 Q3,-5 1,-2 Q3,1 6,-2 Z" fill="#FFFFFF" stroke="#111424" stroke-width="1.2" />
      
      <!-- Arms in swinging pose -->
      <path d="M-5,8 Q-12,-5 0,-85" stroke="#FFFFFF" stroke-width="1.2" fill="none" opacity="0.6" />
      <path d="M5,8 Q12,3 15,-5" stroke="#EF4444" stroke-width="2.2" fill="none" stroke-linecap="round" />
      
      <!-- Legs (bent dynamically in motion) -->
      <path d="M-3,24 Q-9,33 -4,39" stroke="#1F4A96" stroke-width="2.5" fill="none" stroke-linecap="round" />
      <path d="M3,24 Q9,33 4,39" stroke="#1F4A96" stroke-width="2.5" fill="none" stroke-linecap="round" />
    </g>
  </g>
</svg>"""
    with open("profile-spiderman.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("profile-spiderman.svg generated successfully with Spiderman only!")

if __name__ == "__main__":
    generate_spiderman_only()
