class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=False)


        stk = []

        for i in range(len(cars)):
            tt = (target-cars[i][0])/cars[i][1]

            while stk and tt >= stk[-1]:
                stk.pop()
            
            stk.append(tt)
        
        return len(stk)
