# Daily run: how the AerSynk social queue is kept full

Read this first on every scheduled run (daily, 06:47 SAST). It is the rulebook for building and scheduling posts.

## Accounts (Buffer, free plan)
- Organisation: `6acf206beeddaaa8667f8afa`
- Instagram `6acf217c778b240e2f04408b` (auto-shares to the Facebook page through Meta)
- LinkedIn `6acf4c94778b240e2f05d74a`
- TikTok `6acf513b778b240e2f05f437`
- Free plan: at most 10 scheduled posts per channel at any time. Never pay for anything or upgrade.

## Plan (from 14 Oct 2026: maximum posting on the free plan)
- The free plan allows 10 scheduled posts per channel at once (not per week). The task runs DAILY and tops every
  channel back up to 10, so posting volume is limited only by the cadence below.
- Instagram (auto-shares to Facebook): 2 a day, every day. 12:30 and 18:30. Alternate one Reel and one image
  post (carousel or single) each day, so the feed stays a mix; never Reels only.
- TikTok: 2 Reels a day, 12:30 and 19:30. Use the day's Instagram Reel plus one more Reel.
- LinkedIn: 1 a day, Monday to Friday, 08:00 (a 17:30 slot is fine when a morning has passed). No weekends.
- Daily build target: about 2 new Reels and 1 new image post, plus a LinkedIn caption for one of them.
- Content order: `plan/calendar-combined.json` (`next` list) first, which includes the original 30-day plan in
  `plan/calendar-2026-10.json` (keep it; every image post in it still goes out). After that, new educational
  topics from aersynk.io's services: mapping and surveying, inspections, agriculture, security, drone integration
  and consulting, AerSynk Survey (prototype) and AerSynk Rescue (in development).
- Never repost the same file to the same channel. Reels can go to Instagram, TikTok and LinkedIn once each.

## Building
1. `pip install --break-system-packages playwright` (Chromium is already installed; do not run `playwright install`).
2. Voice (Kokoro, free and offline, natural-sounding; replaces the old robotic Piper voice):
   `pip install --break-system-packages kokoro-onnx soundfile`, then download both files into `/tmp/kokoro/`:
   `https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx` and
   `https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin`
   (Hugging Face is blocked here; GitHub works). The voice is set in `tools/reel_engine.py` (`REEL_VOICE`,
   default `bf_emma`, British woman, chosen by Kwazi). Use the same voice on every Reel. Piper remains available with `REEL_VOICE_ENGINE=piper`.
   Pronunciation: AerSynk is said "Air Sync" and aersynk.io is said "air sync dot eye oh" (handled in `SAY` in
   `tools/reel_engine.py`; add any new brand words there). Voice speed 1.0: a natural pace, not slow, not fast.
3. Reels: add a spec to a `tools/reels_YYYY_MM.py` file (see `tools/reels_2026_10.py`, `tools/reel_engine.py`, `tools/art.py`),
   run it, then check frames with `tools/contact_sheet.py` and fix overlaps or overflowing text before publishing.
4. Images: follow `tools/images_2026_10.py` (1080x1350, `tools/render.py`). Look at every image before using it.
5. Write captions, alt text and hashtags into `posts/YYYY-MM/batch-N.json`, in the style of `posts/2026-10/batch-1.json`.
6. Commit as user `AerSynk` / `aersynk@gmail.com` and push to `main`. Buffer fetches media from
   `https://raw.githubusercontent.com/aersynk/aersynk-social/main/posts/...`.

## Scheduling
- `list_posts` (status scheduled and sent) first. Never create a post that already exists for that channel and date.
- `create_post`, mode `customScheduled`, `schedulingType` `automatic`, `dueAt` with `+02:00`.
- Instagram Reels: metadata `{"instagram": {"type": "reel", "shouldShareToFeed": true, "isAiGenerated": true}}`.
  Instagram images: `{"instagram": {"type": "post", "shouldShareToFeed": true}}`. TikTok: `{"tiktok": {"isAiGenerated": true}}`.
- Record each Buffer post ID in the batch file. Say "scheduled" only when Buffer returns status scheduled,
  and "published" only when Buffer shows it as sent.

## Content rules (never break these)
- No invented clients, projects, results, statistics, testimonials, certifications or capabilities.
- AerSynk does not hold its own ROC. Kwazi flies as a BVLOS-certified remote pilot under an approved partner
  operator's certificate. Say so wherever operations are mentioned.
- AerSynk Survey is a working prototype on demo data. AerSynk Rescue is in development, not live.
- Animated illustrations only, labelled as such; voice-over labelled computer-generated. No copyrighted media.
- No bought followers, engagement bots, mass-following, or unsolicited messages. No paid APIs.
- Contact: aersynk.io, WhatsApp or call 073 290 4298, aersynk@gmail.com.

## Report
Finish with a short summary for Kwazi: what was scheduled (dates, channels), what went out last week,
the week's Buffer metrics (`get_aggregated_post_metrics`), and anything that needs him (comments and DMs to answer,
failed posts, Facebook auto-share not working).
