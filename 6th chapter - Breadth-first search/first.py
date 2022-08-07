from collections import deque

print()


#using hash table to connect key to many values 

graph = {}              # create hash table
# add all values of your network to the hash table
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []




searchQueue = deque()               # create a new queue
searchQueue += graph["you"]         # add all "you" values to the queue
searched = []                       # create list keep track of which people you’ve searched before




def PersonIsSeller(name):
    return name[-1] == 'm'      # return true if person name ends with 'm', so he is seller, [-1] return last character in the word



def searchForSeller():
    global searchQueue                  # global keyword is used to access global variables inside a function
    #searchQueue += graph[name]
    global searched

    while searchQueue:
        person = searchQueue.popleft()            # popleft() removes one element from left side and return its value
        if not person in searched:                # only search this person if you have not already searched
            if PersonIsSeller(person):
                return person + " is a mango seller!"
            else:
                searchQueue += graph[person]           # if the person is not a seller, add their neighbors to searchQueue to search
                searched.append(person)                # insert person searched and not mango seller in searched list
                                                       # append inserts a single element in existing list

    return False

print(searchForSeller())



# this contain an error, that if A is neighbor for B and vice versa, this will be an infinite loop in searching process

"""while searchQueue:
    person = searchQueue.popleft()          # popleft() removes one element from left side and return its value

    if PersonIsSeller(person):
        print(person + " is a mango seller")
    else:
        searchQueue += graph[person]            # if the person is not a seller, add their neighbors to searchQueue to search
"""




