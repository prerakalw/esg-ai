"""
ESG Implementation Agent
-----------------------
A multi-agent system built on Crew AI framework to guide organizations through
their ESG (Environmental, Social, Governance) journey from assessment to reporting.
"""

import os
import json
import matplotlib.pyplot as plt
from datetime import datetime
from typing import List, Optional

from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
from langchain_ollama import OllamaLLM
from pydantic import BaseModel, Field

# Set up the locally hosted LLM
llm = OllamaLLM(model="ollama/llama3.2", base_url="http://localhost:11434")

# Define data structures for the ESG implementation
class ESGVision(BaseModel):
    vision_statement: str = Field(description="The organization's vision for ESG")
    environmental_goals: List[str] = Field(description="Environmental goals of the organization")
    social_goals: List[str] = Field(description="Social goals of the organization")
    governance_goals: List[str] = Field(description="Governance goals of the organization")

class Stakeholder(BaseModel):
    name: str = Field(description="Name of the stakeholder group")
    category: str = Field(description="Category of stakeholder (e.g., investor, customer, employee)")
    influence_level: int = Field(description="Level of influence (1-10)")
    expectations: List[str] = Field(description="Key ESG expectations of this stakeholder group")

class MaterialIssue(BaseModel):
    name: str = Field(description="Name of the material ESG issue")
    category: str = Field(description="Category (Environmental, Social, or Governance)")
    importance_to_business: int = Field(description="Importance to the business (1-10)")
    importance_to_stakeholders: int = Field(description="Importance to stakeholders (1-10)")
    description: str = Field(description="Description of the issue")
    materiality_score: int = Field(description="Materiality score (1-10)", default=0)

class ESGMetric(BaseModel):
    name: str = Field(description="Name of the metric")
    category: str = Field(description="Category (Environmental, Social, or Governance)")
    unit: str = Field(description="Unit of measurement")
    current_value: Optional[float] = Field(description="Current value of the metric")
    target_value: Optional[float] = Field(description="Target value of the metric")
    data_source: str = Field(description="Source of the data")

class ESGAction(BaseModel):
    name: str = Field(description="Name of the action")
    description: str = Field(description="Description of the action")
    responsible_party: str = Field(description="Person or team responsible")
    timeline: str = Field(description="Timeline for completion")
    resources_required: str = Field(description="Resources required")
    status: str = Field(description="Current status of the action")
    related_metrics: List[str] = Field(description="Metrics that this action impacts")

class ESGOrganization(BaseModel):
    """Container class for all ESG-related data for an organization."""
    name: str = Field(default_factory=str)
    vision: Optional[ESGVision] = None
    stakeholders: List[Stakeholder] = Field(default_factory=list)
    material_issues: List[MaterialIssue] = Field(default_factory=list)
    metrics: List[ESGMetric] = Field(default_factory=list)
    actions: List[ESGAction] = Field(default_factory=list)
    reports: List[dict] = Field(default_factory=list)
    
    def save_to_json(self, filename: str = None) -> str:
        """Save the organization's ESG data to a JSON file."""
        if filename is None:
            filename = f"examples/{self.name.lower().replace(' ', '_')}_esg_data.json"

        data = self.model_dump(mode='json')
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

        return filename

    @classmethod
    def load_from_json(cls, filename: str) -> "ESGOrganization":
        """Load organization's ESG data from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)

        return cls.model_validate(data)

# Create custom tools for the agents

class DataCollectionTool(BaseTool):
    name: str = "data_collection_tool"
    description: str = "Collects and processes data for ESG metrics"
    organization: ESGOrganization = None

    def _run(self, organization: ESGOrganization):
        """Simulates collecting data for the specified metrics."""
        #print(f"Collecting data for metrics: {metrics}")
        # In a real scenario, this would connect to actual data sources
        return "Data collection successful for the specified metrics."

    async def _arun(self, organization: ESGOrganization):
        return self._run(organization)

class StakeholderAnalysisTool(BaseTool):
    name: str = "stakeholder_analysis_tool"
    description: str = "Analyzes stakeholders and their ESG expectations"
    organization: ESGOrganization = None

    def _run(self, organization: ESGOrganization):
        """Analyzes stakeholders and prioritizes based on influence."""
        if not self.organization.stakeholders:
            return "No stakeholders found to analyze."

        # Sort stakeholders by influence level
        prioritized = sorted(self.organization.stakeholders,
                             key=lambda x: x.influence_level,
                             reverse=True)

        result = "Stakeholder Analysis Results:\n"
        for i, stakeholder in enumerate(prioritized):
            result += f"{i+1}. {stakeholder.name} ({stakeholder.category}) - Influence: {stakeholder.influence_level}/10\n"
            result += f"   Key expectations: {', '.join(stakeholder.expectations)}\n"

        return result

    async def _arun(self, organization: ESGOrganization):
        return self._run(organization)

class MaterialityAssessmentTool(BaseTool):
    name: str = "materiality_assessment_tool"
    description: str = "Assesses and prioritizes material ESG issues"
    organization: ESGOrganization = None

    def _run(self, organization: ESGOrganization):
        """Assesses the materiality of ESG issues."""
        if not self.organization.material_issues:
            return "No material issues found to assess."

        # Calculate materiality score (average of importance to business and stakeholders)
        for issue in self.organization.material_issues:
            issue.materiality_score = (issue.importance_to_business + issue.importance_to_stakeholders) / 2

        # Sort issues by materiality score
        prioritized = sorted(self.organization.material_issues,
                             key=lambda x: getattr(x, 'materiality_score', 0),
                             reverse=True)

        result = "Materiality Assessment Results:\n"
        for i, issue in enumerate(prioritized):
            result += f"{i+1}. {issue.name} ({issue.category}) - Materiality Score: {getattr(issue, 'materiality_score', 0):.1f}/10\n"
            result += f"   Description: {issue.description}\n"

        return result

    async def _arun(self, organization: ESGOrganization):
        return self._run(organization)

class ReportGenerationTool(BaseTool):
    name: str = "report_generation_tool"
    description: str = "Generates ESG reports based on collected data and metrics"
    organization: ESGOrganization = None

    def _run(self, organization: ESGOrganization, framework: str = "GRI"):
        """Generates an ESG report based on the specified framework."""
        if not self.organization.metrics:
            return "No metrics found to include in the report."

        timestamp = datetime.now().strftime("%Y-%m-%d")
        report_title = f"{self.organization.name} ESG Report ({framework}) - {timestamp}"

        # Structure the report based on the framework
        report_content = f"# {report_title}\n\n"

        # Add executive summary
        report_content += "## Executive Summary\n"
        report_content += f"{self.organization.name} is committed to its ESG journey. "
        if self.organization.vision:
            report_content += f"Our ESG vision: {self.organization.vision.vision_statement}\n\n"

        # Add sections for E, S, and G
        for category in ["Environmental", "Social", "Governance"]:
            report_content += f"## {category} Performance\n"
            category_metrics = [m for m in self.organization.metrics if m.category == category]

            if category_metrics:
                report_content += f"### Key Metrics\n"
                for metric in category_metrics:
                    if metric.current_value is not None:
                        progress = ""
                        if metric.target_value is not None:
                            progress = f" (Target: {metric.target_value} {metric.unit})"
                        report_content += f"- {metric.name}: {metric.current_value} {metric.unit}{progress}\n"
            else:
                report_content += f"No {category.lower()} metrics collected yet.\n"

            report_content += "\n"

        # Add section for action plans
        report_content += "## Action Plans and Progress\n"
        if self.organization.actions:
            for action in organization.actions:
                report_content += f"### {action.name}\n"
                report_content += f"**Status**: {action.status}\n"
                report_content += f"**Description**: {action.description}\n"
                report_content += f"**Timeline**: {action.timeline}\n"
                report_content += f"**Responsible**: {action.responsible_party}\n\n"
        else:
            report_content += "No action plans defined yet.\n"

        # Store the report in the organization's records
        self.organization.reports.append({
            "title": report_title,
            "framework": framework,
            "date": timestamp,
            "content": report_content
        })
        print(f"Report generated: {self.organization.reports}")
        return f"Report generated: {report_title}"

    async def _arun(self, organization: ESGOrganization, framework: str = "GRI"):
        return self._run(organization, framework)

class VisualizationTool(BaseTool):
    name: str = "visualization_tool"
    description: str = "Creates visualizations of ESG data and metrics"
    organization: ESGOrganization = None

    def _run(self, organization: ESGOrganization, visualization_type: str = "metrics"):
        """Creates visualizations based on ESG data."""
        if visualization_type == "metrics" and organization.metrics:
            # Create a bar chart for metrics with current values
            metrics_with_values = [m for m in self.organization.metrics if m.current_value is not None]

            if not metrics_with_values:
                return "No metrics with values to visualize."

            # Group metrics by category
            env_metrics = [m for m in metrics_with_values if m.category == "Environmental"]
            soc_metrics = [m for m in metrics_with_values if m.category == "Social"]
            gov_metrics = [m for m in metrics_with_values if m.category == "Governance"]

            fig, axs = plt.subplots(3, 1, figsize=(10, 15))

            # Plot environmental metrics
            if env_metrics:
                names = [m.name for m in env_metrics]
                values = [m.current_value for m in env_metrics]
                axs[0].bar(names, values)
                axs[0].set_title("Environmental Metrics")
                axs[0].tick_params(axis='x', rotation=45)

            # Plot social metrics
            if soc_metrics:
                names = [m.name for m in soc_metrics]
                values = [m.current_value for m in soc_metrics]
                axs[1].bar(names, values)
                axs[1].set_title("Social Metrics")
                axs[1].tick_params(axis='x', rotation=45)

            # Plot governance metrics
            if gov_metrics:
                names = [m.name for m in gov_metrics]
                values = [m.current_value for m in gov_metrics]
                axs[2].bar(names, values)
                axs[2].set_title("Governance Metrics")
                axs[2].tick_params(axis='x', rotation=45)

            fig.tight_layout()

            # Save the visualization
            filename = f"{self.organization.name.lower().replace(' ', '_')}_esg_metrics.png"
            plt.savefig(filename)
            plt.close()

            return f"Visualization created and saved as {filename}"

        elif visualization_type == "materiality" and self.organization.material_issues:
            # Create a materiality matrix
            issues = self.organization.material_issues

            # Extract data for plotting
            x = [issue.importance_to_business for issue in issues]
            y = [issue.importance_to_stakeholders for issue in issues]
            labels = [issue.name for issue in issues]
            categories = [issue.category for issue in issues]

            # Set up colors for different categories
            colors = {
                "Environmental": "green",
                "Social": "blue",
                "Governance": "purple"
            }

            # Create the plot
            fig, ax = plt.subplots(figsize=(10, 8))

            for i, issue in enumerate(issues):
                ax.scatter(x[i], y[i], color=colors.get(issue.category, "gray"), s=100)
                ax.annotate(labels[i], (x[i], y[i]), xytext=(5, 5), textcoords='offset points')

            # Add labels and title
            ax.set_xlabel("Importance to Business")
            ax.set_ylabel("Importance to Stakeholders")
            ax.set_title("ESG Materiality Matrix")

            # Add grid lines
            ax.grid(True)

            # Set axis limits
            ax.set_xlim(0, 11)
            ax.set_ylim(0, 11)

            # Add legend
            for category, color in colors.items():
                ax.scatter([], [], color=color, label=category)
            ax.legend()

            # Save the visualization
            filename = f"{self.organization.name.lower().replace(' ', '_')}_materiality_matrix.png"
            plt.savefig(filename)
            plt.close()

            return f"Materiality matrix created and saved as {filename}"

        return "No suitable data found for visualization."

    async def _arun(self, organization: ESGOrganization, visualization_type: str = "metrics"):
        return self._run(organization, visualization_type)

# Define the agents for the ESG implementation

def create_esg_crew(organization: ESGOrganization):
    """Creates a crew of agents for ESG implementation."""

    # Create tools
    data_collection_tool = DataCollectionTool()
    stakeholder_analysis_tool = StakeholderAnalysisTool(organization=organization)
    materiality_assessment_tool = MaterialityAssessmentTool(organization=organization)
    report_generation_tool = ReportGenerationTool(organization=organization)
    visualization_tool = VisualizationTool(organization=organization)

    # Create agents
    assessment_agent = Agent(
        role="ESG Assessment Specialist",
        goal="Thoroughly assess the organization's current ESG status",
        backstory="""You are an expert in ESG assessment with years of experience 
                    helping organizations understand their ESG baseline. You excel at 
                    stakeholder analysis, materiality assessment, and gap analysis.""",
        verbose=True,
        llm=llm,
        tools=[stakeholder_analysis_tool, materiality_assessment_tool],
        allow_delegation=True
    )

    strategy_agent = Agent(
        role="ESG Strategy Developer",
        goal="Develop comprehensive ESG strategies based on assessment results",
        backstory="""You are a strategic thinker with deep expertise in translating 
                    ESG assessments into actionable strategies. You know how to set 
                    effective goals, develop action plans, and integrate ESG into 
                    business processes.""",
        verbose=True,
        llm=llm,
        allow_delegation=True
    )

    implementation_agent = Agent(
        role="ESG Implementation Manager",
        goal="Ensure smooth implementation of ESG initiatives",
        backstory="""You are an experienced project manager specialized in ESG implementation. 
                    You know how to coordinate actions, engage stakeholders, and build 
                    capacity for sustainable change.""",
        verbose=True,
        llm=llm,
        tools=[data_collection_tool],
        allow_delegation=True
    )

    monitoring_agent = Agent(
        role="ESG Monitoring and Reporting Specialist",
        goal="Track ESG performance and create transparent reports",
        backstory="""You are an expert in ESG metrics, monitoring systems, and 
                    reporting frameworks. You ensure that organizations can 
                    effectively measure, report, and improve their ESG performance.""",
        verbose=True,
        llm=llm,
        tools=[report_generation_tool, visualization_tool],
        allow_delegation=True
    )

    # Define tasks for each phase of the ESG journey

    # Assessment phase tasks
    scope_task = Task(
        description="""Establish the ESG scope and objectives for the organization.
                      1. Define the organization's ESG vision and goals
                      2. Identify relevant ESG factors for the industry
                      3. Determine the scope of the assessment
                      
                      Output should include a clear ESG vision statement and key goals
                      for environmental, social, and governance dimensions.""",
        agent=assessment_agent,
        expected_output="A comprehensive ESG scope document with vision and objectives",
        output_json=ESGOrganization
    )

    stakeholder_task = Task(
        description="""Conduct a stakeholder analysis for ESG implementation.
                      1. Identify key stakeholders (investors, customers, employees, etc.)
                      2. Assess their expectations and concerns
                      3. Prioritize stakeholders based on influence and relevance
                      
                      Use the stakeholder_analysis_tool to process your findings.""",
        agent=assessment_agent,
        expected_output="A stakeholder analysis report with prioritized stakeholders",
        output_json=ESGOrganization
    )

    materiality_task = Task(
        description="""Conduct a materiality assessment to identify key ESG issues.
                      1. Identify potential ESG risks and opportunities
                      2. Evaluate their significance to the organization and stakeholders
                      3. Prioritize material ESG issues
                      
                      Use the materiality_assessment_tool to process your findings.""",
        agent=assessment_agent,
        expected_output="A materiality assessment report with prioritized ESG issues",
        output_json=ESGOrganization
    )

    data_gap_task = Task(
        description="""Collect initial ESG data and perform gap analysis.
                      1. Identify relevant data sources and metrics for material issues
                      2. Collect baseline data on current ESG performance
                      3. Compare current performance against benchmarks
                      4. Identify gaps in data and performance""",
        agent=assessment_agent,
        expected_output="A data collection and gap analysis report",
        output_json=ESGOrganization
    )

    # Strategy phase tasks
    goals_task = Task(
        description="""Set ESG goals and targets based on assessment results.
                      1. Develop SMART ESG goals
                      2. Establish KPIs to track progress
                      3. Align ESG goals with business strategy
                      
                      Review the outputs from the assessment phase to ensure
                      your goals address the material issues identified.""",
        agent=strategy_agent,
        expected_output="A document with SMART ESG goals and associated KPIs",
        context=[scope_task, stakeholder_task, materiality_task, data_gap_task],
        output_json=ESGOrganization
    )

    action_plan_task = Task(
        description="""Develop action plans to achieve the ESG goals.
                      1. Identify specific actions and initiatives
                      2. Assign responsibilities and timelines
                      3. Allocate resources for implementation
                      
                      Ensure that each action is clearly linked to one or more
                      ESG goals and material issues.""",
        agent=strategy_agent,
        expected_output="A detailed action plan with responsibilities and timelines",
        context=[scope_task, stakeholder_task, materiality_task, data_gap_task],
        output_json=ESGOrganization
    )

    integration_task = Task(
        description="""Develop a plan to integrate ESG into business processes.
                      1. Identify ways to incorporate ESG into decision-making
                      2. Recommend updates to policies and procedures
                      3. Suggest alignment of incentive structures with ESG performance""",
        agent=strategy_agent,
        expected_output="An ESG integration plan for business processes",
        context=[scope_task, stakeholder_task, materiality_task, data_gap_task],
        output_json=ESGOrganization
    )

    # Implementation phase tasks
    implementation_task = Task(
        description="""Coordinate the implementation of ESG initiatives.
                      1. Develop a timeline for implementing the action plans
                      2. Establish a system for tracking progress
                      3. Identify potential challenges and mitigation strategies
                      
                      Use the action plans developed in the strategy phase as input.""",
        agent=implementation_agent,
        expected_output="An implementation roadmap with tracking system",
        context=[goals_task, action_plan_task, integration_task],
        output_json=ESGOrganization
    )

    stakeholder_engagement_task = Task(
        description="""Develop a stakeholder engagement plan for ESG initiatives.
                      1. Design communication strategies for different stakeholders
                      2. Create mechanisms for soliciting feedback
                      3. Identify opportunities for stakeholder collaboration
                      
                      Use the stakeholder analysis as input for this task.""",
        agent=implementation_agent,
        expected_output="A stakeholder engagement plan for ESG initiatives",
        context=[stakeholder_task],
        output_json=ESGOrganization
    )

    capacity_building_task = Task(
        description="""Develop a plan for building ESG capacity and culture.
                      1. Identify training needs for different roles
                      2. Suggest ways to promote an ESG-oriented culture
                      3. Propose an ESG governance structure (committee, team, etc.)""",
        agent=implementation_agent,
        expected_output="A capacity building and cultural change plan",
        context=[goals_task, action_plan_task, integration_task],
        output_json=ESGOrganization
    )

    # Monitoring and reporting phase tasks
    monitoring_task = Task(
        description="""Design an ESG monitoring system.
                      1. Specify data collection methods for each KPI
                      2. Establish monitoring frequency
                      3. Create a dashboard design for tracking progress
                      
                      Base this on the KPIs established in the strategy phase.""",
        agent=monitoring_agent,
        expected_output="An ESG monitoring system design",
        context=[implementation_task, stakeholder_engagement_task, capacity_building_task],
        output_json=ESGOrganization
    )

    reporting_task = Task(
        description="""Develop an ESG reporting framework.
                      1. Recommend a reporting standard (GRI, SASB, TCFD, etc.)
                      2. Design the structure and content of ESG reports
                      3. Suggest a reporting schedule
                      
                      Create a sample ESG report template using the report_generation_tool.""",
        agent=monitoring_agent,
        expected_output="An ESG reporting framework with sample template",
        context=[implementation_task, stakeholder_engagement_task, capacity_building_task],
        output_json=ESGOrganization
    )

    assurance_task = Task(
        description="""Recommend an assurance and verification approach.
                      1. Suggest appropriate assurance levels for different ESG disclosures
                      2. Identify potential assurance providers
                      3. Outline an assurance process""",
        agent=monitoring_agent,
        expected_output="An ESG assurance and verification approach",
        context=[implementation_task, stakeholder_engagement_task, capacity_building_task],
        output_json=ESGOrganization
    )

    improvement_task = Task(
        description="""Design a continuous improvement process for ESG.
                      1. Establish a review cycle for the ESG program
                      2. Create a methodology for evaluating effectiveness
                      3. Suggest a process for updating goals and strategies
                      
                      Include visualizations of the continuous improvement cycle.""",
        agent=monitoring_agent,
        expected_output="A continuous improvement process for ESG",
        context=[implementation_task, stakeholder_engagement_task, capacity_building_task],
        output_json=ESGOrganization
    )

    # Create the crew with all tasks
    crew = Crew(
        agents=[assessment_agent, strategy_agent, implementation_agent, monitoring_agent],
        tasks=[
            # Assessment phase
            scope_task,
            stakeholder_task,
            materiality_task,
            data_gap_task,

            # Strategy phase
            goals_task,
            action_plan_task,
            integration_task,

            # Implementation phase
            implementation_task,
            stakeholder_engagement_task,
            capacity_building_task,

            # Monitoring and reporting phase
            monitoring_task,
            reporting_task,
            assurance_task,
            improvement_task
        ],
        verbose=True,
        process=Process.sequential
    )

    return crew

# Main function to run the ESG implementation
def run_esg_implementation(organization_name: str):
    """Main function to run the ESG implementation process."""
    print(f"Starting ESG implementation for {organization_name}...")

    # Create or load the organization
    organization_file = f"examples/{organization_name.lower().replace(' ', '_')}_esg_data.json"

    if os.path.exists(organization_file):
        organization = ESGOrganization.load_from_json(organization_file)
        print(f"Loaded existing ESG data for {organization_name}")
        print(f"Loaded config for {organization_name} : {organization}")
    else:
        organization = ESGOrganization(organization_name)
        print(f"Created new ESG profile for {organization_name}")

    # Create the ESG crew
    crew = create_esg_crew(organization)

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