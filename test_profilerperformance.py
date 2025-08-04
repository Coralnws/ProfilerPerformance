# test_profilerperformance.py
"""
Tests for ProfilerPerformance module.
"""

import unittest
from profilerperformance import ProfilerPerformance

class TestProfilerPerformance(unittest.TestCase):
    """Test cases for ProfilerPerformance class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProfilerPerformance()
        self.assertIsInstance(instance, ProfilerPerformance)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProfilerPerformance()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
