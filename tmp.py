class Solution:
    def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> bool:
        '''
        :param pushed: [1,2,3,4,5]
        :param popped: [4,5,3,2,1]
        :return: True
        '''
        stack = []
        for push in pushed:
            while popped and push == popped[0]:
                popped = popped[1:]
                push = stack[-1]
            else:
                stack.append(push)

        return popped == []
