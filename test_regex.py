import re

string = "usrUpdProfileSvr -Q usrUpdProfile1 -s UsrSetProfile:USER_SET_PROFILE -s UsrDelProfile:USER_DELETE_PROFILE - -SUSDTUAT -LY -Utuxuser -Ptuxedo -OBETA -DUsUserProfileDB"

# Define a regular expression pattern to match the parameter values
pattern = r"-Q\s+([^-\s]+)\s+-s\s+([^-\s]+)\s+-U\s+([^-\s]+)\s+-P\s+([^-\s]+)\s+-D\s+([^-\s]+)"

# Use re.search to find the first occurrence of the pattern in the string
match = re.search(pattern, string)

if match:
    # Extract the values for the -Q, -s, -U, -P, and -D parameters
    q_value = match.group(1)
    s_value_1, s_value_2 = match.group(2).split(':')
    u_value = match.group(3)
    p_value = match.group(4)
    d_value = match.group(5)

    print(f"-Q value: {q_value}")
    print(f"-s value 1: {s_value_1}")
    print(f"-s value 2: {s_value_2}")
    print(f"-U value: {u_value}")
    print(f"-P value: {p_value}")
    print(f"-D value: {d_value}")
else:
    print("No match found")

