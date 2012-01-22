"""On import, sets up SIGUSR1 to print a traceback as INFO for simple_logging"""

import signal, traceback
import simple_logging as logging

def log_traceback(sig, frame):
	tb = traceback.format_stack()
	tb = ''.join(tb)
	logging.info("Recieved SIGUSR1, printing traceback:\n" + tb)

signal.signal(signal.SIGUSR1, log_traceback)