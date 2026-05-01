# InnovateSwarm MCP Server

**Public MCP (Model Context Protocol) Server** for the InnovateSwarm innovation workflow templates.

Connect any MCP-compatible AI (Claude Desktop, Cursor, Windsurf, etc.) directly to our library of powerful multi-agent innovation prompts.

---

## 🚀 Quick Connect

**MCP URL:**
https://fastmcptemplate-production-1014.up.railway.app/mcp


**Server Name:** `InnovateSwarm`

### How to Use
1. Open **Claude Desktop** or **Cursor**
2. Go to MCP Settings → **Add New Server**
3. Select **Remote (Streamable HTTP)**
4. Paste the URL above
5. Start using the templates!

---

## Available Templates

| Command | Description |
|---------|-------------|
| `@swarm://templates` | List all available templates |
| `@swarm://agent-safety` | Stabilized environment for agent to agent interaction |
| `@swarm://brain-agent` | Executive brain for management and delegation of a specialized agent system |
| `@swarm://cross-pollination-engine` | Combine ideas across unrelated domains |
| `@swarm://idea-factory` | Rapid idea generation + ranking |
| `@swarm://idea-rescue` | Rescue and strengthen weak ideas |
| `@swarm://innovation-critique` | Rigorous red-team critique |
| `@swarm://iterative-innovation` | Cycles of innovation |
| `@swarm://future-backcasting` | Work backwards from a successful future |
| `@swarm://mve` | Design Minimal Viable Experiments |
| `@swarm://swarm-tank` | Shark Tank-style investor pitch simulation |
| `@swarm://refresh-perspective` | Shark Tank-style investor pitch simulation |


---

## Project Structure
innovate-swarm-mcp/
├── templates/                  # All innovation workflows
│   ├── idea-rescue/
│   ├── idea-factory/
│   ├── swarm-tank/
│   └── ...
├── server.py                   # Main MCP server
├── Dockerfile
└── pyproject.toml


---

## Local Development

```bash
git clone https://github.com/InnovateSwarm/innovate-swarm-mcp.git
cd innovate-swarm-mcp
````

# Install dependencies
uv sync

# Run locally
uv run server.py

Then connect using stdio transport in your MCP client.

Deployed OnRailway (Live)
Fully open source


Made with love by InnovateSwarm
Website | MCP Page | Original Templates
Star the repo if you find it useful! 

