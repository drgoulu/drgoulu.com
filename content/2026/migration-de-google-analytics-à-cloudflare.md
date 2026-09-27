---
title: 'Migration : de Google Analytics à Cloudflare'
date: 2026-09-27
draft: true
tags:
  - migration
  - google
  - cloudflare
categories:
  - Comment
slug: ''
coverImage: ./images/cloudflare.png
---

Sur l'ancien drgoulu.com, j'utilisais Google Analytics pour obtenir les statistiques sur l'accès au site. J'aurais pu continuer avec eux, mais

1. je suis dans un processus de deGAFAMisation
2. j'étais intrigué depuis quelques temps par ce petit widget

{{< figure align="alignright" src="./images/cloudflare.png" >}}


# Implement Link Response Headers

Add Link response headers to your homepage for agent discovery per

[RFC 8288](https://www.rfc-editor.org/rfc/rfc8288) and

[RFC 9727 Section 3](https://www.rfc-editor.org/rfc/rfc9727#section-3).

## Requirements

- Return \`Link\` headers on your homepage response pointing to machine-readable resources

- Use registered relation types: \`api-catalog\`, \`service-desc\`, \`service-doc\`, \`describedby\`

- Example: \`Link: </.well-known/api-catalog>; rel="api-catalog"\`

- Multiple Link headers or comma-separated values are both valid

## Cloudflare

Use [Transform Rules](https://developers.cloudflare.com/rules/transform/) or

[Workers](https://developers.cloudflare.com/workers/) to add Link headers

without modifying your origin server.

## Validate

\`\`\`

POST https://isitagentready.com/api/scan

Content-Type: application/json

{"url": "https://drgoulu.com"}

\`\`\`

Check that \`checks.discoverability.linkHeaders.status\` is \`"pass"\`.
