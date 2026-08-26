import os
import re

def main():
    svg_path = 'profile-3d-contrib/profile-night-view.svg'
    if not os.path.exists(svg_path):
        svg_path = 'profile-3d-contrib/profile-green.svg'
        if not os.path.exists(svg_path):
            print("No 3D SVG found. Creating a mock empty file to avoid build errors.")
            # If no files exist yet, we write a simple empty placeholder
            with open('profile-spiderman.svg', 'w', encoding='utf-8') as f:
                f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300"></svg>')
            return

    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Hide all text elements (months, days, contribution counts labels)
    content = re.sub(r'<text', '<text display="none"', content)

    # 2. Recolor the 3D buildings and base plates to Spiderman theme (Red & Blue)
    replacements = {
        '#161b22': '#111424', # Darker base plate
        '#0e4429': '#1F4A96', # Level 1 -> Spiderman Blue
        '#006d32': '#3B82F6', # Level 2 -> Bright Spiderman Blue
        '#26a641': '#991B1B', # Level 3 -> Dark Spiderman Red
        '#39d353': '#EF4444', # Level 4 -> Classic Spiderman Red
        
        # Light mode colors if present
        '#ebedf0': '#111424',
        '#9be9a8': '#1F4A96',
        '#40c463': '#3B82F6',
        '#30a14e': '#991B1B',
        '#216e39': '#EF4444',
    }
    
    for src, dst in replacements.items():
        content = re.sub(src, dst, content, flags=re.IGNORECASE)

    # 3. Inject CSS for Spiderman swinging animation
    css_injection = """
  <style>
    .spidey-swing-container {
      transform-origin: 400px -150px;
      animation: spidey-swing 6s infinite ease-in-out;
    }
    @keyframes spidey-swing {
      0% { transform: rotate(-30deg); }
      50% { transform: rotate(30deg); }
      100% { transform: rotate(-30deg); }
    }
    .spidey-web {
      stroke: #FFFFFF;
      stroke-width: 1.2;
      stroke-opacity: 0.6;
      stroke-dasharray: 3 3;
    }
  </style>
    """
    content = content.replace('</style>', '</style>' + css_injection)

    # 4. Inject the swinging Spiderman vector elements before the closing </svg> tag
    spidey_vector = """
  <g class="spidey-swing-container">
    <!-- Web line hanging from a pivot point above the city -->
    <line x1="400" y1="-150" x2="400" y2="120" class="spidey-web" />
    
    <!-- Spiderman Character (centered at local x=400, y=120) -->
    <g transform="translate(400, 120) scale(0.95)">
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
