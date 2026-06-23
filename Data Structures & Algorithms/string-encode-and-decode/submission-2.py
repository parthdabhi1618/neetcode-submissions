class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=""
        for s in strs:
            encoded_str+=str(len(s))+"#"+s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            j+=1
            curr_str=s[j:j+length]
            decoded_strs.append(curr_str)
            i=j+length
        return decoded_strs