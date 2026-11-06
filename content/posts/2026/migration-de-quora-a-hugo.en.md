---
title: 'Migration: from Quora to Hugo'
date: 2026-09-17
draft: false
tags:
  - Quora
  - Hugo
  - Computing
  - Migration
categories:
  - Comment
slug: 'migration-de-quora-a-hugo'
coverImage: ./images/fea4d197-1588-4364-a829-955e901a8c18.jpeg
---

Between 2019 and 2026, I largely neglected this blog, but I was extremely [active on Quora](https://fr.quora.com/profile/Dr-Goulu).

Initially, I was looking for a platform better suited to [Kidi'Sciences](https://kidiscience.cafe-sciences.org), the youth-oriented branch of the C@fé des sciences network. Since WordPress was poorly tailored to handling Q&As, I stumbled across Quora back when it was launching in French. But they weren't interested ("What? A platform where adults answer kids? Are you out of your minds..." the American team replied...)

## From DrGoulu to Quora...

On reflection, they weren't entirely wrong, and gradually getting hooked on the format, I realized my blog articles sometimes targeted too narrow an audience. Perhaps it was more constructive to answer questions other people were actually asking, rather than just my own.

My roughly 15,000 answers on Quora since 2019 are viewed around 50,000 times a week and drive significant traffic back to drgoulu.com. However, Quora gradually felt like it had morphed into "just another social network."

In the beginning, real names were required, and outstanding humans (Silhem, then Amaury) handled moderation with strict criteria that guaranteed high content quality.

Then Quora's business model crystallized: funnel search traffic from Google queries into Quora. This meant accepting virtually any nonsensical question, with little regard for the quality of the answers.

## ... and Back Again

My decision to revive the drgoulu.com blog was deeply tied to Quora fatigue. Yet beyond [migrating drgoulu.com's legacy content from WordPress](/2026/08/24/migration/), it made complete sense to also migrate my Quora content over to the new Hugo site.

Fortunately, authors of Quora answers retain ownership of their content and can request a full export.

Upon request, I received 23 `.zip` files totaling 222 MB, each containing a single `.html` file archiving about a thousand of my contributions along with a folder of associated images.

### (Quora-importer...)

At that point, I still assumed I would keep drgoulu.com on WordPress. I began by creating (through pure vibe coding) a PHP-based Quora import plugin for WordPress: [quora-importer](https://github.com/goulu/quora-importer).

It worked reasonably well, inserting articles and images directly into the WordPress database. But I hit a snag:

The topics for each answer were not included in the `.html` files (inside the `.zip`s, if you're following along...), so they had to be fetched directly from each answer's live Quora page.

Except the URL of that page wasn't in the `.html` file either...

So the importer had to reconstruct the URL from the answer's title and the author's name.

Except Quora truncates title lengths and turns certain special characters into hyphens while leaving others untouched—a conversion algorithm that changed over time...

Consequently, resolving a single topic sometimes took multiple web requests, was quite convoluted, and web hosts don't particularly appreciate a website pinging an external service repeatedly. In fact, WordPress flatly rejected listing my plugin in their official directory...

### (... and Quora2WordPress)

I then "vibe coded" [quora2wordpress](https://github.com/goulu/quora2wordpress), another tool written in Python that converts the `.zip` archives into `.xml` files in WordPress WXR format, ready for standard import.

That's when I realized how tedious refining this tool was: it required multiple steps just to preview the converted Quora posts, spot defects, and restart the entire export/import process.

### Quora2Hugo

Whereas with a static site generator like Hugo, I could inspect the result immediately and make corrections directly on the converted Markdown files instead of having to rerun everything from scratch.

This was one of the key factors that solidified my decision to abandon WordPress for a static site generator—Hugo, in this case.

Once that decision was made, I simply asked my favorite AI to build [quora2hugo](https://web.archive.org/web/20260917/https://github.com/drgoulu/quora2hugo) based on quora2wordpress, outputting individual Markdown files for each article, placing images in their proper folders, and generating Hugo shortcodes for images, links, bibliographic references, and more.

Furthermore, I didn't want to drown drgoulu.com under 15,000 Quora posts, many of which were one-line answers. So I configured any answer shorter than 500 characters to be treated as a draft that I could publish manually if desired.

After a few days of fine-tuning, the new Hugo-powered drgoulu.com hosts:

- The 695 "legacy" articles of drgoulu.com from WordPress
- 6,832 new articles converted from Quora!
- And 11,815 drafts...
