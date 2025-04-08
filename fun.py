from json_utils import *

def register_stud(stud_name,stud_age,stud_course,stud_address):
    data = read_json()
    print(f"Print  keys in the jsonfile ")
    if len(list(data.keys())) == 0:
        sno = 1
    else:
        sno = int(list(data.keys())[-1])+1
        # print(f"Print  keys in the jsonfile {sno}")

    temp_stud = {
       "name" : stud_name,
       "age" : stud_age,
       "course": stud_course,
       "address": stud_address
    }
    data[sno] = temp_stud
    write_json(data)

def update_stud(sno,sname,sage,scourse,saddress):
    data = read_json()
    if sno in data.keys():
        data[sno]["name"] = sname
        data[sno]["age"] = sage
        data[sno]["course"] = scourse
        data[sno]["address"] = saddress
    write_json(data)

def delete_stud(sno):
    data = read_json()
    if sno in data.keys():
        del data[sno]
    i = 1
    j = len(data.keys())
    data_2 = {}
    for k in data.keys():
        data_2[str(i)] = data[k]
        print(f"data_2[str(i)] {data_2[str(i)]}")
        i+=1
    data = data_2.copy()
    print(data)
    write_json(data)


