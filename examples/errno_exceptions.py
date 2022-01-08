import os
import errno

a = {i: os.strerror(i) for i in sorted(errno.errorcode)}

for error_code in a.keys():
    print("{:>5}: {}".format(error_code, a[error_code]))
