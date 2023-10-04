my_str = "G()(al)"


# goal_parser = {"()":'o',"(al)":'al'}    
# class Solution:   
#     def interpreter(self,command):
#         return command.replace("()",'o').replace("(al)",'al')
        


# goal_parser = {"()":'o',"(al)":'al',"G":"G"}
# class Solution:
    
#     def interpreter(self,command):
#         temp = ""
#         res = ""
#         for i in range(len(command)):
#             temp += command[i]
#             if temp in goal_parser:
#                 res += goal_parser[temp]
#                 temp = ""
#         return res
            
        


# solution = Solution()
# print(solution.interpreter(my_str))



##practice

goal_parser = {"()":'o',"(al)":'al',"G":"G"}
class Solution:
    
    def interpreter(self,command):
        temp = ""
        res = ""
        for i in command:
            # temp += command[i]
            res += goal_parser.get(i,i)

        return res
            
        

my_str = "G()(al)"
solution = Solution()
print(solution.interpreter(my_str))

