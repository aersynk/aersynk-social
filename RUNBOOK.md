# Weekly run: how the AerSynk social queue is kept full

Read this first on every scheduled run. It is the rulebook for building and scheduling posts.

## Accounts (Buffer, free plan)
- Organisation: `6acf206beeddaaa8667f8afa`
- Instagram `6acf217c778b240e2f04408b` (auto-shares to the Facebook page through Meta)
- LinkedIn `6acf4c94778b240e2f05d74a`
- TikTok `6acf513b778b240e2f05f437`
- Free plan: at most 10 scheduled posts per channel at any time. Never pay for anything or upgrade.

## Plan
- `plan/calendar-2026-10.json`: the original 30-day plan. Keep it; every image post in it still goes out.
- `plan/calendar-combined.json`: images plus Reels, weekly pattern and what comes next.
- Instagram: Mon carousel 18:30, Tue new Reel 18:30, Wed original-plan Reel 12:30, Thu new Reel 12:30, Fri single image 12:30, Sun carousel 18:00.
- TikTok: every Reel, same day 19:30. LinkedIn: original-plan posts at 08:00.
- After the 30-day plan runs out (17 Nov), continue the same pattern with new educational topics from aersynk.io's services.
  Mix images and Reels; never Reels only.

## Building
1. `pip install --break-system-packages piper-tts playwright` (Chromium is already installed; do not run `playwright install`).
2. Voice: download `https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-en-us-ryan-high.tar.gz`
   and extract it so `/tmp/piper-voices/en-us-ryan-high.onnx` (and its `.onnx.json`) exist.
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
