from collections import Counter, defaultdict, deque
class Solution:
    def alienOrder(self, words: list[str]) -> str:

        # initialize indegree counter -> dictionary style of key: count
        indegrees = Counter({c: 0 for word in words for c in word})
        # print("indegrees currently: ", indegrees)
        # initialize graph style -> (node, {children set)
        graph = defaultdict(set)

        # step 1 -> populate our graph and the indegree count
        for word1, word2 in zip(words, words[1:]):
            for letter1, letter2 in zip(word1, word2):
                # difference + not already a child
                print("before if statement: ", letter1, letter2)
                if letter1 != letter2:
                    if letter2 not in graph[letter1]:
                        print("letter1 is ", letter1, "letter2 is: ", letter2)
                        graph[letter1].add(letter2)
                        indegrees[letter2] += 1
                    # print("current indegree: ", letter2, "is: ", indegrees[letter2])
                    break
            # if it goes through either of the full words -> make sure word2 is not smaller than word1
            else: # if the for loop finishes without breaking
                if len(word2) < len(word1):
                    print(" short error ")
                    return ""
        print("passed step 1")

        # step 2 
        result = ""
        # append all elements with indegree of 0 into double edged queue
        queue = deque([edge for edge in indegrees if indegrees[edge] == 0])
        while queue: # while there are still elements with indegree of 0
            edge = queue.popleft()
            result += edge
            for child in graph[edge]:
                indegrees[child] -= 1 # reduce indegrees by 1
                if indegrees[child] == 0:
                    # add to queue
                    queue.append(child)
                elif indegrees[child] < 0: # if it goes into negatives
                    print("went into negatives")
                    return ""
        if len(indegrees) != len(result):
            print(len(indegrees), len(result))
            print("result: ", result)
            print("not same length")
            return ""
        return result


object = Solution()
print(object.alienOrder(["wrt","wrf","er","ett","rftt","te"]))
# print(object.alienOrder(["wrt","wrf","er","ett","rftt"]))
            


                        

        