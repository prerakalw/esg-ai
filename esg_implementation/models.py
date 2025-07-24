"""Models for ESG Implementation."""
from typing import List, Optional
from pydantic import BaseModel, Field

class ESGVision(BaseModel):
    """Represents the organization's ESG vision and goals."""
    vision_statement: str
    environmental_goals: List[str]
    social_goals: List[str]
    governance_goals: List[str]

class Stakeholder(BaseModel):
    """Represents a stakeholder in the ESG implementation."""
    name: str
    category: str
    influence_level: int
    expectations: List[str]

class MaterialIssue(BaseModel):
    """Represents a material ESG issue."""
    name: str
    description: str
    category: str
    materiality_score: float = 0.0

class ESGMetric(BaseModel):
    """Represents an ESG metric for tracking progress."""
    name: str
    unit: str
    data_source: str
    category: str
    current_value: Optional[float] = None

class Initiative(BaseModel):
    """Represents an ESG initiative."""
    name: str
    description: str
    status: str = "planned"
    timeline: str
    responsible_team: str
    resources_needed: List[str]
    success_criteria: List[str]

class ESGOrganization(BaseModel):
    """Represents an organization's ESG profile."""
    name: str
    vision: Optional[ESGVision] = None
    stakeholders: List[Stakeholder] = Field(default_factory=list)
    material_issues: List[MaterialIssue] = Field(default_factory=list)
    metrics: List[ESGMetric] = Field(default_factory=list)
    initiatives: List[Initiative] = Field(default_factory=list)

    @classmethod
    def load_from_json(cls, filepath: str) -> 'ESGOrganization':
        """Load organization data from JSON file."""
        import json
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls.model_validate(data)
