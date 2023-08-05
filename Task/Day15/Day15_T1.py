import json
dict = {
        "name" : "Chandresh Patle",
        "course" : "batch 4",
        "subject" : "Python3"
}
print(dict["course"])
json_object = json.dumps(dict)
print("the json format - ", json_object)
