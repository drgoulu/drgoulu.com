# auth.md - Dr. Goulu Agent Authentication

This document describes authentication and agent access policies for [Dr. Goulu](https://drgoulu.com/).

## Overview

Dr. Goulu is a public science communication and educational blog. All articles, media, RSS feeds, and machine-readable exports are openly accessible to legitimate readers and automated agents.

## Metadata Endpoints

- **OAuth Protected Resource Metadata (RFC 9728):**
  `https://drgoulu.com/.well-known/oauth-protected-resource`
- **OAuth 2.0 Authorization Server Metadata (RFC 8414):**
  `https://drgoulu.com/.well-known/oauth-authorization-server`
- **OpenID Connect Discovery 1.0:**
  `https://drgoulu.com/.well-known/openid-configuration`
- **API Catalog (RFC 9727):**
  `https://drgoulu.com/.well-known/api-catalog`

## Agent Access & Registration

- **Target Audience:** Autonomous AI agents, web crawlers, research indexers, and assistive tools.
- **Access Model:** Public read (no credential required for standard reading).
- **Bearer Authentication:** Supported via HTTP `Authorization: Bearer <token>` header where applicable.
- **Authorization Server:** `https://drgoulu.com`
- **Agent Registration Endpoint:** `https://drgoulu.com/oauth/register`
- **Supported Identity Types:** `anonymous`, `identity_assertion`
- **Credential Types:** `api_key`
