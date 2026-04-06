"""
plagiarism-detector - Detect plagiarism and similarity

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import PlagiarismDetector, detect, process, main

__all__ = ["PlagiarismDetector", "detect", "process", "main"]
