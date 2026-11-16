# Aadi – Photography Portfolio

Single-page static site (no build tools). Open `index.html` in a browser.

## Structure
- `index.html` – the whole site (HTML, CSS, JS). Do not split it up.
- `build_photos.py` – scans `photos/<series>/` and `reels/`, writes `photos.js`.
- `photos/<series>/` – one folder per event type, any file names:
  - `couple` = Love in Frames
  - `wedding` = Wedding Chronicles
  - `maternity` = Motherhood Stories
  - `birthday` = Birthday Stories
  - `corporate` = Corporate in Focus
  - `family` = Family Stories
  - `anniversary` = Anniversaries
- `reels/` – vertical videos (.mp4/.webm/.mov), shown in the Reels section.

## Adding photos
1. Drop photos into the right `photos/<series>/` folder (resize to ~2000px long side, under ~500 KB each).
2. Run `python build_photos.py` (re-run whenever files change).
3. Open `index.html`. For a local preview server: `python -m http.server`.

## Prompt for Antigravity
> I have unsorted photos in the folder `incoming/`. Look at each photo and move it into the matching `photos/<series>/` folder (couple, wedding, maternity, birthday, corporate, family, anniversary). Resize each to max 2000px on the long side as JPEG quality 85 (use Pillow). Move videos to `reels/`. Then run `python build_photos.py` and tell me how many files went in each folder. Do not edit `index.html`.

## Notes
- Contact details and copy buttons are near the top (hero) and in the footer of `index.html`.
- Instagram link in the footer still says `yourhandle`; replace it with the real handle.
