"""
ESG Implementation Package
-------------------------
A multi-agent system for implementing ESG programs using CrewAI.
"""

from .config import ESGConfig
from .models import (
    ESGVision, 
    Stakeholder, 
    MaterialIssue, 
    ESGMetric, 
    Initiative,
    ESGOrganization
)
from .core import ESGWorkflowManager
from .logging import ESGLogger

__version__ = "0.1.0"
__all__ = [
    # Configuration
    'ESGConfig',
    
    # Models
    'ESGVision',
    'Stakeholder',
    'MaterialIssue',
    'ESGMetric',
    'ESGAction',
    'ESGOrganization',
    
    # Core functionality
    'ESGWorkflowManager',
    'ESGLogger'
]
