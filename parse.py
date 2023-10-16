import re
import os

# get all the logs from the log directory
# each log was stored as an individual file
files = os.listdir(".\logs")
# iterate through the logs
for i in range(len(files)):
  # concatenate the directory to the logfile
  log_file = ".\logs\\" + files[i]
  # open the logfile and read it into a variable
  with open (log_file, "r") as file:
    log_data = file.read()

  # use the regex split method to find just the port number
  # used if-else statements due to simplicity and time constraints
  if i == 0:
    port_parser = re.split("port ", log_data)
  elif i == 1:
    port_parser = re.split("Port: ", log_data)
  elif i == 2:
    port_parser = re.split("s_port:\"", log_data)

  # the port parser returns a list with two strings since there is only one mention
  # of this specific style of port information
  # so we search the second half of the list, where the port number will be 
  # using the unicode number match ignoring any trailing characters
  port = re.search("\d+", port_parser[1])
  # print the found ports
  print(f"Log {i + 1} has port {port[0]}")