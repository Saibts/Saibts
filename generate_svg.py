import os

# --- EDIT THIS DICTIONARY TO CUSTOMIZE YOUR TECH STACK ---
CONFIG = {
    # Core Central Node
    "core": {
        "title": "⚡ TECH STACK",
        "subtitle": "Developer Toolbox",
        "color": "#D946EF"  # Glow color
    },
    
    # Robotics Branch (Left side)
    "robotics": {
        "title": "🤖 ROBOTICS",
        "subtitle": "Control & Systems",
        "color": "#3B82F6",
        "children": [
            {"title": "ROS 2 (Jazzy/Humble)", "subtitle": "Middleware & Nav2"},
            {"title": "AgileX Scout Mini", "subtitle": "Mobile Platforms & Arms"},
            {"title": "Sensors integration", "subtitle": "LIDAR, IMUs, Encoders"}
        ]
    },
    
    # Computer Vision & AI Branch (Right side, Top)
    "ai": {
        "title": "🖥️ CV & AI",
        "subtitle": "Computer Vision",
        "color": "#00E5FF",
        "children": [
            {"title": "OpenCV & MediaPipe", "subtitle": "Hand/Pose Tracking"},
            {"title": "PyTorch & TensorFlow", "subtitle": "Deep Learning models"},
            {"title": "AI Agents & Antigravity", "subtitle": "Google AGY & Vibe Coding"}
        ]
    },
    
    # Embedded Branch (Right side, Bottom)
    "embedded": {
        "title": "💡 EMBEDDED",
        "subtitle": "Firmware & Soft",
        "color": "#10B981",
        "children": [
            {"title": "Python & Embedded C", "subtitle": "Main programming languages"},
            {"title": "ESP32, STM32 & Jetson", "subtitle": "Single Board Computers"},
            {"title": "Micro-ROS & Git", "subtitle": "Linux (Ubuntu) & VS Code"}
        ]
    }
}

# --- SVG GENERATION LOGIC ---
svg_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 320" width="100%" height="100%">
  <style>
    .bg {{ fill: #0D1117; rx: 10px; }}
    .link {{ fill: none; stroke-linecap: round; stroke-linejoin: round; opacity: 0.85; }}
    .link-robotics {{ stroke: {color_robotics}; stroke-width: 2; filter: drop-shadow(0 0 2px {color_robotics}); }}
    .link-ai {{ stroke: {color_ai}; stroke-width: 2; filter: drop-shadow(0 0 2px {color_ai}); }}
    .link-embedded {{ stroke: {color_embedded}; stroke-width: 2; filter: drop-shadow(0 0 2px {color_embedded}); }}
    
    .title-text {{ font-family: "Segoe UI", -apple-system, sans-serif; font-weight: bold; fill: #FFFFFF; font-size: 10.5px; text-anchor: middle; }}
    .sub-text {{ font-family: "Segoe UI", -apple-system, sans-serif; fill: #8B949E; font-size: 9.5px; text-anchor: middle; }}
    
    .core-node {{ fill: #1E1B4B; stroke: {color_core}; stroke-width: 2.5; filter: drop-shadow(0 0 5px {color_core}); }}
    .node-robotics {{ fill: #1E293B; stroke: {color_robotics}; stroke-width: 1.5; }}
    .node-ai {{ fill: #1E293B; stroke: {color_ai}; stroke-width: 1.5; }}
    .node-embedded {{ fill: #1E293B; stroke: {color_embedded}; stroke-width: 1.5; }}
    
    g.node-group:hover rect {{
      fill: #0F172A !important;
      stroke-width: 2 !important;
    }}
  </style>
  
  <rect width="100%" height="100%" class="bg" />
  
  <!-- CONNECTION PATHS -->
  <path d="M 400 160 L 225 160 M 225 160 L 200 75 M 225 160 L 200 155 M 225 160 L 200 235" class="link link-robotics" />
  <path d="M 400 160 Q 400 80 500 80 M 500 80 L 565 50 M 500 80 L 565 100 M 500 80 L 565 150" class="link link-ai" />
  <path d="M 400 160 Q 400 240 500 240 M 500 240 L 565 200 M 500 240 L 565 250 M 500 240 L 565 290" class="link link-embedded" />
  
  <!-- CENTRAL CORE NODE -->
  <g class="node-group">
    <rect x="340" y="135" width="120" height="50" rx="25" class="core-node" />
    <text x="400" y="160" class="title-text" font-size="12px">{title_core}</text>
    <text x="400" y="173" class="sub-text" fill="#E879F9">{subtitle_core}</text>
  </g>
  
  <!-- ROBOTICS BRANCH -->
  <g class="node-group">
    <rect x="225" y="140" width="100" height="40" rx="6" class="node-robotics" />
    <text x="275" y="158" class="title-text">{title_robotics}</text>
    <text x="275" y="171" class="sub-text" fill="#60A5FA">{subtitle_robotics}</text>
  </g>
  <g class="node-group">
    <rect x="65" y="60" width="135" height="30" rx="4" class="node-robotics" />
    <text x="132.5" y="76" class="title-text">{title_rob_child1}</text>
    <text x="132.5" y="85" class="sub-text">{sub_rob_child1}</text>
  </g>
  <g class="node-group">
    <rect x="65" y="140" width="135" height="30" rx="4" class="node-robotics" />
    <text x="132.5" y="156" class="title-text">{title_rob_child2}</text>
    <text x="132.5" y="165" class="sub-text">{sub_rob_child2}</text>
  </g>
  <g class="node-group">
    <rect x="65" y="220" width="135" height="30" rx="4" class="node-robotics" />
    <text x="132.5" y="236" class="title-text">{title_rob_child3}</text>
    <text x="132.5" y="245" class="sub-text">{sub_rob_child3}</text>
  </g>
  
  <!-- CV & AI BRANCH -->
  <g class="node-group">
    <rect x="450" y="60" width="100" height="40" rx="6" class="node-ai" />
    <text x="500" y="78" class="title-text">{title_ai}</text>
    <text x="500" y="91" class="sub-text" fill="#22D3EE">{subtitle_ai}</text>
  </g>
  <g class="node-group">
    <rect x="565" y="35" width="150" height="30" rx="4" class="node-ai" />
    <text x="640" y="51" class="title-text">{title_ai_child1}</text>
    <text x="640" y="60" class="sub-text">{sub_ai_child1}</text>
  </g>
  <g class="node-group">
    <rect x="565" y="85" width="150" height="30" rx="4" class="node-ai" />
    <text x="640" y="101" class="title-text">{title_ai_child2}</text>
    <text x="640" y="110" class="sub-text">{sub_ai_child2}</text>
  </g>
  <g class="node-group">
    <rect x="565" y="135" width="150" height="30" rx="4" class="node-ai" />
    <text x="640" y="151" class="title-text">{title_ai_child3}</text>
    <text x="640" y="160" class="sub-text">{sub_ai_child3}</text>
  </g>
  
  <!-- EMBEDDED BRANCH -->
  <g class="node-group">
    <rect x="450" y="220" width="100" height="40" rx="6" class="node-embedded" />
    <text x="500" y="238" class="title-text">{title_emb}</text>
    <text x="500" y="251" class="sub-text" fill="#34D399">{subtitle_emb}</text>
  </g>
  <g class="node-group">
    <rect x="565" y="185" width="150" height="30" rx="4" class="node-embedded" />
    <text x="640" y="201" class="title-text">{title_emb_child1}</text>
    <text x="640" y="210" class="sub-text">{sub_emb_child1}</text>
  </g>
  <g class="node-group">
    <rect x="565" y="235" width="150" height="30" rx="4" class="node-embedded" />
    <text x="640" y="251" class="title-text">{title_emb_child2}</text>
    <text x="640" y="260" class="sub-text">{sub_emb_child2}</text>
  </g>
  <g class="node-group">
    <rect x="565" y="275" width="150" height="30" rx="4" class="node-embedded" />
    <text x="640" y="291" class="title-text">{title_emb_child3}</text>
    <text x="640" y="300" class="sub-text">{sub_emb_child3}</text>
  </g>
</svg>
"""

# Helper to escape XML special characters
def esc(val):
    return val.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

formatted_svg = svg_template.format(
    color_core=CONFIG["core"]["color"],
    title_core=esc(CONFIG["core"]["title"]),
    subtitle_core=esc(CONFIG["core"]["subtitle"]),
    
    color_robotics=CONFIG["robotics"]["color"],
    title_robotics=esc(CONFIG["robotics"]["title"]),
    subtitle_robotics=esc(CONFIG["robotics"]["subtitle"]),
    title_rob_child1=esc(CONFIG["robotics"]["children"][0]["title"]),
    sub_rob_child1=esc(CONFIG["robotics"]["children"][0]["subtitle"]),
    title_rob_child2=esc(CONFIG["robotics"]["children"][1]["title"]),
    sub_rob_child2=esc(CONFIG["robotics"]["children"][1]["subtitle"]),
    title_rob_child3=esc(CONFIG["robotics"]["children"][2]["title"]),
    sub_rob_child3=esc(CONFIG["robotics"]["children"][2]["subtitle"]),
    
    color_ai=CONFIG["ai"]["color"],
    title_ai=esc(CONFIG["ai"]["title"]),
    subtitle_ai=esc(CONFIG["ai"]["subtitle"]),
    title_ai_child1=esc(CONFIG["ai"]["children"][0]["title"]),
    sub_ai_child1=esc(CONFIG["ai"]["children"][0]["subtitle"]),
    title_ai_child2=esc(CONFIG["ai"]["children"][1]["title"]),
    sub_ai_child2=esc(CONFIG["ai"]["children"][1]["subtitle"]),
    title_ai_child3=esc(CONFIG["ai"]["children"][2]["title"]),
    sub_ai_child3=esc(CONFIG["ai"]["children"][2]["subtitle"]),
    
    color_embedded=CONFIG["embedded"]["color"],
    title_emb=esc(CONFIG["embedded"]["title"]),
    subtitle_emb=esc(CONFIG["embedded"]["subtitle"]),
    title_emb_child1=esc(CONFIG["embedded"]["children"][0]["title"]),
    sub_emb_child1=esc(CONFIG["embedded"]["children"][0]["subtitle"]),
    title_emb_child2=esc(CONFIG["embedded"]["children"][1]["title"]),
    sub_emb_child2=esc(CONFIG["embedded"]["children"][1]["subtitle"]),
    title_emb_child3=esc(CONFIG["embedded"]["children"][2]["title"]),
    sub_emb_child3=esc(CONFIG["embedded"]["children"][2]["subtitle"])
)

with open("tech-stack-mindmap.svg", "w", encoding="utf-8") as f:
    f.write(formatted_svg)

print("Successfully generated tech-stack-mindmap.svg!")

