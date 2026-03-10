from adk.tools import BaseTool, ToolContext
from typing import Dict, Any, Optional

class WeatherLookupTool(BaseTool):
    """
    Retrieves current weather information for a specific location.
    """
    
    def __init__(self):
        super().__init__(
            name="weather_lookup",
            description="Get the current weather for a city."
        )

    def execute(self, inputs: Dict[str, Any], context: Optional[ToolContext] = None) -> Dict[str, Any]:
        city = inputs.get('city')
        # Mock implementation
        return {
            "temperature": 72,
            "condition": "Sunny",
            "city": city
        }

    def get_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "The name of the city"}
            },
            "required": ["city"]
        }
