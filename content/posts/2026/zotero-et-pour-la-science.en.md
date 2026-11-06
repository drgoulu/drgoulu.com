---
title: Zotero and Pour la Science
date: 2026-10-20
draft: false
tags:
  - internet
  - books
  - degafamisation
  - pour la science
  - vibe coding
categories:
  - Comment
slug: 'zotero-et-pour-la-science'
coverImage: ./images/zotero-et-pour-la-science.jpg
---

Since around 1990, I have used reference management software to keep track of my reading and cite papers properly. During my PhD thesis, it was [EndNote](w:EndNote) on Mac. Later, I [juggled between](/2013/10/25/comment-gerer-ses-articles/) [Zotero](w:Zotero) and [Mendeley](w:Mendeley) during my Windows years, accumulating approximately 9,430 references to journal papers, scientific books, and patents, alongside 4,827 PDF files totaling 3.4 GB.

That's not huge, but it exceeds the free storage quotas offered by Mendeley (2 GB) or Zotero (300 MB). So I placed my PDFs in Google Drive and configured the synced local folder as Mendeley's attachment directory. This gave me seamless access on my PC, and workable access from my smartphone.

## But:

1. I migrated to Linux and Proton Drive: no bidirectional background sync (or not yet...).
2. Mendeley used to offer a decent Android app, but they discontinued it, and their mobile web interface is unusable.
3. On the other hand, [Zotero has an official Android app](https://play.google.com/store/apps/details?id=org.zotero.android&hl=en)—somewhat minimal, but genuinely useful.
4. Crucially, Zotero supports storing attachments on an arbitrary [WebDAV](w:WebDAV) server, whereas Mendeley forces you into their paid subscription tiers.
5. And Mendeley is owned by Elsevier, while Zotero is open source.

## And that changes everything.

Because across 30 years of collecting papers migrated across operating systems, hard drives, and software platforms, my library had accumulated considerable damage. Fortunately, [Zotero offers countless ways to repair it](https://www.zotero.org/support/dev/).

First, I had a mountain of duplicate and triplicate entries, and Zotero only supports merging duplicates one by one by hand. Fortunately, ChenglongMa created:

### [zoplicate](https://github.com/ChenglongMa/zoplicate)

A plugin that automates bulk duplicate merging. I installed it immediately, but unfortunately it only merged entries sharing the exact same item type, whereas I had many duplicates across mismatched types like "Report" and "Journal Article."

Open Source in the age of Vibe Coding is glorious: I forked and cloned the plugin repository, and knowing absolutely nothing about Zotero's internal API or how to write plugins for it, I simply gave a prompt along the lines of:

> Allow merging references of different item types, choosing the type that minimizes information loss.

A few minutes later, I pushed a [commit doing just that](https://github.com/goulu/zoplicate/commit/6d94dc1a2a417d032bccd9ecb6b8b29c4791c5ab#diff-d04c18892ed72223035966c81d45fafcad02d90913fa5e57f6591fe1c213f06f) (complete with bilingual documentation...) and that very same day [ChenglongMa merged my Pull Request #223](https://github.com/ChenglongMa/zoplicate/pull/223). From that point on, zoplicate is substantially more capable!

## [zotero-tools](https://github.com/goulu/zotero-tools)

Duplicates weren't the only issue plaguing my collection.

Still through pure Vibe Coding, I built three utilities grouped into a single "zotero-tools" project:

1. [zotero-cleaner](https://github.com/goulu/zotero-tools#2-zotero-cleaner-zotero-cleaner): tidies up titles, tags, and orphaned attachments.
2. [pdf-importer](https://github.com/goulu/zotero-tools#1-pdf-importer-pdf-importer--zotero-import-pdf): matched all my unlinked standalone PDFs to existing library items, or created new records directly from the PDF metadata.
3. `pour-la-science`: originally intended to scrape articles from [the French magazine's site](https://www.pourlascience.fr), though I ultimately took a cleaner approach.

### Pour la Science

In fact, 4,617 of my references are articles from the French popular science magazine [Pour la Science](w:Pour_la_Science) (the French edition of *Scientific American*), to which I subscribed for decades before [canceling in frustration](/2016/12/12/bye-bye-pour-la-science/) 10 years ago. But the journal is genuinely excellent, and hoping their customer service had improved, I resubscribed...

Unfortunately, the official [Zotero Connector extension](https://chromewebstore.google.com/detail/zotero-connector/ekhagklcjbdpajgpjgmbionohlpdbjgc) for Vivaldi (and Chrome) didn't recognize the Pour la Science website to parse and import articles cleanly.

Except you can teach it to!

Fork of [https://github.com/zotero/translators](https://github.com/zotero/translators), clone, vibe coding while feeding [this documentation page](https://www.zotero.org/support/dev/translators/coding#web_translators) to the AI as a reference, a [commit](https://github.com/goulu/zotero-translators/commit/ee322a3a512bbb9359cf9faac3b3ddc349eb59d0), and [Pull Request #3699](https://github.com/zotero/translators/pull/3699): one hour later, Zotero natively imports Pour la Science articles with full metadata!

###### References

1. [Zotero vs Mendeley: The Ultimate Duel (and 2026 Tips)](https://www.stagepfe.com/2026/03/zotero-vs-mendeley-le-duel-ultime-et.html)
