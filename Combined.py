import json

def Error():
    PATH_ = '/var/log/nginx/error.log'
    json_ = 'err_log.json'

    with open(PATH_, 'r') as File:
        lines = File.readlines()

# List for dictionaries
    entries = []

    for line in lines:
# Split the entries
        elements = line.split()

        
        datestamp = elements[0]
        timestamp = elements[1]
        log_level = elements[2].strip('[]')
        process_id = elements[3].strip(':')
        error_message = ' '.join(elements[4:])

# Dictionary
        Dict_list = {
            'datestamp': datestamp,
            'timestamp': timestamp,
            'log_level': log_level,
            'process_id': process_id,
            'error_message': error_message
        }

        entries.append(Dict_list)

    with open(json_, 'w') as json_file:
        json.dump(entries, json_file, indent=4)

def Access():
    PATH_ = '/var/log/nginx/access.log'
    json_ = 'acs_log.json'

    with open(PATH_, 'r') as File:
        lines = File.readlines()

# List for dictionaries
    entries = []

    for line in lines:
# Split the line
        elements = line.split()

        remote_address = elements[0]
        timestamp = elements[3].lstrip('[')
        request = elements[5][1:]
        status_code = elements[8]

# Dictionary
        Dict_list = {
            'remote_address': remote_address,
            'timestamp': timestamp,
            'request': request,
            'status_code': status_code,
        }

        entries.append(Dict_list)

    with open(json_, 'w') as json_file:
        json.dump(entries, json_file, indent=1)

def Run():
    choice = input("Select log  (1: Error Log, 2: Access Log, 3: Both): ")

    if choice == "1" or choice == "3":
        Error()
        

    if choice == "2" or choice == "3":
        Access()
        

Run()
