class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        key=[chr(i) for i in range(97,123)]
        value=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code=dict(zip(key,value))
        after_trans=[]
        for i in words:
            morse=''
            for s in i:
                morse=morse+code[s]
            print(morse)
            if morse not in after_trans:
                after_trans.append(morse)
        return len(after_trans)