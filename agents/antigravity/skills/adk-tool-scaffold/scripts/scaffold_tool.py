import sys
import os

# Ultra-simple template expansion script
def generate_tool(tool_name):
    # Robustly find the template relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = os.path.dirname(script_dir)
    template_path = os.path.join(skill_root, "resources", "ToolTemplate.py.hbs")
    output_filename = f"{tool_name}Tool.py"
    
    if os.path.exists(output_filename):
        print(f"Error: {output_filename} already exists.")
        sys.exit(1)

    with open(template_path, 'r') as f:
        content = f.read()

    # CamelCase to snake_case simple conversion
    snake_case = ''.join(['_' + c.lower() if c.isupper() else c for c in tool_name]).lstrip('_')
    
    # Replace variables
    content = content.replace("{{ToolName}}", tool_name)
    content = content.replace("{{tool_name}}", snake_case)
    content = content.replace("{{toolDescription}}", f"Tool functionality for {tool_name}")

    with open(output_filename, 'w') as f:
        f.write(content)
    
    print(f"Successfully generated {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scaffold_tool.py <ToolName>")
        sys.exit(1)
    
    generate_tool(sys.argv[1])
