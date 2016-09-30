def emp_with_grown_childrens(arr):
    result = []
    for emp in arr:
        for child in emp['children']:
            if child['age'] > 18:
                result.append(emp['name'])
                break
    return result

ivan = {
    "name" : "ivan",
    "age" : 34,
    "children" : [{
        "name" : "vasja",
        "age" : 17,
    }, {
        "name" : "petja",
        "age" : 10,
    }],
}
darja = {
    "name" : "darja",
    "age" : 41,
    "children" : [{
        "name" : "kirill",
        "age" : 21,
    }, {
        "name" : "pavel",
        "age" : 15,
    }],
}
emps = [ivan, darja]

print(emp_with_grown_childrens(emps))
        
