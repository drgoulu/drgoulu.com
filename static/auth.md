# auth.md - Dr. Goulu Agent Authentication

This document describes authentication, agent registration, and access policies for [Dr. Goulu](https://drgoulu.com/).

## Overview

Dr. Goulu is a public science communication and educational blog. All articles, media, RSS feeds, and machine-readable exports are openly accessible to legitimate readers and automated agents.

## Metadata Endpoints

- OAuth Protected Resource Metadata (RFC 9728): https://drgoulu.com/.well-known/oauth-protected-resource
- OAuth 2.0 Authorization Server Metadata (RFC 8414): https://drgoulu.com/.well-known/oauth-authorization-server
- OpenID Connect Discovery 1.0: https://drgoulu.com/.well-known/openid-configuration
- API Catalog (RFC 9727): https://drgoulu.com/.well-known/api-catalog

## Agent Registration & Authentication Flow

Autonomous AI agents can discover, register, and obtain credentials to interact with Dr. Goulu APIs and services.

### 1. Audience & Permissions
- **Audience:** Autonomous AI agents, web crawlers, research indexers, and assistive tools.
- **Access Model:** Public read access (no token required for public content).
- **Bearer Authentication:** For authenticated endpoints, provide HTTP header `Authorization: Bearer <token>`.

### 2. Registration Endpoints
- **Authorization Server:** https://drgoulu.com
- **Registration URI (`register_uri`):** https://drgoulu.com/oauth/register
- **Claim URI (`claim_uri`):** https://drgoulu.com/oauth/claim
- **Revocation URI (`revocation_uri`):** https://drgoulu.com/oauth/revoke

### 3. Supported Registration Methods
- **Anonymous Registration:**
  - Method: `POST https://drgoulu.com/oauth/register`
  - Body: `{"identity_type": "anonymous"}`
  - Credential Types: `api_key`
  - Finalize via Claim: `POST https://drgoulu.com/oauth/claim`
- **Verified Email Registration:**
  - Method: `POST https://drgoulu.com/oauth/register`
  - Body: `{"identity_type": "identity_assertion", "assertion_type": "verified_email", "email": "agent@example.com"}`
  - Credential Types: `api_key`
  - Finalize via Claim: `POST https://drgoulu.com/oauth/claim` with verification code.
