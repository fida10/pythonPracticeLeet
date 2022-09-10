#2391. Minimum Amount of Time to Collect Garbage
# class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # id how many m, g, or P in the index, add 1 for each num of value,
        # depending ono the index add travel time as well

        PickG = 0
        PickP = 0
        PickM = 0
        counter = 0
        RideG = 0
        RideP = 0
        RideM = 0
        travelStart = [0]
        travel = travelStart + travel
        cg = 0
        cp = 0
        cm = 0

        # ["G","P","GP","GG"]
        for x in garbage:
            temp = x.count("G")
            if temp > 0:
                PickG += temp
                cg = counter

                # RideG = sum(travel)

            temp = x.count("P")
            if temp > 0:
                PickP += temp
                # RideP = sum(travel)
                cp = counter

            temp = x.count("M")
            if temp > 0:
                PickM += temp
                cm = counter
            # RideM = sum(travel)

            counter += 1
            # print("Pick ",PickG, " ",  PickP ," " , PickM , "Ride:", RideG , " ",  RideP , " ", RideM)

        RideG = sum(travel[0:(cg + 1)])
        RideP = sum(travel[0:(cp + 1)])
        RideM = sum(travel[0:(cm + 1)])

        return (PickG + PickP + PickM + RideG + RideP + RideM)