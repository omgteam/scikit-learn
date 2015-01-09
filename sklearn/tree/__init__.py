"""
The :mod:`sklearn.tree` module includes decision tree-based models for
classification and regression.
"""

from .tree import DecisionTreeClassifier
from .tree import DecisionTreeRegressor
from .tree import FastDecisionTreeClassifier
from .tree import FastDecisionTreeRegressor
from .tree import ExtraTreeClassifier
from .tree import ExtraTreeRegressor
from .export import export_graphviz

__all__ = ["DecisionTreeClassifier", "DecisionTreeRegressor",
           "FastDecisionTreeClassifier", "FastDecisionTreeRegressor",
           "ExtraTreeClassifier", "ExtraTreeRegressor", "export_graphviz"]
