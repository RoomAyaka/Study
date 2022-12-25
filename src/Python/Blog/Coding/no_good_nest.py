data = {
    "ClassA":{
        "student1": {
            "name": "ito",
            "age": 15,
            "gender": "male"
        },
        "student2": {
            "name": "suzuki",
            "age": 14,
            "gender": "female"
        },
        "student3": {
            "name": "sakai",
            "age": 18,
            "gender": "male"
        }
    },
    "ClassB": {
        "student4": {
            "name": "yamada",
            "age": 19,
            "gender": "male"
        },
        "student5": {
            "name": "maeda",
            "age": 12,
            "gender": "female"
        }
    }
}


# ネストが深く少し読みにくですね
student_list = []
for key, student_info in data.items():
    if key == "ClassA":
        for id, personal_info in student_info.items():
            if personal_info["age"] >= 15:
                student_list.append(personal_info["name"])

print(student_list)

----- 出力結果 -----
['ito', 'sakai']

# ネストが1つ浅くなって少し読みやすくなりました。
student_list = []
for key, student_info in data.items():
    if not key == "ClassA":
        continue
    # 上記のif文のおかげで下記のfor文には"ClassA"のみ情報しか来ない
    for id, personal_info in student_info.items():
        if personal_info["age"] >= 15:
            student_list.append(personal_info["name"])

print(student_list)

----- 出力結果 -----
['ito', 'sakai']
