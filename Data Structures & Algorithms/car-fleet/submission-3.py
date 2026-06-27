class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timing=[]
        i=0
        while i<len(speed):
            timing.append((target-position[i])/speed[i])
            i+=1
        sorted_position,res_timing=zip(*sorted(zip(position,timing),reverse=True))
        que=[]
        fleet=1
        i=0
        while i<len(res_timing):    
            if que and que[0]<res_timing[i]:
                que=[]
                fleet+=1
            que.append(res_timing[i]) 
            i+=1
            print(i,que,fleet)
        print(res_timing)
        return fleet