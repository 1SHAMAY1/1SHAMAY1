import os
import requests

# --- CONFIGURATION ---
USERNAME = "1SHAMAY1"
TOKEN = os.getenv("GH_TOKEN")

QUERY = """
query($userName:String!) {
  user(login: $userName){
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
          }
        }
      }
    }
  }
}
"""

def fetch_contributions():
    if not TOKEN:
        print("No token found. Generating local mock data.")
        return generate_mock_data()
        
    headers = {"Authorization": f"Bearer {TOKEN}"}
    variables = {"userName": USERNAME}
    
    response = requests.post(
        "https://api.github.com/graphql", 
        json={"query": QUERY, "variables": variables}, 
        headers=headers
    )
    
    if response.status_code == 200:
        return response.json()['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
    else:
        raise Exception(f"Query failed {response.status_code}. {response.text}")

def generate_mock_data():
    import random
    weeks = []
    for _ in range(52):
        days = []
        for _ in range(7):
            days.append({"contributionCount": random.choice([0, 1, 4, 8, 15])})
        weeks.append({"contributionDays": days})
    return weeks

def build_svg(weeks_data):
    cell_size = 12
    gap = 4
    width = (52 * (cell_size + gap)) + 20
    height = (7 * (cell_size + gap)) + 20
    
    svg_header = f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .cell {{ rx: 3; ry: 3; stroke: rgba(255,255,255,0.05); stroke-width: 1; transform-origin: center; transform-box: fill-box; }}
        
        /* Strict Color Palette (No Black/White) */
        .lvl-0 {{ fill: #5c4033; }} /* Brown */
        .lvl-1 {{ fill: #2ea043; }} /* Green */
        .lvl-2 {{ fill: #e3b341; }} /* Yellow */
        .lvl-3 {{ fill: #388bfd; }} /* Blue */
        
        /* Pathfinding Sweep for lower commits */
        @keyframes sweep {{
            0%   {{ filter: brightness(0.8) saturate(0.8); transform: scale(1); }}
            50%  {{ filter: brightness(1.8) saturate(1.5); transform: scale(1.15); }}
            100% {{ filter: brightness(0.8) saturate(0.8); transform: scale(1); }}
        }}

        /* Intense Pulse for highest commits */
        @keyframes pulse-red {{
            0%   {{ fill: #aa0000; filter: drop-shadow(0 0 2px #ff0000); transform: scale(1); }}
            50%  {{ fill: #ff0000; filter: drop-shadow(0 0 10px #ff0000); transform: scale(1.25); }}
            100% {{ fill: #aa0000; filter: drop-shadow(0 0 2px #ff0000); transform: scale(1); }}
        }}
        
        .lvl-4 {{
            fill: #ff0000;
        }}
    </style>
    <rect width="100%" height="100%" fill="#0D1117" rx="10"/>
    <g transform="translate(10, 10)">
    """
    
    svg_body = ""
    for week_idx, week in enumerate(weeks_data):
        x = week_idx * (cell_size + gap)
        
        # Calculate the wave delay progressing from left to right
        base_delay = week_idx * 0.08
        
        for day_idx, day in enumerate(week['contributionDays']):
            y = day_idx * (cell_size + gap)
            count = day.get('contributionCount', 0)
            
            # Map commit counts to the color palette
            if count == 0: css_class = "lvl-0"
            elif count < 3: css_class = "lvl-1"
            elif count < 6: css_class = "lvl-2"
            elif count < 10: css_class = "lvl-3"
            else: css_class = "lvl-4"
            
            # Add a slight Y-axis delay for a diagonal pathfinding effect
            delay = base_delay + (day_idx * 0.02)
            
            if css_class == "lvl-4":
                anim = f"pulse-red 2s infinite {delay}s"
            else:
                anim = f"sweep 3.5s infinite {delay}s"
                
            svg_body += f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" class="cell {css_class}" style="animation: {anim};"/>\n'

    svg_footer = "</g></svg>"
    return svg_header + svg_body + svg_footer

if __name__ == "__main__":
    weeks = fetch_contributions()
    svg_content = build_svg(weeks)
    
    os.makedirs("dist", exist_ok=True)
    with open("dist/rgb-graph.svg", "w") as f:
        f.write(svg_content)
    
    print("Pathfinding SVG generated successfully.")
