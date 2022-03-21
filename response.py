import json
import re
import sys

from types import SimpleNamespace

# Parse JSON into an object with attributes corresponding to dict keys.


class SimpleNamespace:
    '''
            Redefining SimpleNamespace to add toJSON method
    '''
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


def lambda_function(d):
    '''
            Replace '-' by '_' from all keys
    '''
    d2 = {k.replace(u'-', '_') : v for k, v in d.items()}    
    return SimpleNamespace(**d2)



def main():
    '''
            Main function
    '''
    if (len(sys.argv) != 3):
        print("Usage : " + sys.argv[0] + "CONFIG_ FILE MOFIS_FILE")
        return

    file_path = sys.argv[1]
    modif_path = sys.argv[2]

    with open(file_path) as f:
        data_result = json.loads(f.read(), object_hook=lambda d: lambda_function(d))

    with open(modif_path) as f:

        for line in f:
            command = re.sub(r"\"\s*:\s*", " = ", line, count=1)
            command = re.sub(r"^\"", "", command)

            command = "data_result." + command.replace(u'-', '_')

            command = re.sub(r"=\s*{", "= '{", command, count=1)
            command = re.sub(r"}\s*$", "}'", command)

            try:
                exec(command)
            except (AttributeError):
                print ("JSON doesn't have correct attribute : " + command, file=sys.stderr)
            except (SyntaxError):
                print ("Error Input changes : " + command, file=sys.stderr) 

    print(data_result.toJSON())

if __name__ == "__main__": 
    main()
