# add the current parent directory to the python path
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# now the module is ready to be imported
import log
