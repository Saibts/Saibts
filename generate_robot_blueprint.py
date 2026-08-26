def generate_robot_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 320" width="100%" height="100%">
  <style>
    .bg { fill: #0D1117; rx: 10px; }
    .title { fill: #58A6FF; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; font-size: 16px; font-weight: 600; }
    .subtitle { fill: #8B949E; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; font-size: 11px; }
    
    /* Blueprint style graphics */
    .blueprint-grid { stroke: #161B22; stroke-width: 1; }
    .blueprint-line { stroke: #1F2937; stroke-width: 1.5; fill: none; }
    .robot-body { fill: #161B22; stroke: #30363D; stroke-width: 2; }
    .robot-accent { fill: none; stroke: #00E5FF; stroke-width: 2; opacity: 0.8; }
    .robot-wheel { fill: #0D1117; stroke: #30363D; stroke-width: 3; }
    
    /* Hotspots & Interactivity */
    .hotspot { cursor: pointer; }
    .hotspot-ring { fill: none; stroke: #00E5FF; stroke-width: 1.5; transform-origin: center; animation: pulse 2s infinite; }
    .hotspot-center { fill: #00E5FF; stroke: #0D1117; stroke-width: 1.5; transition: all 0.3s ease; }
    
    /* Connection lines pointing to info panel */
    .connector-line { stroke: #00E5FF; stroke-width: 1.5; stroke-dasharray: 4 4; fill: none; opacity: 0; transition: opacity 0.3s ease, stroke-dashoffset 0.5s linear; stroke-dashoffset: 0; }
    
    /* Tooltip Info Panels on the right (x=450, y=70) */
    .info-panel { opacity: 0; pointer-events: none; transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s ease; transform: translateX(10px); }
    .info-header { fill: #00E5FF; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: 14px; font-weight: bold; }
    .info-sub { fill: #58A6FF; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: 11px; font-weight: 600; }
    .info-body { fill: #C9D1D9; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: 11px; }
    .info-label { fill: #8B949E; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: 11px; font-weight: 500; }
    
    .default-panel { opacity: 1; transition: opacity 0.3s ease; }
    .default-text { fill: #8B949E; font-family: -apple-system, sans-serif; font-size: 12px; }
    
    /* Hover triggers */
    .hotspot:hover .hotspot-center { r: 7px; fill: #FFFFFF; filter: drop-shadow(0 0 6px #00E5FF); }
    
    /* Show specific panels on hover */
    #hs-lidar:hover ~ #panel-lidar,
    #hs-camera:hover ~ #panel-camera,
    #hs-brain:hover ~ #panel-brain,
    #hs-chassis:hover ~ #panel-chassis { opacity: 1; transform: translateX(0); }
    
    #hs-lidar:hover ~ #line-lidar,
    #hs-camera:hover ~ #line-camera,
    #hs-brain:hover ~ #line-brain,
    #hs-chassis:hover ~ #line-chassis { opacity: 0.8; stroke-dashoffset: -10; animation: dash 1s infinite linear; }
    
    /* Hide default panel when hovering any hotspot */
    .interactive-group:hover #panel-default { opacity: 0; }
    
    @keyframes pulse {
      0% { r: 5px; opacity: 1; }
      100% { r: 16px; opacity: 0; }
    }
    @keyframes dash {
      to { stroke-dashoffset: -20; }
    }
  </style>
  
  <rect width="100%" height="100%" class="bg" />
  
  <!-- Header -->
  <text x="25" y="32" class="title">🤖 Interactive Hardware/Software Stack</text>
  <text x="25" y="50" class="subtitle">Hover over components to view control architectures &amp; software integration</text>
  
  <!-- Grid background on the left -->
  <g class="blueprint-grid">
    <line x1="40" y1="70" x2="380" y2="70" stroke="#161B22" />
    <line x1="40" y1="120" x2="380" y2="120" stroke="#161B22" />
    <line x1="40" y1="170" x2="380" y2="170" stroke="#161B22" />
    <line x1="40" y1="220" x2="380" y2="220" stroke="#161B22" />
    <line x1="40" y1="270" x2="380" y2="270" stroke="#161B22" />
    
    <line x1="40" y1="70" x2="40" y2="270" stroke="#161B22" />
    <line x1="125" y1="70" x2="125" y2="270" stroke="#161B22" />
    <line x1="210" y1="70" x2="210" y2="270" stroke="#161B22" />
    <line x1="295" y1="70" x2="295" y2="270" stroke="#161B22" />
    <line x1="380" y1="70" x2="380" y2="270" stroke="#161B22" />
  </g>

  <!-- Interactive Group Wrapper -->
  <g class="interactive-group">
    
    <!-- ROBOT BLUEPRINT GRAPHICS (Top-down / isometric style mobile platform) -->
    <g transform="translate(40, 20)">
      <!-- Main Chassis Frame -->
      <rect x="80" y="100" width="160" height="100" rx="15" class="robot-body" />
      <rect x="90" y="110" width="140" height="80" rx="10" class="blueprint-line" />
      
      <!-- Wheels -->
      <!-- Top Left -->
      <rect x="60" y="80" width="40" height="30" rx="5" class="robot-wheel" />
      <line x1="80" y1="85" x2="80" y2="105" stroke="#30363D" />
      <!-- Bottom Left -->
      <rect x="60" y="190" width="40" height="30" rx="5" class="robot-wheel" />
      <line x1="80" y1="195" x2="80" y2="215" stroke="#30363D" />
      <!-- Top Right -->
      <rect x="220" y="80" width="40" height="30" rx="5" class="robot-wheel" />
      <line x1="240" y1="85" x2="240" y2="105" stroke="#30363D" />
      <!-- Bottom Right -->
      <rect x="220" y="190" width="40" height="30" rx="5" class="robot-wheel" />
      <line x1="240" y1="195" x2="240" y2="215" stroke="#30363D" />
      
      <!-- LIDAR Scanner Ring (Center) -->
      <circle cx="160" cy="150" r="28" class="robot-body" />
      <circle cx="160" cy="150" r="22" class="robot-accent" />
      <line x1="160" y1="122" x2="160" y2="178" stroke="#30363D" />
      <line x1="132" y1="150" x2="178" y2="150" stroke="#30363D" />
      
      <!-- Depth Camera Block (Front/Right) -->
      <rect x="235" y="135" width="12" height="30" rx="2" class="robot-body" />
      <circle cx="241" cy="142" r="2" fill="#00E5FF" />
      <circle cx="241" cy="158" r="2" fill="#00E5FF" />
      
      <!-- Embedded Microcontroller Board (Internal) -->
      <rect x="105" y="125" width="40" height="35" rx="3" fill="#161B22" stroke="#30363D" />
      <rect x="110" y="130" width="12" height="12" fill="#00E5FF" opacity="0.6" />
      <line x1="110" y1="148" x2="135" y2="148" stroke="#30363D" stroke-width="2" />
    </g>

    <!-- GUIDELINES (Connector lines from hotspot to info panel) -->
    <!-- Lidar connector: cx=200, cy=170 -> Info: x=430, y=100 -->
    <path id="line-lidar" d="M 200 170 L 320 120 L 430 120" class="connector-line" />
    <!-- Camera connector: cx=280, cy=170 -> Info: x=430, y=100 -->
    <path id="line-camera" d="M 281 170 L 350 140 L 430 140" class="connector-line" />
    <!-- Brain connector: cx=155, cy=155 -> Info: x=430, y=100 -->
    <path id="line-brain" d="M 155 155 L 280 200 L 430 200" class="connector-line" />
    <!-- Chassis connector: cx=120, cy=210 -> Info: x=430, y=100 -->
    <path id="line-chassis" d="M 120 210 L 250 250 L 430 250" class="connector-line" />

    <!-- HOTSPOTS (Hover zones) -->
    <!-- 1. LIDAR -->
    <g id="hs-lidar" class="hotspot" transform="translate(200, 170)">
      <circle cx="0" cy="0" r="12" class="hotspot-ring" />
      <circle cx="0" cy="0" r="4.5" class="hotspot-center" />
      <circle cx="0" cy="0" r="16" fill="transparent" />
    </g>
    <!-- 2. Camera -->
    <g id="hs-camera" class="hotspot" transform="translate(281, 170)">
      <circle cx="0" cy="0" r="12" class="hotspot-ring" />
      <circle cx="0" cy="0" r="4.5" class="hotspot-center" />
      <circle cx="0" cy="0" r="16" fill="transparent" />
    </g>
    <!-- 3. Microcontroller / Brain -->
    <g id="hs-brain" class="hotspot" transform="translate(155, 155)">
      <circle cx="0" cy="0" r="12" class="hotspot-ring" />
      <circle cx="0" cy="0" r="4.5" class="hotspot-center" />
      <circle cx="0" cy="0" r="16" fill="transparent" />
    </g>
    <!-- 4. Wheels / Chassis -->
    <g id="hs-chassis" class="hotspot" transform="translate(120, 210)">
      <circle cx="0" cy="0" r="12" class="hotspot-ring" />
      <circle cx="0" cy="0" r="4.5" class="hotspot-center" />
      <circle cx="0" cy="0" r="16" fill="transparent" />
    </g>

    <!-- RIGHT SIDE INFO PANELS (Stacked in same position, toggled by CSS opacity) -->
    
    <!-- Default Instruction Panel -->
    <g id="panel-default" class="default-panel" transform="translate(450, 120)">
      <rect width="320" height="150" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.5" />
      <text x="160" y="65" class="default-text" text-anchor="middle">🔍 Hover over any pulse hotspot</text>
      <text x="160" y="85" class="default-text" text-anchor="middle">on the blueprint to inspect the integration stack.</text>
    </g>
    
    <!-- 1. LIDAR Panel -->
    <g id="panel-lidar" class="info-panel" transform="translate(450, 75)">
      <rect width="320" height="195" rx="8" fill="#161B22" stroke="#00E5FF" stroke-width="1.5" filter="drop-shadow(0 0 4px rgba(0,229,255,0.15))" />
      <text x="20" y="30" class="info-header">📡 Laser Scanner (LIDAR)</text>
      <line x1="20" y1="42" x2="300" y2="42" stroke="#30363D" />
      
      <text x="20" y="65" class="info-label">Framework:</text>
      <text x="100" y="65" class="info-body">ROS 2 Jazzy, Micro-ROS</text>
      
      <text x="20" y="90" class="info-label">Drivers:</text>
      <text x="100" y="90" class="info-body">rplidar_ros, laser_filters</text>
      
      <text x="20" y="115" class="info-label">SLAM Stack:</text>
      <text x="100" y="115" class="info-body">SLAM Toolbox, Nav2 (Navigation Suite)</text>
      
      <text x="20" y="140" class="info-label">Application:</text>
      <text x="20" y="157" class="info-body">Generates real-time 2D costmaps, performing lidar-</text>
      <text x="20" y="174" class="info-body">based mapping, localization, &amp; autonomous navigation.</text>
    </g>
    
    <!-- 2. Camera Panel -->
    <g id="panel-camera" class="info-panel" transform="translate(450, 75)">
      <rect width="320" height="195" rx="8" fill="#161B22" stroke="#00E5FF" stroke-width="1.5" filter="drop-shadow(0 0 4px rgba(0,229,255,0.15))" />
      <text x="20" y="30" class="info-header">👁️ Computer Vision System</text>
      <line x1="20" y1="42" x2="300" y2="42" stroke="#30363D" />
      
      <text x="20" y="65" class="info-label">Libraries:</text>
      <text x="100" y="65" class="info-body">OpenCV, MediaPipe</text>
      
      <text x="20" y="90" class="info-label">Classifiers:</text>
      <text x="100" y="90" class="info-body">Scikit-learn, Custom SVM &amp; CNNs</text>
      
      <text x="20" y="115" class="info-label">Models:</text>
      <text x="100" y="115" class="info-body">Gesture Classification models</text>
      
      <text x="20" y="140" class="info-label">Application:</text>
      <text x="20" y="157" class="info-body">Runs real-time hand-gesture tracking &amp; sign-</text>
      <text x="20" y="174" class="info-body">language translation pipelines via image classification.</text>
    </g>
    
    <!-- 3. Brain Panel -->
    <g id="panel-brain" class="info-panel" transform="translate(450, 75)">
      <rect width="320" height="195" rx="8" fill="#161B22" stroke="#00E5FF" stroke-width="1.5" filter="drop-shadow(0 0 4px rgba(0,229,255,0.15))" />
      <text x="20" y="30" class="info-header">🧠 Main Compute / AI Agent</text>
      <line x1="20" y1="42" x2="300" y2="42" stroke="#30363D" />
      
      <text x="20" y="65" class="info-label">Compute Core:</text>
      <text x="100" y="65" class="info-body">NVIDIA Jetson, Edge SBC</text>
      
      <text x="20" y="90" class="info-label">Edge LLM:</text>
      <text x="100" y="90" class="info-body">Llama 3.2, Ollama Orchestration</text>
      
      <text x="20" y="115" class="info-label">Backend Stack:</text>
      <text x="100" y="115" class="info-body">FastAPI, WebSockets, Python</text>
      
      <text x="20" y="140" class="info-label">Application:</text>
      <text x="20" y="157" class="info-body">Hosts local voice assistant AI agents (Orion),</text>
      <text x="20" y="174" class="info-body">and runs autonomous behavioral cloning models.</text>
    </g>
    
    <!-- 4. Chassis Panel -->
    <g id="panel-chassis" class="info-panel" transform="translate(450, 75)">
      <rect width="320" height="195" rx="8" fill="#161B22" stroke="#00E5FF" stroke-width="1.5" filter="drop-shadow(0 0 4px rgba(0,229,255,0.15))" />
      <text x="20" y="30" class="info-header">🚜 Drive Train &amp; Embedded Control</text>
      <line x1="20" y1="42" x2="300" y2="42" stroke="#30363D" />
      
      <text x="20" y="65" class="info-label">Chassis:</text>
      <text x="100" y="65" class="info-body">AgileX Scout Mini (Skid-steer)</text>
      
      <text x="20" y="90" class="info-label">Controller:</text>
      <text x="100" y="90" class="info-body">STM32 / ESP32 MCU boards</text>
      
      <text x="20" y="115" class="info-label">Protocol:</text>
      <text x="100" y="115" class="info-body">CAN-bus (Control Area Network), UART</text>
      
      <text x="20" y="140" class="info-label">Application:</text>
      <text x="20" y="157" class="info-body">Embedded drivers controlling kinematics, wheel speeds,</text>
      <text x="20" y="174" class="info-body">and feedback metrics back to the ROS 2 workspace.</text>
    </g>
    
  </g>
</svg>"""
    with open("robot-schematic.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("robot-schematic.svg generated successfully with interactive hotspots!")

if __name__ == "__main__":
    generate_robot_svg()
