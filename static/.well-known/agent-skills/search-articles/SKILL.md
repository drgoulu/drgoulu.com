# Skill: Search and Read Dr. Goulu Articles

## What This Skill Does

Enables AI agents to discover, search, and retrieve articles published on Dr. Goulu (https://drgoulu.com). Dr. Goulu is a French-language science, technology, mathematics, and philosophy blog active since 2004 with over 1,000 in-depth articles.

## When to Use It

- Searching for articles on scientific subjects (physics, astronomy, biology, mathematics).
- Reading full article content formatted specifically for AI/LLMs in Markdown.
- Browsing historical archives and citations.

## How to Retrieve Content

### 1. Markdown Content Negotiation

For any article URL on `drgoulu.com`, request the page with an `Accept: text/markdown` header to receive the raw markdown content directly:

```http
GET /2026/09/slug/ HTTP/1.1
Host: drgoulu.com
Accept: text/markdown
```

### 2. Indexes and Overviews

- **LLM Summary Index:** `https://drgoulu.com/llms.txt`
- **Full LLM Content Index:** `https://drgoulu.com/llms-full.txt`
- **RSS Feed:** `https://drgoulu.com/index.xml`
- **Sitemap:** `https://drgoulu.com/sitemap.xml`

### 3. Client Side Search

Search queries can be matched against the sitemap or the pre-indexed Pagefind index at `https://drgoulu.com/pagefind/pagefind.js`.
