def generate_game_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 240" width="100%" height="100%">
  <style>
    .bg { fill: #0D1117; rx: 10px; }
    .grid { stroke: #1F2937; stroke-width: 0.8; }
    .title { fill: #58A6FF; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; font-size: 15px; font-weight: 600; }
    .instructions { fill: #8B949E; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; font-size: 11px; }
    
    /* System Status Texts */
    .status-text { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; font-size: 12px; font-weight: bold; }
    .status-alert { fill: #FF7B72; animation: flash 1s infinite alternate; }
    .status-stable { fill: #56D364; opacity: 0; }
    
    /* Warning Panel */
    .warning-panel { fill: rgba(248, 81, 73, 0.1); stroke: #F85149; stroke-width: 1.5; rx: 6px; }
    .stable-panel { fill: rgba(56, 211, 100, 0.1); stroke: #3fb950; stroke-width: 1.5; rx: 6px; opacity: 0; }
    
    /* The Bug - Target */
    .bug-wrapper {
      animation: fly 14s infinite linear;
      transform-box: fill-box;
      transform-origin: center;
      cursor: crosshair;
    }
    .bug-body { fill: #FF7B72; filter: drop-shadow(0 0 6px #F85149); transition: fill 0.2s, filter 0.2s; }
    .bug-legs { stroke: #FF7B72; stroke-width: 1.5; fill: none; transition: stroke 0.2s; }
    
    /* Interactive State on Hover */
    .game-container:hover .bug-wrapper {
      animation-play-state: paused;
    }
    .bug-wrapper:hover .bug-body {
      fill: #56D364;
      filter: drop-shadow(0 0 10px #3fb950);
    }
    .bug-wrapper:hover .bug-legs {
      stroke: #56D364;
    }
    
    /* Display state adjustments on Hover */
    .bug-wrapper:hover ~ .status-alert { opacity: 0; animation: none; }
    .bug-wrapper:hover ~ .status-stable { opacity: 1; }
    .bug-wrapper:hover ~ .warning-panel { opacity: 0; }
    .bug-wrapper:hover ~ .stable-panel { opacity: 1; }
    
    /* Keyframes for random flying path */
    @keyframes fly {
      0%   { transform: translate(100px, 60px); }
      10%  { transform: translate(350px, 140px); }
      20%  { transform: translate(600px, 50px); }
      30%  { transform: translate(250px, 120px); }
      40%  { transform: translate(500px, 80px); }
      50%  { transform: translate(150px, 150px); }
      60%  { transform: translate(580px, 130px); }
      70%  { transform: translate(300px, 60px); }
      80%  { transform: translate(620px, 90px); }
      90%  { transform: translate(200px, 80px); }
      100% { transform: translate(100px, 60px); }
    }
    
    @keyframes flash {
      0% { opacity: 0.3; }
      100% { opacity: 1; }
    }
  </style>
  
  <g class="game-container">
    <rect width="100%" height="100%" class="bg" />
    
    <!-- Grid -->
    <g class="grid">
      <line x1="80" y1="0" x2="80" y2="240" />
      <line x1="160" y1="0" x2="160" y2="240" />
      <line x1="240" y1="0" x2="240" y2="240" />
      <line x1="320" y1="0" x2="320" y2="240" />
      <line x1="400" y1="0" x2="400" y2="240" />
      <line x1="480" y1="0" x2="480" y2="240" />
      <line x1="560" y1="0" x2="560" y2="240" />
      <line x1="640" y1="0" x2="640" y2="240" />
      <line x1="720" y1="0" x2="720" y2="240" />
      <line x1="0" y1="60" x2="800" y2="60" />
      <line x1="0" y1="120" x2="800" y2="120" />
      <line x1="0" y1="180" x2="800" y2="180" />
    </g>

    <!-- Header info -->
    <text x="25" y="32" class="title">🎮 Catch the Bug Game</text>
    <text x="25" y="48" class="instructions">Hover your mouse pointer over the moving bug to debug the system!</text>

    <!-- Panels -->
    <rect x="420" y="15" width="350" height="35" class="warning-panel" />
    <rect x="420" y="15" width="350" height="35" class="stable-panel" />

    <!-- Bug Object -->
    <g class="bug-wrapper">
      <!-- Bug Shape -->
      <!-- Legs -->
      <path d="M-8,-4 L-14,-8 M-8,0 L-15,0 M-8,4 L-14,8 M8,-4 L14,-8 M8,0 L15,0 M8,4 L14,8" class="bug-legs" />
      <!-- Body -->
      <ellipse cx="0" cy="0" rx="8" ry="11" class="bug-body" />
      <!-- Head -->
      <circle cx="0" cy="-13" r="4.5" class="bug-body" />
      <!-- Antennae -->
      <path d="M-2,-16 Q-6,-22 -10,-20 M2,-16 Q6,-22 10,-20" stroke="#FF7B72" stroke-width="1" fill="none" class="bug-legs" />
    </g>

    <!-- System Status Texts (Positioned relative to the panels) -->
    <!-- Alert State -->
    <g class="status-alert">
      <text x="440" y="37" class="status-text">⚠️ SYSTEM STATUS: UNSTABLE (1 BUG)</text>
    </g>
    <!-- Stable State -->
    <g class="status-stable">
      <text x="440" y="37" class="status-text">✅ SYSTEM DEBUGGED: 100% STABLE (+100 XP)</text>
    </g>
  </g>
</svg>"""
    with open("bug-hunt.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("bug-hunt.svg generated successfully!")

if __name__ == "__main__":
    generate_game_svg()
