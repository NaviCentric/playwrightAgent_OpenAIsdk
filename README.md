## Quickstart: Running playwright_mcp_demo.py

Follow these steps to set up and run the Playwright MCP demo:

```powershell
# 1. Create and activate a Python virtual environment
python -m venv agents-env
agents-env\Scripts\activate   # On Windows

# 2. Install dependencies (run as administrator if needed)
pip install -e .

# 3. Install MCP server for time tools
pip install mcp-server-time

# 4. Install Playwright MCP globally
npm install -g @playwright/mcp

# 5. Install Playwright browsers
npx playwright install

# 6. (Optional) Remove OPENAI_API_KEY from environment for a clean start
Remove-Item Env:OPENAI_API_KEY

# 7. Run Playwright MCP server in a separate terminal
npx @playwright/mcp

# 8. Run the demo
python playwright_mcp_demo.py


# .env setup
Create a file named `.env` in the project root with your OpenAI API key:

```
OPENAI_API_KEY=your-key-here
```

## Modifying the Prompt

The agent prompt is read from the markdown file `playwright_mcp_demo.md` in the project root. To change the agent's instructions, simply edit the contents of this file.

For example, open `playwright_mcp_demo.md` and update the text:

```
Open example.com, extract the page title, and return it.
```

You can write any instructions you want the agent to follow. Save the file and re-run the demo script to use your new prompt.