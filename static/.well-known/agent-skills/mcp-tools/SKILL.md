# Skill: Connect to Dr. Goulu MCP Server

## What This Skill Does

Provides connection and capability details for Dr. Goulu's Model Context Protocol (MCP) server.

## When to Use It

- Accessing structured resources and tools exposed by Dr. Goulu for autonomous AI agents.
- Discovering server capabilities and endpoints per SEP-1649.

## Connection Details

- **MCP Server Card:** `https://drgoulu.com/.well-known/mcp/server-card.json`
- **Transport Type:** Streamable HTTP (`streamable-http`)
- **Endpoint URL:** `https://drgoulu.com/mcp`
- **Supported Protocol Versions:** `2026-07-28`, `2025-11-25`, `2025-06-18`

## Authentication

Public read operations do not require authentication. For agent identification and registration, refer to `https://drgoulu.com/auth.md`.
