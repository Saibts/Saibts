import os
import sys
import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def generate_graph():
    username = "Saibts"
    url = f"https://github.com/users/{username}/contributions"
    
    print(f"Fetching contribution data for {username}...")
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        html_content = response.text
    except Exception as e:
        print(f"Error fetching data from GitHub: {e}")
        sys.exit(1)
        
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Map td elements by their ID to their dates
    days = {}
    for td in soup.find_all("td", class_="ContributionCalendar-day"):
        date_str = td.get("data-date")
        td_id = td.get("id")
        if date_str and td_id:
            days[td_id] = {
                "date": date_str,
                "count": 0
            }
            
    # Extract counts from corresponding tool-tips
    for tooltip in soup.find_all("tool-tip"):
        for_id = tooltip.get("for")
        if for_id in days:
            text = tooltip.text.strip()
            # "No contributions on August 24th." -> 0
            # "6 contributions on June 7th." -> 6
            # "1 contribution on June 14th." -> 1
            if "No contributions" in text:
                count = 0
            else:
                match = re.match(r"(\d+)\s+contribution", text)
                if match:
                    count = int(match.group(1))
                else:
                    count = 0
            days[for_id]["count"] = count
            
    # Sort contributions by date
    sorted_days = sorted(days.values(), key=lambda x: x["date"])
    if not sorted_days:
        print("No contribution data parsed from HTML.")
        sys.exit(1)
        
    # Get last 30 days of contributions
    last_30_days = sorted_days[-30:]
    
    # SVG Config
    svg_width = 800
    svg_height = 260
    padding_left = 50
    padding_right = 45
    padding_top = 65
    padding_bottom = 40
    
    plot_width = svg_width - padding_left - padding_right
    plot_height = svg_height - padding_top - padding_bottom
    
    counts = [day["count"] for day in last_30_days]
    max_count = max(counts) if counts else 0
    if max_count < 5:
        max_count = 5  # Ensure we have a reasonable scale even if contributions are low
        
    # Helper to calculate coordinate
    def get_coords(index, count):
        x = padding_left + index * (plot_width / 29)
        y = padding_top + plot_height - (count / max_count) * plot_height
        return x, y

    points = []
    for i, day in enumerate(last_30_days):
        x, y = get_coords(i, day["count"])
        points.append({
            "x": x,
            "y": y,
            "date": datetime.strptime(day["date"], "%Y-%m-%d").strftime("%b %d, %Y"),
            "count": day["count"]
        })
        
    # Draw line path
    line_path_d = ""
    area_path_d = f"M {points[0]['x']} {padding_top + plot_height} "
    
    for i, p in enumerate(points):
        prefix = "M" if i == 0 else "L"
        line_path_d += f"{prefix} {p['x']:.1f} {p['y']:.1f} "
        area_path_d += f"L {p['x']:.1f} {p['y']:.1f} "
        
    area_path_d += f"L {points[-1]['x']:.1f} {padding_top + plot_height} Z"
    
    # Generate interactive SVG structure
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="100%" height="100%">')
    
    # Styling and Animations
    svg.append("""  <style>
    .bg { fill: #0D1117; rx: 10px; }
    .grid-line { stroke: #30363D; stroke-width: 1; stroke-dasharray: 4 4; }
    .axis-text { fill: #8B949E; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; }
    .title { fill: #58A6FF; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 600; }
    .subtitle { fill: #8B949E; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11px; }
    .graph-line { stroke: #00E5FF; stroke-width: 2.5; fill: none; stroke-linecap: round; stroke-linejoin: round; filter: drop-shadow(0px 2px 8px rgba(0, 229, 255, 0.4)); }
    .graph-area { fill: url(#area-grad); }
    
    /* Interactive Point Group styles */
    .point-group { cursor: pointer; }
    .point-group .point-dot { fill: #0D1117; stroke: #00E5FF; stroke-width: 2; transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1); }
    .point-group .guide-line { stroke: #00E5FF; stroke-width: 1; stroke-dasharray: 2 2; opacity: 0; transition: opacity 0.25s ease; }
    .point-group .tooltip { opacity: 0; pointer-events: none; transition: opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1), transform 0.25s cubic-bezier(0.4, 0, 0.2, 1); transform: translateY(8px); }
    
    /* Hover Effects */
    .point-group:hover .point-dot { r: 6.5px; fill: #00E5FF; filter: drop-shadow(0 0 5px #00E5FF); }
    .point-group:hover .guide-line { opacity: 0.35; }
    .point-group:hover .tooltip { opacity: 1; transform: translateY(0); }
  </style>""")
    
    # Defs (Gradients and Filters)
    svg.append("""  <defs>
    <linearGradient id="area-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0.0" />
    </linearGradient>
  </defs>""")
    
    # Card Background
    svg.append(f'  <rect width="100%" height="100%" class="bg" />')
    
    # Title & Stats Info
    total_last_30 = sum(counts)
    svg.append(f'  <text x="25" y="32" class="title">Activity Graph</text>')
    svg.append(f'  <text x="25" y="50" class="subtitle">Total contributions (last 30 days): {total_last_30}</text>')
    
    # Grid lines (horizontal)
    grid_steps = 4
    for i in range(grid_steps + 1):
        y_val = padding_top + (plot_height / grid_steps) * i
        count_val = int(max_count - (max_count / grid_steps) * i)
        svg.append(f'  <line x1="{padding_left}" y1="{y_val}" x2="{svg_width - padding_right}" y2="{y_val}" class="grid-line" />')
        svg.append(f'  <text x="{padding_left - 10}" y="{y_val + 4}" class="axis-text" text-anchor="end">{count_val}</text>')
        
    # Area path
    svg.append(f'  <path d="{area_path_d}" class="graph-area" />')
    
    # Line path
    svg.append(f'  <path d="{line_path_d}" class="graph-line" />')
    
    # X-axis Labels (e.g., show labels for every 5 days to avoid clutter)
    for i, p in enumerate(points):
        if i % 5 == 0 or i == 29:
            label_date = datetime.strptime(last_30_days[i]["date"], "%Y-%m-%d").strftime("%b %d")
            svg.append(f'  <text x="{p["x"]}" y="{padding_top + plot_height + 20}" class="axis-text" text-anchor="middle">{label_date}</text>')
            
    # Interactive Points and Tooltips
    for i, p in enumerate(points):
        # Determine tooltip text
        contrib_text = f"{p['count']} contribution" + ("s" if p['count'] != 1 else "")
        if p['count'] == 0:
            contrib_text = "No contributions"
            
        # Tooltip position adjustments to make sure it stays inside the boundary
        tooltip_w = 120
        tooltip_h = 42
        tx = p['x'] - (tooltip_w / 2)
        ty = p['y'] - tooltip_h - 10
        
        # Keep tooltips inside SVG boundaries
        if tx < 10:
            tx = 10
        elif tx + tooltip_w > svg_width - 10:
            tx = svg_width - tooltip_w - 10
            
        if ty < 5:
            ty = p['y'] + 15  # Render below point if too close to top
            
        svg.append(f'  <g class="point-group">')
        # Guide line to X axis
        svg.append(f'    <line x1="{p["x"]:.1f}" y1="{padding_top}" x2="{p["x"]:.1f}" y2="{padding_top + plot_height}" class="guide-line" />')
        # Point dot
        svg.append(f'    <circle cx="{p["x"]:.1f}" cy="{p["y"]:.1f}" r="4" class="point-dot" />')
        # Large invisible hit box for easier hovering
        svg.append(f'    <circle cx="{p["x"]:.1f}" cy="{p["y"]:.1f}" r="12" fill="transparent" />')
        
        # Tooltip
        svg.append(f'    <g class="tooltip" transform="translate({tx:.1f}, {ty:.1f})">')
        svg.append(f'      <rect width="{tooltip_w}" height="{tooltip_h}" rx="5" fill="#161B22" stroke="#30363D" stroke-width="1.5" filter="drop-shadow(0px 3px 6px rgba(0,0,0,0.5))" />')
        svg.append(f'      <text x="{tooltip_w/2}" y="17" fill="#F0F6FC" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10.5px" font-weight="600" text-anchor="middle">{contrib_text}</text>')
        svg.append(f'      <text x="{tooltip_w/2}" y="31" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9px" text-anchor="middle">{p["date"]}</text>')
        svg.append(f'    </g>')
        svg.append(f'  </g>')
        
    svg.append('</svg>')
    
    output_content = "\n".join(svg)
    with open("activity-graph.svg", "w", encoding="utf-8") as f:
        f.write(output_content)
    print("activity-graph.svg generated successfully with interactive CSS styling!")

if __name__ == "__main__":
    generate_graph()
