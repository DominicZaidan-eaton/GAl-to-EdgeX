import yaml

with open('yaml-test.yml','r') as file:
    test_d = yaml.safe_load(file)

# Function iterates through given dictionary and creates path while
# Searching for specific key
# Returns the path in list format or None
def create_path(curr_dict, out_path):
    
    for key, val in curr_dict.items():
        if key == "final_time" or key == "key":
            return curr_dict, out_path
        elif isinstance(val, dict):
            out_path.append(key)
            create_path(val, out_path)
        
        return curr_dict, out_path



# Function iterates through given yaml file and searches for specific key value pairs.
# outputs list of those pairs and associated paths
# add another param that contains list of desired keys, replace if with if val is mapped
def get_key_val(test_d, path_list):

    map_list = []

    for key, val in test_d.items():

        # if key is of a desired name, add key and value to list of mapped values
        if key == "final_time" or key == "key":
            map_list.append((key, val))
       
        # If the value is a dictionary, access it recursively
        elif isinstance(val, dict):
            next, path_list = get_key_val(val, path_list)

            # Add to map list
            for dic in next:
                map_list.append(dic)

    return map_list, path_list
        
# Initialize empty master path list, call recursive function, print output
path_list = []
dit, path = get_key_val(test_d, path_list)
print(dit)
print(path)