import sys
import os
from sshutil import connect_to_server as cts


def main():

	credentials = cts.get_credentials(sys.argv[1])
	# print(sys.argv[1])

	command = str(sys.argv[2])

	client = cts.connect_to_client(credentials)

	cts.run_command(client, command)




if __name__ == '__main__':
	main()