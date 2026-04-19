import re

with open("Outings.html", "r") as f:
    content = f.read()

# 1. Extract the whole style block to ensure no styles are missed
style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
styles = style_match.group(0) if style_match else ""

# 2. Extract Planning Hub HTML
html_match = re.search(r'<!-- ══ PLANNING HUB ══ -->.*?</div>\n(?=<!-- MODAL -->)', content, re.DOTALL)
if not html_match:
    # Try another bound
    html_match = re.search(r'<!-- ══ PLANNING HUB ══ -->.*?</div>\n\n<!--', content, re.DOTALL)

planning_html = html_match.group(0) if html_match else ""

# 3. Extract Planning Hub JS
js_match = re.search(r'// ── PLANNING HUB ──\nconst PLAN_LOCS=.*?(?=\n\n// ── EXPANDED CHRONICLE ──)', content, re.DOTALL)
planning_js = js_match.group(0) if js_match else ""

# Create Planning_Hub.html
planning_hub_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Troop 222 — Planning Hub</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Spectral:ital,wght@0,400;0,600;1,400&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
{styles}
</head>
<body>
<div class="page">
<section class="hero" style="min-height:40vh; padding: 2rem 0 2rem;">
  <div class="hero-bg"></div>
  <div class="hero-topo"></div>
  <p class="hero-eyebrow">BSA Troop 222</p>
  <h1>PLANNING<br><span>HUB</span></h1>
  <p class="hero-sub">The Outing Coordinator's Toolkit</p>
</section>

<nav class="nav" id="main-nav">
  <a href="Outings.html" class="nav-btn" style="text-decoration:none;">← Back to Outings</a>
  <button class="nav-btn active">Planning Hub</button>
</nav>

<div style="margin-top: 3rem;">
{planning_html.replace('id="tab-planning" class="section"', 'id="tab-planning" class="section active"')}
</div>

<footer>
  <span class="footer-brand">Troop 222</span>
  <span class="footer-note">BSA · Pacific Skyline Council · Menlo Park · 2017–2026</span>
</footer>

</div><!-- .page -->

<script>
{planning_js}
</script>
</body>
</html>
"""

with open("Planning_Hub.html", "w") as f:
    f.write(planning_hub_content)

# Modify Outings.html
# Replace nav button
new_content = content.replace('<button class="nav-btn" data-tab="planning">Planning Hub</button>', '<a href="Planning_Hub.html" class="nav-btn" style="text-decoration:none;">Planning Hub ↗</a>')

# Remove HTML
if planning_html:
    new_content = new_content.replace(planning_html, '')

# Remove JS
if planning_js:
    new_content = new_content.replace(planning_js, '')

with open("Outings.html", "w") as f:
    f.write(new_content)

print("Done")
