"""
original author: Dominik Cedro
created: 2024-03-27
license: BSL 3.0
description: This module contains visalization class for python finance app.
"""

import matplotlib.pyplot as plt
from source.analysis_module.analysis import Analysis
from source.operations_module.financial_operations import Expense, Income

class Visualization:

    def __init__(self, analysis):
        self.analysis = analysis



