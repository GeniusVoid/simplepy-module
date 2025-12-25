# simplepy
# A beginner-friendly utility module
# Rule:
# - Functions never crash the program
# - Known errors -> print + return error string
# - Unknown errors -> return -1


from .error_utils import xerror
from .search_utils import xfind
from .count_utils import xcount

__all__ = [
    "xerror",
    "xfind",
    "xcount",
]
