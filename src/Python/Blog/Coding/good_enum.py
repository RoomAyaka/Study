from enum import Enum
from pprint import pprint

class Gender(Enum):
    Male = "male"
    Female = "female"

data = {
    "ClassA":{
        "student1": {
            "name": "ito",
            "age": 15,
            "gender": Gender.Male.value
        },
        "student2": {
            "name": "suzuki",
            "age": 14,
            "gender": Gender.Female.value
        },
        "student3": {
            "name": "sakai",
            "age": 18,
            "gender": Gender.Male.value
        }
    }
}

pprint(data)
