"""
Question 1:
Write a function which takes a list of pin and board id pairs (ex: (1, 11) - 1 is a pin and 11 is a board). Return all the pins which are relevant to each other. A pin is relevant to another pin if they have a matching board.
Input: [(1, 11), (1, 14), (2, 12), (3, 15), (3, 16), (4, 11), (4, 16), (5, 12), (5, 16), (6, 14)]
Output: {1: [4, 6], 2: [5], 3: [5], 4: [1, 5], 5: [2, 3, 4], 6: [1]}
Note that the relevance property is NOT transitive, as we see 1 is relevant to 4 and 4 is relevant to 5, but 1 and 5 are not relevant to each other
"""
# are there ever duplicate pairs?
# is the input ever empty

def cabbageq1(input: list[tuple[int, int]]) -> dict:
    """ takes in a list of tuple pairs and outputs a dictionary pair """
    # part 1 -> output all boards a certain pin is related to
    relations = {}
    for pair in input:
        if pair[1] not in relations:
            relations[pair[1]] = [pair[0]]
        else:
            relations[pair[1]].append(pair[0])
    # part 2 -> combine pairs
    answer = {}
    for pins in relations.values():
        for index in range(len(pins)):
            if pins[index] not in answer: # if it is not in answer
                answer[pins[index]] = pins[:index]
                if index+1 < len(pins):
                    answer[pins[index]].extend(pins[index+1:])        
            else: # if its already in the answer
                answer[pins[index]].extend(pins[:index])
                if index+1 < len(pins):
                    answer[pins[index]].extend(pins[index+1:])
    return answer

print(cabbageq1([(1, 11), (1, 14), (2, 12), (3, 15), (3, 16), (4, 11), (4, 16), (5, 12), (5, 16), (6, 14)]))
    


