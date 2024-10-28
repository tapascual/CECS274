import numpy as np
import ArrayStack
# import BinaryTree
import ChainedHashTable
import DLList
import operator
import re

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable()

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)
        
    def matched_expression(self, s : str) -> bool :

        stack = ArrayStack.ArrayStack()
        for i in s:
            if i =='(' :
                stack.push('(')
            elif i == ')':
                try: 
                    stack.pop()  
                except IndexError: 
                    return False
        size = stack.size()
        if size == 0:
            return True
        else:
            return False


    def build_parse_tree(self, exp : str) ->str:
        # todo
        pass 

    def _evaluate(self, root):
        op = { '+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        # todo
        pass 

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
    
    def print_expression(self, exp: str) :
        
        # Creates a list of variables found in the expression
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]    # Given as hint on Canvas
        
        # Creates list of tokens (everything other than the variables)
        everything_else = re.split('\w+', exp)    # Given as hint on Canvas
        
        result = ''
        
        # Concate into one string (result var)
        for i in range(len(everything_else)):
            result += everything_else[i]
            
            # Verifies loop variable is within the range of list of variables stored
            if i < len(variables):
                value = self.dict.find(variables[i])    # Find the value of the variable with the given key
                
                if value is not None:   # Verifies if there is a value for the variable
                    result += str(value)
                    
                else:   # If there is no value, add the variable bc there is no value for the variable
                    result += variables[i]
                
        print(result)