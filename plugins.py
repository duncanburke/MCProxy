import sys
from config import *
sys.path.append(PLUGIN_PATH)

# Import plugins here
import log_all, log_sorted, username

# Set ordering here
plugins = [log_all, log_sorted, username]
