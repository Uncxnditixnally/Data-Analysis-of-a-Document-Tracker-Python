import argparse  # https://docs.python.org/2/howto/argparse.html
import sys
from Gui import *
from Task2 import *
from Task3 import *
from Task4 import *
from Task5 import *
from Task6 import *

# Define the arguments for command line usage
parser = argparse.ArgumentParser(
	prog='Doccument Analyser',
	description='',
	epilog = '',
	add_help = True
)
parser.add_argument("-f", "--filename", type=str, help="Name of file to be analysed")
parser.add_argument("-u", "--user_uuid", type=str, help="User id of visitor to search for")
parser.add_argument("-d", "--document_uuid", type=str, help="Document id of the document to search for")
parser.add_argument("-t", "--task_id", type=str, help="ID identifying which task the program should carry out.")

# Read in the arguments
args = parser.parse_args()

# Run the gui if the user passed no arguments
if len(sys.argv) == 1:  # There will always be one argument which is this file's name
	Gui("sample_100k_lines.json")
else:
	if args.filename is None or args.document_uuid is None or args.task_id is None:
		# Don't run if necessary arguments aren't present
		print('Invalid arguments passed. For instruction on usage use the -h argument or to run GUI pass no arguments')
		sys.exit()
	else:
		#c.Controller(args.filename, args.task_id, args.document_uuid, args.user_uuid)
		pass