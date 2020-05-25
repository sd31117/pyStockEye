#(c) 2020 The Keker LLC
# Spencer Dyvig, Max Shriver
import json
import requests
import re


def callApi():
    with open('api.txt', 'r') as api:
        api = api.read()
    response = requests.get(api)

    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return 1


apicall = callApi()
print(apicall['userId'])

print ("Please select an option. [sview], [dview], [vlist], [alist], ['rlist']")

option = input("Enter your choice: ")

if option == "sview":
    # code
    sview_parm = input("Please enter 'sview all' or 'STOCK SYMBOL'")

elif option == "dview":
    # code
    dview_parm = input("Please enter 'dview all' or 'STOCK SYMBOL'")

elif option == "vlist":
    # code
    stock_list_file = open("list.txt", "r")
    view_list = stock_list_file.read().split(',')

    print(' '.join(map(str, view_list)))

elif option == "alist":
    # code
    alist_parm = input("Please enter 'STOCK SYMBOL' to add a stock")

    list_text = open('list.txt', 'a')

    list_text.write(alist_parm+",")

    list_text.close()


elif option == "rlist":
    # code
    rlist_parm = input("Please enter 'STOCK SYMBOL' to remove a stock")

    f = open('list.txt','r')
    a = [rlist_parm+',']
    lst = []
    for line in f:
        for word in a:
            if word in line:
                line = line.replace(word,'')
                lst.append(line)
    f.close()
    f = open('list.txt','w')
    for line in lst:
        f.write(line)
    f.close()
