"""Agents for ESG Implementation."""
from typing import Dict, List, Optional
import google.generativeai as genai
from crewai import Agent
from crewai.tools import BaseTool

from .config import ESGConfig
from .llm import GeminiLLM

def create_esg_crew(tools: Dict[str, BaseTool], config: Optional[ESGConfig] = None) -> List[Agent]:
    """Creates and configures agents for ESG implementation."""
    # Use default config if none provided
    config = config or ESGConfig()
    
    # Configure the generation settings
    generation_config = {
        "temperature": config.llm.temperature,
        "top_p": config.llm.top_p,
        "top_k": config.llm.top_k,
        "max_output_tokens": config.llm.max_output_tokens,
    }
    
    # Initialize Gemini Model
    model = genai.GenerativeModel(
        model_name=config.llm.model,  # Use model name from config
        generation_config=genai.GenerationConfig(
            temperature=config.llm.temperature,
            top_p=config.llm.top_p,
            top_k=config.llm.top_k,
            max_output_tokens=config.llm.max_output_tokens
        )
    )
    
    # Create our custom LLM instance
    llm = GeminiLLM(model)
    """Creates and configures agents for ESG implementation."""
    
    # Assessment Agent
    assessment_agent = Agent(
        role="ESG Assessment Specialist",
        goal="Thoroughly assess the organization's current ESG status",
        backstory="""You are an expert in ESG assessment with years of experience 
                    helping organizations understand their ESG baseline. You excel at 
                    stakeholder analysis, materiality assessment, and gap analysis.""",
        verbose=True,
        llm=llm,
        tools=[tools["stakeholder_analysis"], tools["materiality_assessment"]],
        allow_delegation=True
    )

    # Strategy Agent
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

    # Implementation Agent
    implementation_agent = Agent(
        role="ESG Implementation Manager",
        goal="Ensure smooth implementation of ESG initiatives",
        backstory="""You are an experienced project manager specialized in ESG implementation. 
                    You know how to coordinate actions, engage stakeholders, and build 
                    capacity for sustainable change.""",
        verbose=True,
        llm=llm,
        tools=[tools["data_collection"]],
        allow_delegation=True
    )

    # Monitoring Agent
    monitoring_agent = Agent(
        role="ESG Monitoring and Reporting Specialist",
        goal="Track ESG performance and create transparent reports",
        backstory="""You are an expert in ESG metrics, monitoring systems, and 
                    reporting frameworks. You ensure that organizations can 
                    effectively measure, report, and improve their ESG performance.""",
        verbose=True,
        llm=llm,
        tools=[tools["report_generation"], tools["visualization"]],
        allow_delegation=True
    )

    return [
        assessment_agent,
        strategy_agent,
        implementation_agent,
        monitoring_agent
    ]
