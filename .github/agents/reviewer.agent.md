---
name: docs-researcher
description: Reads approved external documentation through a remote MCP server.
tools:
  - read
  - search
  - context7/*
mcp-servers:
  context7:
    type: http
    url: https://mcp.context7.com/mcp
    headers:
      CONTEXT7_API_KEY: ${{ secrets.COPILOT_MCP_CONTEXT7_API_KEY }}
    tools:
      - "*"
---
