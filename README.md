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

# 7. Run the demo
python playwright_mcp_demo.py
```