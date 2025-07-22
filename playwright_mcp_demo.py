import sys, os, asyncio
#os.environ["OPENAI_API_KEY"] = ""
from dotenv import load_dotenv  # ✅ Add this
load_dotenv(dotenv_path=".env")
print("Using OpenAI API key:", os.getenv("OPENAI_API_KEY"))                  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServerStdio

async def run(agent, mcp_servers):
    print(f"\nRunning agent with servers: {[s.name for s in mcp_servers]}")
    # Read prompt from markdown file
    with open("playwright_mcp_demo.md", "r", encoding="utf-8") as f:
        prompt = f.read()
    result = await Runner.run(starting_agent=agent, input=prompt)
    print("Result:", result.final_output)

async def main():
    # Existing servers (filesystem & time), optional
    servers = []

    # Add Playwright MCP server
    servers.append(MCPServerStdio(
        name="Playwright MCP",
        params={
            "command": "npx",
            "args": ["@playwright/mcp"]
        },
        cache_tools_list=True
    ))

    # Use context manager to start servers
    async with servers[0] as playwright_server:
        agent = Agent(
            name="WebAgent",
            instructions="Use the browser automation tool to fetch web page data.",
            mcp_servers=[playwright_server],
            model="gpt-3.5-turbo"
        )
        await run(agent, [playwright_server])

if __name__ == "__main__":
    asyncio.run(main())
