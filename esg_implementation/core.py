"""Core functionality for ESG Implementation."""
import json
import logging
import os
from typing import Dict, Any, Optional, List
from pathlib import Path
from crewai import Crew, Process
import google.generativeai as genai

from .config import ESGConfig
from .models import ESGOrganization
from .tools import (
    DataCollectionTool,
    StakeholderAnalysisTool,
    MaterialityAssessmentTool,
    ReportGenerationTool,
    VisualizationTool
)
from .agents import create_esg_crew
from .logging import ESGLogger

class ESGWorkflowManager:
    """Manages ESG implementation workflows."""
    
    def __init__(self, config: Optional[ESGConfig] = None):
        """Initialize the workflow manager."""
        self.config = config or ESGConfig()
        self._setup_api_key()
        self._initialize_tools()

    def _setup_api_key(self) -> None:
        """Setup Gemini API key from environment or config."""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key and hasattr(self.config, "llm") and hasattr(self.config.llm, "api_key"):
            api_key = self.config.llm.api_key
        
        if not api_key:
            raise ValueError("Gemini API key not found in environment or config")
        
                # Configure Google Generative AI with API key and latest API version
        genai.configure(api_key=api_key)
        
        # List available models
        print("Available models:")
        for model in genai.list_models():
            print(f"- {model.name}")

    def _initialize_tools(self) -> None:
        """Initialize ESG implementation tools."""
        self.tools = {
            "data_collection": DataCollectionTool(),
            "stakeholder_analysis": StakeholderAnalysisTool(),
            "materiality_assessment": MaterialityAssessmentTool(),
            "report_generation": ReportGenerationTool(),
            "visualization": VisualizationTool()
        }

    def load_or_create_organization(self, name: str, data_path: Optional[str] = None) -> ESGOrganization:
        """Load an existing organization or create a new one."""
        if data_path is None:
            data_path = Path(self.config.data_path) / f"{name.lower().replace(' ', '_')}_esg_data.json"

        try:
            if data_path.exists() and data_path.stat().st_size > 0:
                return ESGOrganization.load_from_json(str(data_path))
        except (json.JSONDecodeError, IOError) as e:
            self.logger.warning(f"Could not load organization data: {e}")
        
        return ESGOrganization(name=name)

    def save_organization_data(self, organization: ESGOrganization, data_path: Optional[str] = None) -> Path:
        """Save organization data to file."""
        if data_path is None:
            # Ensure data path exists in config
            if not hasattr(self.config, "data_path"):
                self.config.data_path = "examples"  # Default to examples directory
            
            data_path = Path(self.config.data_path) / f"{organization.name.lower().replace(' ', '_')}_esg_data.json"
        
        # Ensure directory exists
        data_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save data
        with data_path.open('w') as f:
            json_data = organization.model_dump_json(indent=2)
            f.write(json_data)
        
        return data_path

    def create_workflow(self, organization: ESGOrganization) -> Crew:
        """Create an ESG implementation workflow."""
        # Import task creation functions
        from .tasks import (
            create_assessment_tasks,
            create_strategy_tasks,
            create_implementation_tasks,
            create_monitoring_tasks
        )

        # Create agents with tools and config
        agents = create_esg_crew(self.tools, self.config)

        # Create all tasks
        assessment_tasks = create_assessment_tasks(agents[0])
        strategy_tasks = create_strategy_tasks(agents[1], assessment_tasks)
        implementation_tasks = create_implementation_tasks(agents[2], strategy_tasks, assessment_tasks[1])
        monitoring_tasks = create_monitoring_tasks(agents[3], implementation_tasks)

        # Create and configure crew
        return Crew(
            agents=agents,
            tasks=(
                assessment_tasks +
                strategy_tasks +
                implementation_tasks +
                monitoring_tasks
            ),
            verbose=True,
            process=Process.sequential
        )

    def run_implementation(self, organization_name: str) -> Dict[str, Any]:
        """Run the complete ESG implementation process."""
        # Load or create organization
        organization = self.load_or_create_organization(organization_name)

        # Create and run workflow
        crew = self.create_workflow(organization)
        result = crew.kickoff()

        # Save updated organization data
        saved_path = self.save_organization_data(organization)
        print(f"ESG implementation completed. Data saved to {saved_path}")

        return result

    def create_workflow(self, organization: ESGOrganization) -> Crew:
        """Create an ESG implementation workflow."""
        # Import task creation functions
        from .tasks import (
            create_assessment_tasks,
            create_strategy_tasks,
            create_implementation_tasks,
            create_monitoring_tasks
        )

        # Create agents with tools and config
        agents = create_esg_crew(self.tools, self.config)

        # Create all tasks
        assessment_tasks = create_assessment_tasks(agents[0])
        strategy_tasks = create_strategy_tasks(agents[1], assessment_tasks)
        implementation_tasks = create_implementation_tasks(agents[2], strategy_tasks, assessment_tasks[1])
        monitoring_tasks = create_monitoring_tasks(agents[3], implementation_tasks)

        # Create and configure crew
        return Crew(
            agents=agents,
            tasks=(
                assessment_tasks +
                strategy_tasks +
                implementation_tasks +
                monitoring_tasks
            ),
            verbose=True,
            process=Process.sequential
        )

    def run_implementation(self, organization_name: str) -> Dict[str, Any]:
        """Run the complete ESG implementation process."""
        # Load or create organization
        organization = self.load_or_create_organization(organization_name)

        # Create and run workflow
        crew = self.create_workflow(organization)
        result = crew.kickoff()

        # Save updated organization data
        saved_path = self.save_organization_data(organization)
        print(f"ESG implementation completed. Data saved to {saved_path}")

        return result
