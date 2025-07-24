"""Tasks for ESG Implementation."""
from typing import List, Optional
from crewai import Agent, Task

def create_assessment_tasks(assessment_agent: Agent) -> List[Task]:
    """Create tasks for the assessment phase."""
    return [
        Task(
            description="""Establish the ESG scope and objectives for the organization.
                      1. Define the organization's ESG vision and goals
                      2. Identify relevant ESG factors for the industry
                      3. Determine the scope of the assessment
                      
                      Output should include a clear ESG vision statement and key goals
                      for environmental, social, and governance dimensions.""",
            agent=assessment_agent,
            expected_output="A comprehensive ESG scope document with vision and objectives"
        ),
        Task(
            description="""Conduct a stakeholder analysis for ESG implementation.
                      1. Identify key stakeholders (investors, customers, employees, etc.)
                      2. Assess their expectations and concerns
                      3. Prioritize stakeholders based on influence and relevance""",
            agent=assessment_agent,
            expected_output="A stakeholder analysis report with prioritized stakeholders"
        ),
        Task(
            description="""Conduct a materiality assessment to identify key ESG issues.
                      1. Identify potential ESG risks and opportunities
                      2. Evaluate their significance to the organization and stakeholders
                      3. Prioritize material ESG issues""",
            agent=assessment_agent,
            expected_output="A materiality assessment report with prioritized ESG issues"
        ),
        Task(
            description="""Collect initial ESG data and perform gap analysis.
                      1. Identify relevant data sources and metrics for material issues
                      2. Collect baseline data on current ESG performance
                      3. Compare current performance against benchmarks
                      4. Identify gaps in data and performance""",
            agent=assessment_agent,
            expected_output="A data collection and gap analysis report"
        )
    ]

def create_strategy_tasks(strategy_agent: Agent, assessment_tasks: List[Task]) -> List[Task]:
    """Create tasks for the strategy phase."""
    return [
        Task(
            description="""Set ESG goals and targets based on assessment results.
                      1. Develop SMART ESG goals
                      2. Establish KPIs to track progress
                      3. Align ESG goals with business strategy""",
            agent=strategy_agent,
            expected_output="A document with SMART ESG goals and associated KPIs",
            context=assessment_tasks
        ),
        Task(
            description="""Develop action plans to achieve the ESG goals.
                      1. Identify specific actions and initiatives
                      2. Assign responsibilities and timelines
                      3. Allocate resources for implementation""",
            agent=strategy_agent,
            expected_output="A detailed action plan with responsibilities and timelines",
            context=assessment_tasks
        ),
        Task(
            description="""Develop a plan to integrate ESG into business processes.
                      1. Identify ways to incorporate ESG into decision-making
                      2. Recommend updates to policies and procedures
                      3. Suggest alignment of incentive structures with ESG performance""",
            agent=strategy_agent,
            expected_output="An ESG integration plan for business processes",
            context=assessment_tasks
        )
    ]

def create_implementation_tasks(implementation_agent: Agent, strategy_tasks: List[Task], stakeholder_task: Optional[Task] = None) -> List[Task]:
    """Create tasks for the implementation phase."""
    return [
        Task(
            description="""Coordinate the implementation of ESG initiatives.
                      1. Develop a timeline for implementing the action plans
                      2. Establish a system for tracking progress
                      3. Identify potential challenges and mitigation strategies""",
            agent=implementation_agent,
            expected_output="An implementation roadmap with tracking system",
            context=strategy_tasks
        ),
        Task(
            description="""Develop a stakeholder engagement plan for ESG initiatives.
                      1. Design communication strategies for different stakeholders
                      2. Create mechanisms for soliciting feedback
                      3. Identify opportunities for stakeholder collaboration""",
            agent=implementation_agent,
            expected_output="A stakeholder engagement plan for ESG initiatives",
            context=[stakeholder_task] if stakeholder_task else []
        ),
        Task(
            description="""Develop a plan for building ESG capacity and culture.
                      1. Identify training needs for different roles
                      2. Suggest ways to promote an ESG-oriented culture
                      3. Propose an ESG governance structure (committee, team, etc.)""",
            agent=implementation_agent,
            expected_output="A capacity building and cultural change plan",
            context=strategy_tasks
        )
    ]

def create_monitoring_tasks(monitoring_agent: Agent, implementation_tasks: List[Task]) -> List[Task]:
    """Create tasks for the monitoring and reporting phase."""
    return [
        Task(
            description="""Design an ESG monitoring system.
                      1. Specify data collection methods for each KPI
                      2. Establish monitoring frequency
                      3. Create a dashboard design for tracking progress""",
            agent=monitoring_agent,
            expected_output="An ESG monitoring system design",
            context=implementation_tasks
        ),
        Task(
            description="""Develop an ESG reporting framework.
                      1. Recommend a reporting standard (GRI, SASB, TCFD, etc.)
                      2. Design the structure and content of ESG reports
                      3. Suggest a reporting schedule""",
            agent=monitoring_agent,
            expected_output="An ESG reporting framework with sample template",
            context=implementation_tasks
        ),
        Task(
            description="""Recommend an assurance and verification approach.
                      1. Suggest appropriate assurance levels for different ESG disclosures
                      2. Identify potential assurance providers
                      3. Outline an assurance process""",
            agent=monitoring_agent,
            expected_output="An ESG assurance and verification approach",
            context=implementation_tasks
        ),
        Task(
            description="""Design a continuous improvement process for ESG.
                      1. Establish a review cycle for the ESG program
                      2. Create a methodology for evaluating effectiveness
                      3. Suggest a process for updating goals and strategies""",
            agent=monitoring_agent,
            expected_output="A continuous improvement process for ESG",
            context=implementation_tasks
        )
    ]
