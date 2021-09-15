# these are different ways to modify the behavior of import statements
# feel free to test these out; make sure to restart the kernel (Kernel -> Restart Kernel) in jupyter before re-importing

### SETUP 1, import everything from each module, apply filter afterwards within __all__ list
### user gets access to everything; doesn't have to remember names of modules; pandas, numpy, seaborn use this
from .preprocess.filter import *
from .preprocess.transform import *
from .analysis.regression import *
#__all__ = ["filter_1", "transform_1"] # list of public objects, as interpreted by "import *"

### SETUP 2
### restrict user access to specific functions
#from .preprocess.filter import filter_1
#from .preprocess.transform import (transform_1, 
#                                    transform_2)

### SETUP 3
### import the modules themselves; 
### forces user to be more clear about what theyre importing
### developer can add a lot more w/out overwhelming the user 
### examples include matplotlib, scikit-learn, scipy
#from .preprocess import filter
#from .preprocess import transform
#from .analysis import regression

### Lastly, if a user insists on using "from datascience import *", constrain what gets imported with __all__ special variable
