import os
import re

def main():
    svg_path = 'profile-3d-contrib/profile-night-view.svg'
    if not os.path.exists(svg_path):
        svg_path = 'profile-3d-contrib/profile-green.svg'
        if not os.path.exists(svg_path):
            print("No 3D SVG found. Creating a mock empty file to avoid build errors.")
            with open('profile-spiderman.svg', 'w', encoding='utf-8') as f:
                f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300"></svg>')
            return

    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Hide all text elements (months, days, contribution counts labels)
    content = re.sub(r'<text', '<text display="none"', content)

    # 2. Inject CSS overrides to apply Spiderman Red/Blue colors and swinging animation
    css_injection = """
  <style>
    /* Spiderman Color Overrides for 3D Blocks */
    .fill-bg { fill: #0D1117 !important; }
    
    /* Level 0 - Base grid plates */
    .cont-top-0 { fill: #111424 !important; }
    .cont-left-0 { fill: #0B0D18 !important; }
    .cont-right-0 { fill: #07080F !important; }
    
    /* Level 1 - Spiderman Blue */
    .cont-top-1 { fill: #1F4A96 !important; }
    .cont-left-1 { fill: #173770 !important; }
    .cont-right-1 { fill: #112852 !important; }
    
    /* Level 2 - Bright Spiderman Blue */
    .cont-top-2 { fill: #3B82F6 !important; }
    .cont-left-2 { fill: #2563EB !important; }
    .cont-right-2 { fill: #1D4ED8 !important; }
    
    /* Level 3 - Dark Spiderman Red */
    .cont-top-3 { fill: #991B1B !important; }
    .cont-left-3 { fill: #7F1D1D !important; }
    .cont-right-3 { fill: #6B1D1D !important; }
    
    /* Level 4 - Classic Spiderman Red */
    .cont-top-4 { fill: #EF4444 !important; }
    .cont-left-4 { fill: #DC2626 !important; }
    .cont-right-4 { fill: #B91C1C !important; }

    /* Web-swinging Spiderman Animation */
    .spidey-swing-container {
      transform-origin: 640px -180px; /* Pivoted from top-middle */
      animation: spidey-swing 5s infinite ease-in-out;
    }
    @keyframes spidey-swing {
      0% { transform: rotate(-25deg); }
      50% { transform: rotate(25deg); }
      100% { transform: rotate(-25deg); }
    }
    .spidey-web {
      stroke: #EAEAEA;
      stroke-width: 1.5;
      stroke-opacity: 0.7;
      stroke-dasharray: 4 4;
    }
  </style>
    """
    
    # Insert styles before the closing </style> tag in the file
    content = content.replace('</style>', css_injection + '\n</style>')

    # 3. Inject the swinging Spiderman vector elements before the closing </svg> tag
    # In the 3D grid, the center is around x=640 (since the viewBox is 1280x850).
    spidey_vector = """
  <g class="spidey-swing-container">
    <!-- Web line hanging from a pivot point above the city -->
    <line x1="640" y1="-180" x2="640" y2="280" class="spidey-web" />
    
    <!-- Spiderman Character (centered at local x=640, y=280) -->
    <g transform="translate(640, 280) scale(1.6)">
      <!-- Torso -->
      <ellipse cx="0" cy="14" rx="7" ry="11" fill="#EF4444" />
      <path d="M-7,10 L-4,25 L4,25 L7,10 Z" fill="#1F4A96" />
      <line x1="0" y1="9" x2="0" y2="15" stroke="#000000" stroke-width="1" />
      <path d="M-3,10 L3,14 M-3,14 L3,10" stroke="#000000" stroke-width="0.8" />
      
      <!-- Head -->
      <circle cx="0" cy="0" r="9" fill="#EF4444" stroke="#B91C1C" stroke-width="0.8" />
      <path d="M-6,-2 Q-3,-5 -1,-2 Q-3,1 -6,-2 Z" fill="#FFFFFF" stroke="#111424" stroke-width="1.2" />
      <path d="M6,-2 Q3,-5 1,-2 Q3,1 6,-2 Z" fill="#FFFFFF" stroke="#111424" stroke-width="1.2" />
      
      <!-- Arms -->
      <path d="M-5,8 Q-12,-5 0,-85" stroke="#FFFFFF" stroke-width="1.2" fill="none" opacity="0.6" />
      <path d="M5,8 Q12,3 15,-5" stroke="#EF4444" stroke-width="2.2" fill="none" stroke-linecap="round" />
      
      <!-- Legs -->
      <path d="M-3,24 Q-9,33 -4,39" stroke="#1F4A96" stroke-width="2.5" fill="none" stroke-linecap="round" />
      <path d="M3,24 Q9,33 4,39" stroke="#1F4A96" stroke-width="2.5" fill="none" stroke-linecap="round" />
    </g>
  </g>
</svg>
    """
    content = re.sub(r'</svg>\s*$', spidey_vector, content)

    with open('profile-spiderman.svg', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Spiderman 3D city theme and swing animation applied successfully!")

if __name__ == '__main__':
    main()
