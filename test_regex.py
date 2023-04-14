import pandas as pd

def extract_parameters(string):
    # Define a regular expression pattern to match the parameter values
    pattern = r"-Q\s+([^-\s]+)\s+-s\s+([^-\s]+)\s+-s\s+([^-\s]+)\s+-U\s+([^-\s]+)\s+-P\s+([^-\s]+)\s+-D\s+([^-\s]+)"

    # Use re.search to find the first occurrence of the pattern in the string
    match = re.search(pattern, string)

    if match:
        # Extract the values for the -Q, -s, -U, -P, and -D parameters
        q_value = match.group(1)
        s_value_1, s_value_2 = match.group(2).split(':')
        s_value_3, s_value_4 = match.group(3).split(':')
        u_value = match.group(4)
        p_value = match.group(5)
        d_value = match.group(6)

        return {
            "-Q": q_value,
            "-s1": s_value_1,
            "-s2": s_value_2,
            "-s3": s_value_3,
            "-s4": s_value_4,
            "-U": u_value,
            "-P": p_value,
            "-D": d_value,
        }
    else:
        return None

def extract_dataframe(string):
    # Extract the parameters from the string
    params = extract_parameters(string)
    
    if not params:
        print("No match found")
        return None
    
    # Create a pandas DataFrame from the parameters dictionary
    df = pd.DataFrame(params, index=[0])
    
    return df


string = "usrUpdProfileSvr -Q usrUpdProfile1 -s UsrSetProfile:USER_SET_PROFILE -s UsrDelProfile:USER_DELETE_PROFILE - -SUSDTUAT -LY -Utuxuser -Ptuxedo -OBETA -DUsUserProfileDB"
df = extract_dataframe(string)


