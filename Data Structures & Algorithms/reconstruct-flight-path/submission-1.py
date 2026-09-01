class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict

        tickets.sort(reverse=True)

        routes = defaultdict(list)

        for src,des in tickets:
            routes[src].append(des)

        itinerary = []

        def boardPlane(airport):
            
            while routes[airport]:
                n_airport = routes[airport].pop()
                boardPlane(n_airport)
            
            itinerary.append(airport)
        
        boardPlane("JFK")
            
        return itinerary[::-1]
                    