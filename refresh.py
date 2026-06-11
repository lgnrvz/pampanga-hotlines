#!/usr/bin/env python3
"""Weekly hotline verifier — checks key sources, updates if changes found, pushes to GitHub Pages."""
import json, os, subprocess, sys, datetime

REPO = "/home/raspberrypi/pampanga-hotlines"
PAGES_REPO = "/tmp/lgnrvz.github.io-hotlines"
HOTLINES_JSON = f"{REPO}/hotlines.json"
INDEX_HTML = f"{REPO}/index.html"
PAGES_HTML = f"{PAGES_REPO}/pampanga-hotlines/index.html"
GITHUB_PAGES = "https://github.com/lgnrvz/lgnrvz.github.io.git"

def log(msg):
    print(f"[hotlines-refresh] {datetime.datetime.now():%Y-%m-%d %H:%M} {msg}")

def run(cmd, workdir=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=workdir)
    return result.returncode == 0, result.stdout.strip(), result.stderr.strip()

log("Starting weekly hotline refresh...")

# 1. Pull latest hotlines data
ok, _, err = run("git pull origin master", REPO)
if not ok:
    log(f"Git pull failed: {err}")
    sys.exit(1)

# 2. Clone/update the GitHub Pages repo
if os.path.isdir(PAGES_REPO):
    ok, _, err = run(f"git -C {PAGES_REPO} pull origin main")
    if not ok:
        log(f"Pages pull failed: {err}")
else:
    ok, _, err = run(f"git clone {GITHUB_PAGES} {PAGES_REPO}")
    if not ok:
        log(f"Pages clone failed: {err}")
        sys.exit(1)

# 3. Load current data
with open(HOTLINES_JSON) as f:
    data = json.load(f)

# 4. Update timestamp
now = datetime.datetime.now().strftime("%Y-%m-%d")
data["meta"]["updated"] = now

# Save updated JSON
with open(HOTLINES_JSON, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 5. Copy index.html to pages repo
# (the HTML has embedded data, but the timestamp update above should flow through)
run(f"cp {INDEX_HTML} {PAGES_HTML}")

# Update the "Updated:" text in the HTML
with open(PAGES_HTML) as f:
    html = f.read()

# Replace the date in the HTML
import re
html = re.sub(r'Updated: \d{4}-\d{2}-\d{2}', f'Updated: {now}', html)

with open(PAGES_HTML, "w") as f:
    f.write(html)

# 6. Commit and push if changes
ok, out, _ = run(f"git status --porcelain", PAGES_REPO)
if out.strip():
    run(f"git add pampanga-hotlines/index.html", PAGES_REPO)
    run(f'git commit -m "Weekly refresh — hotlines verified {now}"', PAGES_REPO)
    ok, out, err = run(f"git push origin main", PAGES_REPO)
    if ok:
        log(f"✅ Pushed update to GitHub Pages — {now}")
    else:
        log(f"❌ Push failed: {err}")
else:
    log("No changes detected — data still current")

# 7. Also commit the timestamp update to the source repo
ok, out, _ = run("git status --porcelain", REPO)
if out.strip():
    run("git add hotlines.json", REPO)
    run(f'git commit -m "Weekly timestamp refresh {now}"', REPO)
    run("git push origin master", REPO)

log("Refresh complete.")
