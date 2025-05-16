"""
Sample Inputs for ESG Implementation Agent
-----------------------------------------
This script provides sample data to test the ESG Implementation Agent
with a fictional company called GreenTech Solutions.
"""

import json

# Sample organization data for GreenTech Solutions
sample_org_data = {
    "name": "GreenTech Solutions",
    "vision": {
        "vision_statement": "To become a carbon-neutral technology company by 2030 while creating positive social impact and maintaining the highest standards of corporate governance.",
        "environmental_goals": [
            "Reduce carbon emissions by 50% by 2025 and 100% by 2030",
            "Achieve zero waste to landfill across all operations by 2027",
            "Transition to 100% renewable energy by 2026",
            "Reduce water consumption by 30% by 2025"
        ],
        "social_goals": [
            "Achieve gender parity across all levels of the organization by 2026",
            "Ensure all employees earn at least a living wage",
            "Implement a comprehensive supplier diversity program",
            "Contribute 1% of profits to community development initiatives"
        ],
        "governance_goals": [
            "Maintain a diverse board with at least 40% representation from underrepresented groups",
            "Implement a robust ESG risk management framework",
            "Ensure 100% compliance with all applicable regulations",
            "Achieve top-quartile ESG ratings from major rating agencies"
        ]
    },
    "stakeholders": [
        {
            "name": "Institutional Investors",
            "category": "Investor",
            "influence_level": 9,
            "expectations": [
                "Transparent ESG disclosure",
                "Climate risk management",
                "Long-term value creation",
                "Alignment with global ESG standards"
            ]
        },
        {
            "name": "Enterprise Customers",
            "category": "Customer",
            "influence_level": 8,
            "expectations": [
                "Sustainable product offerings",
                "Responsible supply chain management",
                "Innovation in green technologies",
                "Ethical business practices"
            ]
        },
        {
            "name": "Employees",
            "category": "Internal",
            "influence_level": 7,
            "expectations": [
                "Diverse and inclusive workplace",
                "Competitive compensation and benefits",
                "Professional development opportunities",
                "Meaningful sustainability initiatives"
            ]
        },
        {
            "name": "Local Communities",
            "category": "Community",
            "influence_level": 6,
            "expectations": [
                "Job creation",
                "Environmental stewardship",
                "Community engagement",
                "Local economic development"
            ]
        },
        {
            "name": "Regulatory Bodies",
            "category": "Regulator",
            "influence_level": 9,
            "expectations": [
                "Compliance with environmental regulations",
                "Transparent reporting",
                "Ethical business conduct",
                "Product safety and quality"
            ]
        },
        {
            "name": "NGOs and Advocacy Groups",
            "category": "Civil Society",
            "influence_level": 5,
            "expectations": [
                "Climate action",
                "Human rights protection",
                "Resource conservation",
                "Corporate accountability"
            ]
        }
    ],
    "material_issues": [
        {
            "name": "Carbon Emissions",
            "category": "Environmental",
            "importance_to_business": 9,
            "importance_to_stakeholders": 10,
            "description": "Direct and indirect greenhouse gas emissions from operations and value chain."
        },
        {
            "name": "Energy Management",
            "category": "Environmental",
            "importance_to_business": 8,
            "importance_to_stakeholders": 7,
            "description": "Energy consumption, efficiency, and transition to renewable sources."
        },
        {
            "name": "Water Management",
            "category": "Environmental",
            "importance_to_business": 6,
            "importance_to_stakeholders": 5,
            "description": "Water usage, efficiency, and impact on water-stressed areas."
        },
        {
            "name": "Waste and Hazardous Materials",
            "category": "Environmental",
            "importance_to_business": 7,
            "importance_to_stakeholders": 6,
            "description": "Generation, management, and disposal of waste and hazardous materials."
        },
        {
            "name": "Diversity and Inclusion",
            "category": "Social",
            "importance_to_business": 8,
            "importance_to_stakeholders": 9,
            "description": "Workforce diversity, equity, and inclusion across all levels."
        },
        {
            "name": "Labor Practices",
            "category": "Social",
            "importance_to_business": 7,
            "importance_to_stakeholders": 8,
            "description": "Fair compensation, benefits, working conditions, and labor rights."
        },
        {
            "name": "Community Relations",
            "category": "Social",
            "importance_to_business": 6,
            "importance_to_stakeholders": 7,
            "description": "Engagement with and impact on local communities."
        },
        {
            "name": "Product Quality and Safety",
            "category": "Social",
            "importance_to_business": 9,
            "importance_to_stakeholders": 9,
            "description": "Ensuring products meet quality standards and are safe for customers."
        },
        {
            "name": "Data Privacy and Security",
            "category": "Governance",
            "importance_to_business": 10,
            "importance_to_stakeholders": 10,
            "description": "Protection of customer data and information security practices."
        },
        {
            "name": "Business Ethics",
            "category": "Governance",
            "importance_to_business": 9,
            "importance_to_stakeholders": 9,
            "description": "Anti-corruption, anti-bribery, and ethical business conduct."
        },
        {
            "name": "Board Diversity and Structure",
            "category": "Governance",
            "importance_to_business": 7,
            "importance_to_stakeholders": 8,
            "description": "Diversity, independence, and expertise of the board of directors."
        },
        {
            "name": "ESG Governance",
            "category": "Governance",
            "importance_to_business": 8,
            "importance_to_stakeholders": 7,
            "description": "Oversight and management of ESG issues at the board and executive levels."
        }
    ],
    "metrics": [
        {
            "name": "Scope 1 GHG Emissions",
            "category": "Environmental",
            "unit": "tCO2e",
            "current_value": 15000,
            "target_value": 7500,
            "data_source": "Energy consumption records"
        },
        {
            "name": "Scope 2 GHG Emissions",
            "category": "Environmental",
            "unit": "tCO2e",
            "current_value": 22000,
            "target_value": 11000,
            "data_source": "Utility bills and energy supplier data"
        },
        {
            "name": "Renewable Energy Percentage",
            "category": "Environmental",
            "unit": "%",
            "current_value": 35,
            "target_value": 100,
            "data_source": "Energy procurement contracts"
        },
        {
            "name": "Water Consumption",
            "category": "Environmental",
            "unit": "cubic meters",
            "current_value": 45000,
            "target_value": 31500,
            "data_source": "Water utility bills"
        },
        {
            "name": "Waste Diversion Rate",
            "category": "Environmental",
            "unit": "%",
            "current_value": 65,
            "target_value": 100,
            "data_source": "Waste management records"
        },
        {
            "name": "Gender Diversity - Management",
            "category": "Social",
            "unit": "% women",
            "current_value": 32,
            "target_value": 50,
            "data_source": "HR records"
        },
        {
            "name": "Gender Diversity - Board",
            "category": "Social",
            "unit": "% women",
            "current_value": 30,
            "target_value": 50,
            "data_source": "Board records"
        },
        {
            "name": "Employee Satisfaction",
            "category": "Social",
            "unit": "score out of 5",
            "current_value": 3.8,
            "target_value": 4.5,
            "data_source": "Annual employee survey"
        },
        {
            "name": "Community Investment",
            "category": "Social",
            "unit": "% of profit",
            "current_value": 0.5,
            "target_value": 1.0,
            "data_source": "Financial records"
        },
        {
            "name": "Supplier Diversity",
            "category": "Social",
            "unit": "% diverse suppliers",
            "current_value": 15,
            "target_value": 30,
            "data_source": "Procurement records"
        },
        {
            "name": "Board Independence",
            "category": "Governance",
            "unit": "% independent directors",
            "current_value": 75,
            "target_value": 80,
            "data_source": "Board records"
        },
        {
            "name": "Ethics Training Completion",
            "category": "Governance",
            "unit": "% employees trained",
            "current_value": 90,
            "target_value": 100,
            "data_source": "Training records"
        },
        {
            "name": "Data Breaches",
            "category": "Governance",
            "unit": "number per year",
            "current_value": 1,
            "target_value": 0,
            "data_source": "Security incident reports"
        },
        {
            "name": "ESG Disclosure Score",
            "category": "Governance",
            "unit": "score out of 100",
            "current_value": 68,
            "target_value": 90,
            "data_source": "ESG rating agency reports"
        }
    ],
    "actions": [
        {
            "name": "Carbon Reduction Program",
            "description": "Implement energy efficiency measures and transition to renewable energy across all facilities.",
            "responsible_party": "Sustainability Team",
            "timeline": "2023-2026",
            "resources_required": "$2.5M budget, dedicated project manager, external consultants",
            "status": "In Progress",
            "related_metrics": ["Scope 1 GHG Emissions", "Scope 2 GHG Emissions", "Renewable Energy Percentage"]
        },
        {
            "name": "Zero Waste Initiative",
            "description": "Implement waste reduction, recycling, and composting programs to eliminate waste to landfill.",
            "responsible_party": "Facilities Management",
            "timeline": "2023-2027",
            "resources_required": "$800K budget, waste management consultant, employee training",
            "status": "Planning Phase",
            "related_metrics": ["Waste Diversion Rate"]
        },
        {
            "name": "Water Conservation Project",
            "description": "Install water-efficient fixtures, implement water recycling, and optimize cooling systems.",
            "responsible_party": "Engineering Team",
            "timeline": "2023-2025",
            "resources_required": "$600K budget, engineering staff time",
            "status": "In Progress",
            "related_metrics": ["Water Consumption"]
        },
        {
            "name": "Diversity and Inclusion Program",
            "description": "Comprehensive D&I strategy including recruitment, retention, and advancement initiatives.",
            "responsible_party": "HR Department",
            "timeline": "2023-2026",
            "resources_required": "$1.2M budget, D&I specialist, training resources",
            "status": "In Progress",
            "related_metrics": ["Gender Diversity - Management", "Gender Diversity - Board", "Employee Satisfaction"]
        },
        {
            "name": "Community Impact Initiative",
            "description": "Structured program for community investments, volunteering, and local partnerships.",
            "responsible_party": "Corporate Affairs",
            "timeline": "2023-2025",
            "resources_required": "$500K budget, volunteer coordinator, NGO partnerships",
            "status": "In Progress",
            "related_metrics": ["Community Investment"]
        },
        {
            "name": "Supplier Diversity Enhancement",
            "description": "Expand supplier diversity program with new targets, training, and supplier development.",
            "responsible_party": "Procurement Department",
            "timeline": "2023-2024",
            "resources_required": "$350K budget, procurement staff time",
            "status": "Planning Phase",
            "related_metrics": ["Supplier Diversity"]
        },
        {
            "name": "Enhanced ESG Governance Structure",
            "description": "Establish board ESG committee, executive ESG council, and formal ESG reporting process.",
            "responsible_party": "Corporate Secretary",
            "timeline": "2023",
            "resources_required": "Board and executive time, governance consultant",
            "status": "Completed",
            "related_metrics": ["ESG Disclosure Score", "Board Independence"]
        },
        {
            "name": "Cybersecurity Enhancement Program",
            "description": "Strengthen data protection through improved systems, processes, and employee training.",
            "responsible_party": "IT Security Team",
            "timeline": "2023-2024",
            "resources_required": "$1.5M budget, security consultants, training materials",
            "status": "In Progress",
            "related_metrics": ["Data Breaches", "Ethics Training Completion"]
        }
    ],
    "reports": []
}

# Save the sample data to a JSON file
def save_sample_data():
    """Save the sample data to a JSON file."""
    filename = "examples/greentech_solutions_esg_data.json"
    with open(filename, 'w') as f:
        json.dump(sample_org_data, f, indent=2)
    print(f"Sample data saved to {filename}")
    return filename

# Additional sample data for different phases of implementation

# Sample data for initial assessment phase (less complete)
def create_assessment_phase_sample():
    """Create a sample organization in the assessment phase."""
    initial_data = {
        "name": "Eco Manufacturing Inc.",
        "vision": None,  # Not defined yet
        "stakeholders": [
            {
                "name": "Investors",
                "category": "Investor",
                "influence_level": 8,
                "expectations": ["ESG performance", "Risk management"]
            },
            {
                "name": "Customers",
                "category": "Customer",
                "influence_level": 7,
                "expectations": ["Sustainable products", "Ethical practices"]
            }
        ],
        "material_issues": [],  # Not identified yet
        "metrics": [],  # Not defined yet
        "actions": [],  # Not defined yet
        "reports": []
    }
    filename = "examples/eco_manufacturing_esg_data.json"
    with open(filename, 'w') as f:
        json.dump(initial_data, f, indent=2)
    print(f"Assessment phase sample saved to {filename}")
    return filename

# Sample data for strategy development phase
def create_strategy_phase_sample():
    """Create a sample organization in the strategy development phase."""
    strategy_data = {
        "name": "TechInnovate",
        "vision": {
            "vision_statement": "To lead technology innovation with environmental and social responsibility.",
            "environmental_goals": ["Carbon neutral by 2030", "Zero waste operations"],
            "social_goals": ["Diverse workforce", "Ethical supply chain"],
            "governance_goals": ["Transparent reporting", "Ethical leadership"]
        },
        "stakeholders": [
            {
                "name": "Shareholders",
                "category": "Investor",
                "influence_level": 9,
                "expectations": ["Long-term growth", "ESG risk management", "Transparent disclosure"]
            },
            {
                "name": "B2B Customers",
                "category": "Customer",
                "influence_level": 8,
                "expectations": ["Innovative solutions", "Sustainable products", "Ethical practices"]
            },
            {
                "name": "Employees",
                "category": "Internal",
                "influence_level": 7,
                "expectations": ["Inclusive culture", "Competitive compensation", "Career growth"]
            },
            {
                "name": "Regulators",
                "category": "Regulator",
                "influence_level": 8,
                "expectations": ["Compliance", "Responsible AI", "Data protection"]
            }
        ],
        "material_issues": [
            {
                "name": "Climate Impact",
                "category": "Environmental",
                "importance_to_business": 8,
                "importance_to_stakeholders": 9,
                "description": "Carbon footprint of operations and products."
            },
            {
                "name": "Talent Diversity",
                "category": "Social",
                "importance_to_business": 7,
                "importance_to_stakeholders": 8,
                "description": "Diversity in workforce and leadership."
            },
            {
                "name": "Data Security",
                "category": "Governance",
                "importance_to_business": 9,
                "importance_to_stakeholders": 9,
                "description": "Protection of sensitive customer and business data."
            }
        ],
        "metrics": [
            {
                "name": "Carbon Footprint",
                "category": "Environmental",
                "unit": "tCO2e",
                "current_value": 12000,
                "target_value": 0,
                "data_source": "Energy consumption data"
            },
            {
                "name": "Gender Diversity",
                "category": "Social",
                "unit": "% women in leadership",
                "current_value": 28,
                "target_value": 50,
                "data_source": "HR records"
            }
        ],
        "actions": [],  # Not defined yet
        "reports": []
    }
    filename = "examples/techinnovate_esg_data.json"
    with open(filename, 'w') as f:
        json.dump(strategy_data, f, indent=2)
    print(f"Strategy phase sample saved to {filename}")
    return filename

# Sample responses for agent tasks
sample_agent_responses = {
    "scope_task": """
# ESG Scope and Objectives for GreenTech Solutions

## ESG Vision Statement
To become a carbon-neutral technology company by 2030 while creating positive social impact and maintaining the highest standards of corporate governance.

## Environmental Goals
1. Reduce carbon emissions by 50% by 2025 and 100% by 2030
2. Achieve zero waste to landfill across all operations by 2027
3. Transition to 100% renewable energy by 2026
4. Reduce water consumption by 30% by 2025

## Social Goals
1. Achieve gender parity across all levels of the organization by 2026
2. Ensure all employees earn at least a living wage
3. Implement a comprehensive supplier diversity program
4. Contribute 1% of profits to community development initiatives

## Governance Goals
1. Maintain a diverse board with at least 40% representation from underrepresented groups
2. Implement a robust ESG risk management framework
3. Ensure 100% compliance with all applicable regulations
4. Achieve top-quartile ESG ratings from major rating agencies

## Assessment Scope
The ESG assessment will cover:
- All direct operations (offices, data centers, manufacturing facilities)
- Scope 1, 2, and 3 emissions (with initial focus on largest Scope 3 categories)
- Tier 1 suppliers (with a roadmap to expand to additional tiers)
- Key social metrics across all employee groups and locations
- All governance structures and policies
    """,

    "stakeholder_task": """
Stakeholder Analysis Results:
1. Regulatory Bodies (Regulator) - Influence: 9/10
   Key expectations: Compliance with environmental regulations, Transparent reporting, Ethical business conduct, Product safety and quality

2. Institutional Investors (Investor) - Influence: 9/10
   Key expectations: Transparent ESG disclosure, Climate risk management, Long-term value creation, Alignment with global ESG standards

3. Enterprise Customers (Customer) - Influence: 8/10
   Key expectations: Sustainable product offerings, Responsible supply chain management, Innovation in green technologies, Ethical business practices

4. Employees (Internal) - Influence: 7/10
   Key expectations: Diverse and inclusive workplace, Competitive compensation and benefits, Professional development opportunities, Meaningful sustainability initiatives

5. Local Communities (Community) - Influence: 6/10
   Key expectations: Job creation, Environmental stewardship, Community engagement, Local economic development

6. NGOs and Advocacy Groups (Civil Society) - Influence: 5/10
   Key expectations: Climate action, Human rights protection, Resource conservation, Corporate accountability
    """,

    "materiality_task": """
Materiality Assessment Results:
1. Data Privacy and Security (Governance) - Materiality Score: 10.0/10
   Description: Protection of customer data and information security practices.

2. Carbon Emissions (Environmental) - Materiality Score: 9.5/10
   Description: Direct and indirect greenhouse gas emissions from operations and value chain.

3. Product Quality and Safety (Social) - Materiality Score: 9.0/10
   Description: Ensuring products meet quality standards and are safe for customers.

4. Business Ethics (Governance) - Materiality Score: 9.0/10
   Description: Anti-corruption, anti-bribery, and ethical business conduct.

5. Diversity and Inclusion (Social) - Materiality Score: 8.5/10
   Description: Workforce diversity, equity, and inclusion across all levels.

6. Energy Management (Environmental) - Materiality Score: 7.5/10
   Description: Energy consumption, efficiency, and transition to renewable sources.

7. Labor Practices (Social) - Materiality Score: 7.5/10
   Description: Fair compensation, benefits, working conditions, and labor rights.

8. ESG Governance (Governance) - Materiality Score: 7.5/10
   Description: Oversight and management of ESG issues at the board and executive levels.

9. Board Diversity and Structure (Governance) - Materiality Score: 7.5/10
   Description: Diversity, independence, and expertise of the board of directors.

10. Waste and Hazardous Materials (Environmental) - Materiality Score: 6.5/10
    Description: Generation, management, and disposal of waste and hazardous materials.

11. Community Relations (Social) - Materiality Score: 6.5/10
    Description: Engagement with and impact on local communities.

12. Water Management (Environmental) - Materiality Score: 5.5/10
    Description: Water usage, efficiency, and impact on water-stressed areas.
    """
}

# Function to demonstrate using the sample data with the ESG agent
def demonstrate_esg_agent_usage():
    """Provide code example for using the sample data with the ESG agent."""
    usage_example = """
# Example usage of the ESG Implementation Agent with sample data

from esg_implementation_agent import run_esg_implementation, ESGOrganization

# Option 1: Use with a new organization
result = run_esg_implementation("GreenTech Solutions")

# Option 2: Load existing data from sample file
organization = ESGOrganization.load_from_json("greentech_solutions_esg_data.json")

# You can also inspect specific aspects of the ESG implementation
print(f"Organization: {organization.name}")
print(f"Vision statement: {organization.vision.vision_statement if organization.vision else 'Not defined'}")
print(f"Number of stakeholders: {len(organization.stakeholders)}")
print(f"Number of material issues: {len(organization.material_issues)}")
print(f"Number of metrics: {len(organization.metrics)}")
print(f"Number of actions: {len(organization.actions)}")
    """
    print("\nExample usage of the ESG Implementation Agent with sample data:")
    print(usage_example)

# Main function to create all sample data
def create_all_samples():
    """Create all sample data files for testing the ESG agent."""
    save_sample_data()
    create_assessment_phase_sample()
    create_strategy_phase_sample()
    demonstrate_esg_agent_usage()

if __name__ == "__main__":
    create_all_samples()