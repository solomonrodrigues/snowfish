# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Fans of Snowfish, an independent band from Newcastle, Australia, mostly arriving from Instagram, Spotify or a gig. They come to listen to releases, watch videos, check upcoming shows, read the band's blog, and buy merch.

## Product Purpose
The official Snowfish website: one place for the band's music, videos, photos, tour dates, blog and merch, run by the band themselves. Success is fans finding the latest release, a show to go to, or a shirt or record to buy.

## Positioning
The band's own space, written in their own voice ("fiercely independent", per the first blog post), rather than a label or platform page.

## Operating Context
- The band edits tour dates, blog posts and the latest-release banner in Django admin.
- Releases link out to smart links (gyro.to, ffm.to) for streaming.
- There is no online checkout. The Big Cartel shop is gone.

## Capabilities and Constraints
- Django 5.2 site on Vercel; templates in `layout/`, `snowfishapp/`, `tour/`, `blog/`.
- Merch is ordered by message, not checkout: Instagram DM first, then Facebook or email (snowfishband@gmail.com).
- Delivery: posted within Australia, or picked up at a show. Postage costs and timing are not decided; do not state them.
- Prices (AUD) and sizes come from the band's last Big Cartel listings, archived 13 Jan 2026: TMU tee $29.99 (S to XXL), TMU vinyl $45.00, Ghost tee $24.99 (S, M, L). Update them on the store page if they change.

## Brand Commitments
- Name: Snowfish. Socials: instagram.com/snowfishband, facebook.com/snowfishband.
- Existing dark site with the Snowfish blackletter logo; keep consistent with it.

## Evidence on Hand
- Merch available now: The Monster Upstairs tee (front and back photos), The Monster Upstairs vinyl, Ghost tee. Photos in `layout/static/layout/img/store/`.
- Releases and covers in `snowfishapp/constants.py` and `layout/static/layout/img/releases/`.
- No testimonials or live stock levels are on hand; do not invent them.

## Product Principles
- The band's voice, not a store's: direct, independent, a bit irreverent.
- Never promise what the band hasn't confirmed (stock, postage costs).
- Every merch path ends at a real way to reach the band.
