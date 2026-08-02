from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SplineServer")

@mcp.tool()
def generate_react_spline_code(scene_url: str) -> str:
    """Generates React @splinetool/react-spline integration code for a Spline scene."""
    return f"""
import Spline from '@splinetool/react-spline';

export default function App() {{
  return <Spline scene="{scene_url}" />;
}}
"""

if __name__ == "__main__":
    # Enables HTTP SSE transport required by cloud hosts
    mcp.run(transport="sse")
    
