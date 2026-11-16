"""Run this in the portfolio folder after adding photos:  python build_photos.py
Reads photos/<series>/ and reels/ and writes photos.js for index.html."""
import os, re, json
SERIES = ["couple","wedding","maternity","birthday","corporate","family","anniversary"]
IMG = (".jpg",".jpeg",".png",".webp",".avif")
VID = (".mp4",".webm",".mov")
nat = lambda t: [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", t)]
def files(folder, exts):
    if not os.path.isdir(folder): return []
    return sorted([f for f in os.listdir(folder) if f.lower().endswith(exts)], key=nat)
out, root = {}, "photos"
folders = {d.lower(): d for d in os.listdir(root)} if os.path.isdir(root) else {}
for sid in SERIES:
    real = folders.get(sid)
    out[sid] = files(os.path.join(root, real), IMG) if real else []
    print(f"{sid}: {len(out[sid])} photos" + ("" if real else "  (folder not found)"))
out["reels"] = files("reels", VID)
print(f"reels: {len(out['reels'])} videos")
with open("photos.js", "w", encoding="utf-8") as f:
    f.write("window.PHOTOS=" + json.dumps(out, ensure_ascii=False) + ";")
print("Done: photos.js written. Open index.html.")
