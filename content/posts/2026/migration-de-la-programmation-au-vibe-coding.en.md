---
title: 'Migration: from Programming to "Vibe Coding"'
date: 2026-09-18
draft: true
tags:
  - computing
  - programming
  - artificial intelligence
  - vibe coding
categories:
  - Comment
slug: 'migration-de-la-programmation-au-vibe-coding'
coverImage: ''
---

Once again, I didn't see it coming.

Even though I've been immersed in computer science for roughly 50 years, I didn't anticipate the AI tidal wave any better than I did Nvidia, crypto, Google, or Apple, among others.

A few years ago, I thought programming would be one of the very last jobs to be automated. I completely underestimated the astonishing speed at which AI models could learn from the gargantuan mountain of codebases stored on GitHub.

## The Beginnings: Dumb AIs

When I left my last job three years ago, my assessment was that AIs were glorified autocomplete engines, spitting out ugly, bug-ridden code.

My employer, deeply entangled in Microsoft's Azure ecosystem, allowed us to use Copilot provided we turned on the privacy toggle preventing enterprise code from being transmitted externally (I still wonder how that was technically achievable with an AI hosted in the US...).

One day, I asked it to write a tedious function with lots of edge cases. And suddenly, to my utter astonishment, Copilot wrote a magnificent, nuanced function, exactly the way I would have crafted it myself... so much so that a doubt struck me. I ran a quick search and yes! That was it: I had already written that exact function for another project a few years earlier!

Yet that foolish AI had duplicated the code without citing the existing implementation, let alone proposing to extract the function into a shared library to be called from both projects...

## "Junior" AIs

With a head full of projects for my "retirement," I still began using AIs for programming, somewhat in the spirit of pair programming from [Extreme programming](w:Extreme_programming) which had served me very well in past projects: I gave the AI precise, step-by-step instructions, supervising its output and correcting course whenever necessary.

It works, but it isn't drastically faster than programming alone.

Where it changes everything, however, is on the chores: documentation and unit tests materialize like magic, saving hours of mind-numbing busywork.

The AI becomes the eager junior intern who never says no, constantly showering you with "You're right, that's a much better approach" and "Oh, I see! That's very clever," which feels even more flattering than human bootlicking.

The most memorable story occurred while tracking down a hairy bug in a data-intensive program that produced an erroneous output once in a while. The AI was floundering to locate the issue, haphazardly trying random fixes without any methodology.

At one point, I stopped it and gave it an earful (I love lecturing AIs or correcting them when they're wrong...), and it apologized, saying:

> It's like looking for a needle in a haystack.

I must admit I smiled... Then I instructed it to build a structured logging system to track everything the program executed, so we could inspect the log to pinpoint what was going wrong. Its response blew me away:

> Great idea! We're still looking for a needle in a haystack, but now we have a magnet.

At that moment, I was almost terrified...

## Enter the "Agents"

At first, I didn't quite grasp what "agents" were.
