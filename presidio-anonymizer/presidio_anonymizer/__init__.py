"""Anonymizer root module."""
import logging

from .anonymizer_engine import AnonymizerEngine
from .decrypt_engine import DecryptEngine

# Set up default logging (with NullHandler)


logging.getLogger("presidio-anonymizer").addHandler(logging.NullHandler())

__all__ = ["AnonymizerEngine", "DecryptEngine"]
