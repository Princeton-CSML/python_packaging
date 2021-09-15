# SETUP 1, import everything from each module, apply filter afterwards within __all__ list
# user gets access to everything; doesn't have to remember names of modules; pandas, numpy, seaborn use this
#from .filter import *
#from .transform import *
#__all__ = ["filter_1", "transform_1"]

# SETUP 2, accomplishes same as above, just restricts which functions users can access in a diff way
#from .filter import filter_1
#from .transform import transform_1

# SETUP 3
#import .preprocess.filter
#import .preprocess.transform


