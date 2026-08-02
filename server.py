from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server binding to port 8000
mcp = FastMCP("SplineServer", host="0.0.0.0", port=8000)

@mcp.tool()
def generate_react_spline_code(scene_url: str) -> str:
    """Generates React @splinetool/react-spline integration code for a Spline scene."""
    return f"""
import Spline from '@splinetool/react-spline';

export default function App() {{
  return (
    <div style={{{{ width: '100%', height: '100vh' }}}}>
      <Spline scene="{scene_url}" />
    </div>
  );
}}
"""

@mcp.tool()
def generate_spline_event_listener(object_name: str, action_type: str = "mouseDown") -> str:
    """Generates JS event listener snippet for a Spline scene object."""
    return f"""
spline.addEventListener('{action_type}', (e) => {{
  if (e.target.name === '{object_name}') {{
    console.log('Triggered {action_type} on {object_name}');
  }}
}});
"""

if __name__ == "__main__":
    mcp.run(transport="sse")
    
