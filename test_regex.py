import re

import configparser

def extract_config_data(filename):
    # create configparser object
    config = configparser.ConfigParser()
    
    # read the config file
    config.read(filename)
    
    data = []
    
    # loop through each section in the config file
    for section in config.sections():
        # extract the required data from the section
        command = config.get(section, 'command')
        min = config.get(section, 'minimum')
        max = config.get(section, 'numprocs')
        db_group = config.get(section, 'group')
        type = config.get(section, 'type')
        
        # append the data to the list
        data.append([command, min, max, db_group, type])
    
    return data


def extract_params(input_str):
    if input_str.startswith('java'):
        # Define regular expressions for each parameter in the Java command
        logical_db_re = r'-D(\w+)'
        service_re = r'-s\s+([\w:]+)'
        classpath_re = r'-cp\s+([\w/.:*]+)'
        
        # Find all matches for each parameter
        logical_db_match = re.search(logical_db_re, input_str)
        service_matches = re.findall(service_re, input_str)
        classpath_match = re.search(classpath_re, input_str)
        
        # Extract the parameter values from the matches
        logical_db = logical_db_match.group(1) if logical_db_match else ''
        services = [[s.split(':')[0], s.split(':')[1]] for s in service_matches] if service_matches else []
        classpath = classpath_match.group(1) if classpath_match else ''
        server_name = ''
        if classpath:
            jar_files = classpath.split(':')
            for jar_file in jar_files:
                if jar_file.endswith('.jar'):
                    server_name = jar_file.split('/')[-1][:-4]
                    break
        
        # Create a list of lists, one for each service match
        output = []
        for service in services:
            output.append([
                logical_db,
                service[0],
                service[1],
                server_name,
                ''
            ])
    else:
        # Define regular expressions for each parameter in the Tuxedo command
        logical_db_re = r'-D(\w+)'
        service_re = r'-s\s+([\w:]+)'
        server_name_re = r'-Q\s+(\w+)'
        s2_server_name_re = r'\s+(\w+)\s+-Q'
        
        # Find all matches for each parameter
        logical_db_match = re.search(logical_db_re, input_str)
        service_matches = re.findall(service_re, input_str)
        server_name_match = re.search(server_name_re, input_str)
        s2_server_name_match = re.search(s2_server_name_re, input_str)
        
        # Extract the parameter values from the matches
        logical_db = logical_db_match.group(1) if logical_db_match else ''
        services = [[s.split(':')[0], s.split(':')[1]] for s in service_matches] if service_matches else []
        server_name = server_name_match.group(1) if server_name_match else ''
        s2_server_name = s2_server_name_match.group(1) if s2_server_name_match else ''
        
        # Create a list of lists, one for each service match
        for service in services:
            output.append([
                logical_db,
                service[0],
                service[1],
                server_name,
                s2_server_name
            ])
    
    return output
