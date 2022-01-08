# ----------------------------------------------------------------------
#  Args.py
#  A program that prints out its own command line arguments
# ----------------------------------------------------------------------
import sys

print()
print('index', '\t', 'value')
for i in range(len(sys.argv)):
    print('  ', i, '\t', sys.argv[i])
# end
print()
