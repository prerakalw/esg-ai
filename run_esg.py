"""
ESG Implementation Runner
------------------------
Main script to run the ESG implementation process.
"""

import logging
from esg_implementation import ESGConfig, ESGWorkflowManager, ESGLogger

def main():
    # Load configuration (will look for esg_config.yaml or use environment variables)
    config = ESGConfig.load()

    # Create workflow manager (this will set up logging automatically)
    manager = ESGWorkflowManager(config)
    log = logging.getLogger("ESGImplementation")

    try:
        log.info("Starting ESG implementation process")
        
        # Get organization name from config or use default
        organization_name = config.organization.name if hasattr(config, 'organization') else "TechInnovate"
        log.info(f"Running implementation for organization: {organization_name}")
        
        result = manager.run_implementation(organization_name)

        log.info("ESG Implementation completed successfully")
        print("\nESG Implementation Summary:")
        print(result)
        print("\nSustainability is everyone's responsibility!")
        
    except Exception as e:
        log.error(f"ESG Implementation failed: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
