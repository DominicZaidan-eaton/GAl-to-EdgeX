import yaml

with open('yaml-test.yml','r') as file:
    test_d = yaml.safe_load(file)

 # Takes a given dictionary and empty list and iterates through keys until it reaches the bottom of the nested dictionary.
 # It then recursively builds a path from the keys and appends them to list, so that a path is built in order, with the first item being the topmost key
 # Parameters:
 # dic: dictionary to be iterated through
 # path: defaults to an empty list, will contain list of keys to create the path
 # Return: list of keys that make up the desired path
def traversal(dic, path=[]):
    
    if isinstance(dic, dict): # --> Check if dic is a dictionary, if not we have reached the bottom of the nested dictionaries
        for var in dic.keys():
            local_path = path[:] # --> Add all path locations to local_path
            local_path.append(var) # --> Add current key to local_path
            b = traversal(dic[var], local_path) # --> Call function on next key
            return b
    else:
        return path

# Takes a given dictionary and determines if there is a value within that is mapped
# Parameters:
# dic: provided dictionary
# Returns: bool stating if there is a mapped value within the dictionary
def check_mapped(dic):

    flag = False

    key = list(dic)[0]
    val = dic[key]

    if isinstance(val,dict): # --> If the value is a dictionary
        if key == "mag" and "key" in val: # --> If the key is a desired one and its value dictionary contains a desired value
            if val["key"] == "value": # --> If the two correspond
                flag = True
        else:
            flag = check_mapped(val) # --> If the desired key/value pair is not found within the current dictionary, recursively call th function on the nested dictionary

    return flag

# Iterates through a nested dictionary, checking for desired key/value pairings.  Creates a path of keys if one is found
# Parameters:
# curr_dict: the current dictionary being searched
# out_path: defaults to an empty list, contains lists of all paths to desired pairings
# Returns: list of lists containing strings of paths made of keys, 
def create_path(curr_dict, out_path=[]):

    for key, val in curr_dict.items():
        if key == "mag": # --> If the key is the desired one, move to next instance of nested dictionaries
            continue
        elif isinstance(val, dict):
            mapped = check_mapped(val) # --> If there are nested dictionaries that contain mapped values
            if mapped:
                out_path.append(traversal(val,[key])) # --> Iterate through creating a list of all the paths, add to master path list
                continue
            create_path(val, out_path)
        else:
            return
    temp = []
    for p in out_path: # --> For every path found
        s = ""
        for i in p: # --> For every key in every path
            if i != p[-1]: # --> If it is not the last key
                s += i + "."
            else: # --> If it is the last key
                s += i
        temp.append(s)

    return temp


# Function iterates through given yaml file and searches for specific key value pairs.
# outputs list of those pairs and associated paths
#def get_key_val(test_d, path_list=[]):
#
#    map_list = []
#
#    for key, val in test_d.items():
#
#        # if key is of a desired name, add key and value to list of mapped values
#        if key == "mag" and "key" in val:
#            if val["key"] == "value":
#                map_list.append((key, val))
#       
#        # If the value is a dictionary, access it recursively
#       elif isinstance(val, dict):
#            next, path_list = get_key_val(val, path_list)
#
#            # Add to map list
#            for dic in next:
#                map_list.append(dic)
#
#    return map_list, path_list
        
# Initialize empty master path list, call recursive function, print output

tester = create_path(test_d)
print(tester)