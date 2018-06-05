import sys
import os
from sftputil import copy_file as copy


def main():

    credentials = copy.get_credentials(sys.argv[1])
    sftp = copy.connect_to_client(credentials)

    src = sys.argv[3]
    dest = sys.argv[4]

    if sys.argv[2] == 'put':
        copy.copy_file_to_server(sftp,  src, dest)

    elif sys.argv[2] == 'get':
        copy.get_file_from_server(sftp, src, dest)


if __name__ == '__main__':
    main()