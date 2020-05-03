"""
Module for storage enum classes
"""

from enum import Enum


class ItemOption(str, Enum):
    """
    This class represents all options available
    """
    office = 'office'
    home = 'home'
    travel = 'travel'
