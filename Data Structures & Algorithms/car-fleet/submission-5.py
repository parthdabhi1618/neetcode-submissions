class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timing=[]
        i=0
        while i<len(speed):
            timing.append((target-position[i])/speed[i])
            i+=1
        sorted_position,res_timing=zip(*sorted(zip(position,timing),reverse=True))
        que=[]
        fleet,i,lt=1,0,res_timing[0]
        while i<len(res_timing):
            if res_timing[i]>lt:
                lt=res_timing[i]
                fleet+=1
            i+=1
        return fleet