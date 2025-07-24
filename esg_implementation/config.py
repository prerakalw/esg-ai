"""Configuration management for ESG Implementation."""
from typing import Dict, Any, Optional
import os
import yaml
from pathlib import Path
from pydantic import BaseModel, Field

class LLMConfig(BaseModel):
    """Configuration for the Google Gemini API."""
    api_key: Optional[str] = None  # Will use GOOGLE_API_KEY env var if not set
    model: str = "models/gemini-1.5-pro"  # Default Gemini model
    temperature: float = 0.7
    top_p: float = 0.95
    top_k: int = 40
    max_output_tokens: int = 2048
    safety_settings: Dict[str, int] = {
        "1": 4,  # HARM_CATEGORY_HARASSMENT: BLOCK_MEDIUM_AND_ABOVE
        "2": 4,  # HARM_CATEGORY_HATE_SPEECH: BLOCK_MEDIUM_AND_ABOVE
        "3": 4,  # HARM_CATEGORY_SEXUALLY_EXPLICIT: BLOCK_MEDIUM_AND_ABOVE
        "4": 4,  # HARM_CATEGORY_DANGEROUS_CONTENT: BLOCK_MEDIUM_AND_ABOVE
    }

class AgentConfig(BaseModel):
    """Configuration for agents."""
    verbose: bool = True
    allow_delegation: bool = True
    memory_window: int = 5

class LoggingConfig(BaseModel):
    """Configuration for logging."""
    enabled: bool = True
    level: str = "INFO"
    format: str = "%(asctime)s - %(levelname)s - %(message)s"
    date_format: str = "%Y-%m-%d %H:%M:%S"

class ESGConfig(BaseModel):
    """Main configuration for ESG Implementation."""
    llm: LLMConfig = LLMConfig()
    agents: AgentConfig = AgentConfig()
    data_path: str = "examples"
    output_path: str = "output"
    logging: LoggingConfig = LoggingConfig()
    
    @classmethod
    def load(cls, config_file: Optional[str] = None) -> "ESGConfig":
        """Load configuration from file.
        
        Args:
            config_file: Path to YAML configuration file. If None, tries to load from
                        default locations: ./esg_config.yaml or ~/.esg/config.yaml
        
        Returns:
            ESGConfig: Loaded configuration or default if no file found
        """
        if config_file is None:
            # Try default locations
            default_paths = [
                Path("esg_config.yaml"),
                Path.home() / ".esg" / "config.yaml"
            ]
            for path in default_paths:
                if path.exists():
                    config_file = str(path)
                    break
        
        if config_file is None or not Path(config_file).exists():
            # Use environment variable for API key if available
            api_key = os.environ.get("GOOGLE_API_KEY")
            return cls(llm=LLMConfig(api_key=api_key) if api_key else LLMConfig())
        
        # Load from YAML
        with open(config_file, 'r') as f:
            config_data = yaml.safe_load(f)
            return cls.model_validate(config_data)

    def save(self, config_file: str) -> None:
        """Save configuration to file.
        
        Args:
            config_file: Path where to save the configuration YAML
        """
        # Create parent directories if they don't exist
        path = Path(config_file)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert to dict and save as YAML
        config_dict = self.model_dump()
        with path.open('w') as f:
            yaml.safe_dump(config_dict, f, default_flow_style=False)
