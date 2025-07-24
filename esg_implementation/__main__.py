"""Main module for running ESG implementation."""
import os
from crewai import Process
from .models import ESGOrganization
from .agents import create_esg_crew
from .tasks import (
    create_assessment_tasks,
    create_strategy_tasks,
    create_implementation_tasks,
    create_monitoring_tasks
)

def run_esg_implementation(organization_name: str) -> dict:
    """Run the complete ESG implementation process."""
    print(f"Starting ESG implementation for {organization_name}...")

    # Create or load the organization
    organization_file = f"examples/{organization_name.lower().replace(' ', '_')}_esg_data.json"

    if os.path.exists(organization_file):
        organization = ESGOrganization.load_from_json(organization_file)
        print(f"Loaded existing ESG data for {organization_name}")
    else:
        organization = ESGOrganization(name=organization_name)
        print(f"Created new ESG profile for {organization_name}")

    # Create the ESG crew
    crew = create_esg_crew(organization)

    # Create and organize tasks for each phase
    assessment_tasks = create_assessment_tasks(crew.agents[0])  # assessment agent
    strategy_tasks = create_strategy_tasks(crew.agents[1], assessment_tasks)  # strategy agent
    implementation_tasks = create_implementation_tasks(crew.agents[2], strategy_tasks, assessment_tasks[1])  # implementation agent
    monitoring_tasks = create_monitoring_tasks(crew.agents[3], implementation_tasks)  # monitoring agent

    # Configure crew with all tasks
    crew.tasks = (
        assessment_tasks +
        strategy_tasks +
        implementation_tasks +
        monitoring_tasks
    )
    crew.process = Process.sequential

    # Run the crew to execute the ESG implementation process
    result = crew.kickoff()

    # Save the updated organization data
    saved_file = organization.save_to_json()
    print(f"ESG implementation completed. Data saved to {saved_file}")

    return result

if __name__ == "__main__":
    # Example usage
    organization_name: str = "TechInnovate"
    result = run_esg_implementation(organization_name)
    print("ESG Implementation Summary:")
    print(result)

    print("Sustainability is everyone's responsibility!")
