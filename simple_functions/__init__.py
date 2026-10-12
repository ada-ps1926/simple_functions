"""A few simple functions, for practising continuous integration."""

from .functions1 import *  # noqa
from .constants import * #noqa --> no quality assurance --> this will be skipped during any flake8 run (it will not say 'unused import')

#not a good practice to use noqa everywhere to make the error go away