# Dictionary in python
#defining dictionary
people = {
            "1":{
                "name":"abhi",
                "birth":"1999",
                "movie":{"abhi 1", "abhi 2", "abhi 3"}
                },
            "2":{
                "name":"true",
                 "birth":"1999",
                 "movie":"new2"
                 },
            "3":{
                "name":"ataa",
                "birth":"1999",
                "movie":"new3"
                }
        }

source = "1" 
a = people[source]["movie"] #accessing dictonary 
print(a)
print(type(a))

for person_id in people :
    print(people[person_id]["movie"])
    print(type(people[person_id]["movie"]))