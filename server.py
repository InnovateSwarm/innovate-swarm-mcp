from fastmcp import FastMCP
from pathlib import Path
from typing import Dict, Any

mcp = FastMCP("InnovateSwarm")

TEMPLATES_DIR = Path("templates")

@mcp.resource("swarm://templates")
def list_templates() -> Dict[str, Any]:
    templates = {}
    for folder in TEMPLATES_DIR.iterdir():
        if folder.is_dir() and not folder.name.startswith('.'):
            readme = folder / "README.md"
            if readme.exists():
                content = readme.read_text()
                templates[folder.name] = {
                    "name": folder.name.replace("-", " ").title(),
                    "slug": folder.name,
                    "description": content.split("\n\n")[0][:250] + "...",
                }
    return {"templates": templates, "repo": "https://github.com/InnovateSwarm/InnovateSwarm-Instructions"}

@mcp.prompt("swarm://get-template/{template_name}")
def get_swarm_template(template_name: str, **variables) -> str:
    slug = template_name.lower().replace(" ", "-").replace("_", "-")
    template_dir = TEMPLATES_DIR / slug
    if not template_dir.exists():
        available = [f.name for f in TEMPLATES_DIR.iterdir() if f.is_dir() and not f.name.startswith('.')]
        return f"Template '{template_name}' not found."
    content = (template_dir / "README.md").read_text()
    for key, value in variables.items():
        upper = key.upper()
        content = content.replace(f"{{{{ {upper} }}}}", str(value))
        content = content.replace(f"{{{{{upper}}}}}", str(value))
    return content

# Add your specific prompts
@mcp.prompt("swarm://idea-rescue")
def idea_rescue(seed_idea: str) -> str:
    return get_swarm_template("idea-rescue", SEED_IDEA=seed_idea)

# Add the rest (swarm-tank, idea-factory, etc.) the same way...

if __name__ == "__main__":
    print("🚀 InnovateSwarm MCP Server started!")
    import asyncio
    asyncio.run(mcp.run_async(transport="streamable-http"))