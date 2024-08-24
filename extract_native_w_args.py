import requests
import json

output_file_name = "table_natives.json"

api_link = "https://runtime.fivem.net/doc/natives_cfx.json"

table_result = {}

def convert_to_camel_case(line):
    words = line.split('_')
    camel_case = ''.join(word.capitalize() for word in words)
    return camel_case

def fetchv2(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"A problem occurred while fetching the data. Status code: {response.status_code}")
        return

    data = json.loads(response.text)

    cfx_data = data

    result = []
    type_different = []
    for type_native in cfx_data.keys():
        for native, native_data in cfx_data[type_native].items():
            if native_data["apiset"] == "server":
                native_name = convert_to_camel_case(native_data["name"])
                native_hash = native
                native_params = native_data["params"]
                for param in native_params:
                    if "description" in param:
                        del param["description"]
                for param in native_params:
                    if param["type"] not in type_different:
                        type_different.append(param["type"])

                table_result[native_name] = native_params
                table_result[native_hash] = native_params

    with open(output_file_name, "w") as file:
        file.write(json.dumps(table_result))
    
    print(type_different)
    



fetchv2(api_link)