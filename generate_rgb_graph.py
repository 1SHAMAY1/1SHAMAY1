import os
import requests
import datetime
from string import Template

# --- CONFIGURATION ---
USERNAME = "1SHAMAY1"
TOKEN = os.getenv("GH_TOKEN") # Will be passed by GitHub Actions

# GraphQL query to get the contribution graph
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
        print("No GitHub Token found. Generating mock data for testing.")
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
    # Fallback to create a cool pattern if API fails or running locally
    import random
    weeks = []
    for _ in range(52):
        days = []
        for _ in range(7):
            days.append({"contributionCount": random.choice([0, 0, 1, 3, 5, 10])})
        weeks.append({"contributionDays": days})
    return weeks

def build_svg(weeks_data):
    # Base SVG layout math
    cell_size = 12
    gap = 4
    width = (52 * (cell_size + gap)) + 20
    height = (7 * (cell_size + gap)) + 20
    
    # CSS inside the SVG for the RGB breathing effect
    svg_header = f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .cell {{ rx: 3; ry: 3; stroke: #ffffff10; stroke-width: 1; }}
        .lvl-0 {{ fill: #161b22; }}
        .lvl-1 {{ fill: #0e4429; }}
        .lvl-2 {{ fill: #006d32; }}
        .lvl-3 {{ fill: #26a641; }}
        
        /* The RGB Animation for high-density commits */
        @keyframes rgb-glow {{
            0%   {{ fill: #ff0055; filter: drop-shadow(0 0 2px #ff0055); }}
            33%  {{ fill: #00a3ff; filter: drop-shadow(0 0 2px #00a3ff); }}
            66%  {{ fill: #aa00ff; filter: drop-shadow(0 0 2px #aa00ff); }}
            100% {{ fill: #ff0055; filter: drop-shadow(0 0 2px #ff0055); }}
        }}
        
        /* Apply the animation with a slight random delay so they don't pulse at the exact same time */
        .lvl-4 {{
            animation: rgb-glow 4s infinite alternate;
        }}
        
        .delay-1 {{ animation-delay: 0s; }}
        .delay-2 {{ animation-delay: 0.5s; }}
        .delay-3 {{ animation-delay: 1s; }}
    </style>
    <rect width="100%" height="100%" fill="#0D1117" rx="10"/>
    <g transform="translate(10, 10)">
    """
    
    svg_body = ""
    for week_idx, week in enumerate(weeks_data):
        x = week_idx * (cell_size + gap)
        for day_idx, day in enumerate(week['contributionDays']):
            y = day_idx * (cell_size + gap)
            count = day.get('contributionCount', 0)
            
            # Classify contribution density
            if count == 0: css_class = "lvl-0"
            elif count < 3: css_class = "lvl-1"
            elif count < 6: css_class = "lvl-2"
            elif count < 10: css_class = "lvl-3"
            else: 
                # Highest level gets the RGB animation
                delay = f"delay-{(x+y)%3 + 1}" # Staggered animation effect
                css_class = f"lvl-4 {delay}"
                
            svg_body += f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" class="cell {css_class}"/>\n'

    svg_footer = "</g></svg>"
    return svg_header + svg_body + svg_footer

if __name__ == "__main__":
    weeks = fetch_contributions()
    svg_content = build_svg(weeks)
    
    # Save the SVG
    os.makedirs("dist", exist_ok=True)
    with open("dist/rgb-graph.svg", "w") as f:
        f.write(svg_content)
    
    print("Successfully generated rgb-graph.svg inside /dist directory!")
