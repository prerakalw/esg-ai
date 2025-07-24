"""Logging utilities for ESG Implementation."""
import sys
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, TextIO
from .config import ESGConfig

class TeeLogger:
    """Logger that writes to both file and console."""
    
    def __init__(self, filename: Path):
        self.console = sys.stdout
        self.file = open(filename, 'a', encoding='utf-8')
        
    def write(self, message):
        self.console.write(message)
        self.file.write(message)
        self.file.flush()
        
    def flush(self):
        self.console.flush()
        self.file.flush()

class ESGLogger:
    """Manages logging for ESG implementation."""
    
    def __init__(self, config: ESGConfig):
        """Initialize logger with configuration."""
        self.config = config
        self.log_file: Optional[Path] = None
        self.output_file: Optional[TextIO] = None
        self.original_stdout = sys.stdout
        self._setup_logging()
    
    def _setup_logging(self):
        """Set up logging configuration."""
        # Create output directory
        output_dir = Path(self.config.output_path)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Create timestamped log file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = output_dir / f"esg_implementation_{timestamp}.log"
        
        # Configure logging
        logging.basicConfig(
            level=getattr(logging, self.config.logging.level),
            format=self.config.logging.format,
            datefmt=self.config.logging.date_format,
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        # Set up console output capture
        sys.stdout = TeeLogger(self.log_file)
    
    def get_logger(self, name: str) -> logging.Logger:
        """Get a logger instance."""
        return logging.getLogger(name)
    
    def cleanup(self):
        """Clean up logging resources."""
        if hasattr(sys.stdout, 'file'):
            sys.stdout.file.close()
        sys.stdout = self.original_stdout
