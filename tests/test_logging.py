"""
Test ESG implementation logging functionality
"""

import os
import pytest
import logging
import tempfile
from pathlib import Path
from datetime import datetime
from esg_implementation import ESGLogger, ESGConfig

def test_esg_logger_file_creation():
    """Test that ESGLogger creates a log file with the correct name format"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test config
        config = ESGConfig(
            output_path=temp_dir,
            logging={"level": "INFO"}
        )
        
        # Initialize logger
        logger = ESGLogger(config)
        log = logging.getLogger("ESGImplementation")
        
        # Log some test messages
        log.info("Test info message")
        log.warning("Test warning message")
        log.error("Test error message")
        
        # Check log file exists and has correct format
        log_files = list(Path(temp_dir).glob("esg_implementation_*.log"))
        assert len(log_files) == 1, "Expected exactly one log file"
        
        log_file = log_files[0]
        assert log_file.exists(), "Log file should exist"
        
        # Check file name format
        name_pattern = "esg_implementation_" + datetime.now().strftime("%Y%m%d")
        assert name_pattern in log_file.name, "Log file should have correct date format"
        
        # Verify log content
        with open(log_file, "r") as f:
            content = f.read()
            assert "Test info message" in content
            assert "Test warning message" in content
            assert "Test error message" in content

def test_esg_logger_console_output():
    """Test that ESGLogger outputs to both console and file"""
    with tempfile.TemporaryDirectory() as temp_dir:
        config = ESGConfig(
            output_path=temp_dir,
            logging={"level": "INFO"}
        )
        
        # Initialize logger
        logger = ESGLogger(config)
        log = logging.getLogger("ESGImplementation")
        
        # Capture console output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            log.info("Console test message")
            console_output = captured_output.getvalue()
            assert "Console test message" in console_output
            
            # Check file output
            log_file = next(Path(temp_dir).glob("esg_implementation_*.log"))
            with open(log_file, "r") as f:
                file_content = f.read()
                assert "Console test message" in file_content
                
        finally:
            sys.stdout = sys.__stdout__

def test_esg_logger_levels():
    """Test that ESGLogger respects log levels"""
    with tempfile.TemporaryDirectory() as temp_dir:
        config = ESGConfig(
            output_path=temp_dir,
            logging={"level": "WARNING"}  # Set to WARNING level
        )
        
        logger = ESGLogger(config)
        log = logging.getLogger("ESGImplementation")
        
        # Log messages at different levels
        log.debug("Debug message")
        log.info("Info message")
        log.warning("Warning message")
        log.error("Error message")
        
        # Check log file content
        log_file = next(Path(temp_dir).glob("esg_implementation_*.log"))
        with open(log_file, "r") as f:
            content = f.read()
            assert "Debug message" not in content
            assert "Info message" not in content
            assert "Warning message" in content
            assert "Error message" in content
