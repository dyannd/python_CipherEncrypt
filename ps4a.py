# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # l=len(sequence)
    #base case: only 1 character in list: 
    
    if len(sequence)==1:
        return [sequence]
    #if there are more than 1 character, pick1 char and consider the others n-1 character
    else:
        ans=[]
      
        #hold 1 character
        for index in range(len(sequence)):
            #Print for flex
            
            hold=sequence[index]
            # print('Hold ', hold)
            left_side=sequence[0:index]
            right_side=sequence[index+1:len(sequence)]
            remaining=left_side+right_side
            # print('Remain ',remaining)
            
            #cut down the hold character 
            for i in range(len(remaining)):
                # print(hold)
                add_ans=hold+get_permutations(remaining)[i]
                # print(add_ans)
                ans.append(add_ans)
            # print(ans)
    return ans
                 
        

if __name__ == '__main__':
    #EXAMPLE
    example_input = 'ax'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a 
    # sequence of length n)

    

