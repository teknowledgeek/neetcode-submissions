class Solution:

    def encode(self, strs : list[str]) -> str :
        encoded_str = ''
        for s in strs :
            encoded_str += str(len(s)) + "#" + s
        return encoded_str
    def decode(self, strs : str) -> list[str] :
        str_list = []
        length = 0
        start_index = 0
        stop_index = 0
        for i in range(0, len(strs)):
            if strs[i] == "#"  and i > start_index :
                
                stop_index = i 
                print(i, start_index,stop_index)
                print(strs[start_index:stop_index])
                length = int(strs[start_index:stop_index])+1 # as the last index is excluding 
                print(length)
                s = str(strs[stop_index+1 : stop_index + length])
                start_index = stop_index + length
                print(s)
                str_list.append(s)
        return str_list
