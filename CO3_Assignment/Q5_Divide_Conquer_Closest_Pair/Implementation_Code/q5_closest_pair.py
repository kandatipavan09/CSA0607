"""Q5: Brute-force and divide-and-conquer closest pair of 2D points."""
import math
def dist(p,q): return math.hypot(p[0]-q[0], p[1]-q[1])
def brute_force(points):
    best=float("inf"); pair=None; count=0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            count+=1; d=dist(points[i],points[j])
            if d<best: best,pair=d,(points[i],points[j])
    return best,pair,count
def closest_pair(points):
    px=sorted(points); py=sorted(points,key=lambda p:p[1])
    count=[0]
    def rec(xs, ys):
        n=len(xs)
        if n<=3:
            best=float("inf"); pair=None
            for i in range(n):
                for j in range(i+1,n):
                    count[0]+=1; d=dist(xs[i],xs[j])
                    if d<best: best,pair=d,(xs[i],xs[j])
            return best,pair
        mid=n//2; midx=xs[mid][0]
        leftx,rightx=xs[:mid],xs[mid:]
        leftset=set(leftx)
        lefty=[p for p in ys if p in leftset]
        righty=[p for p in ys if p not in leftset]
        dl,pl=rec(leftx,lefty); dr,pr=rec(rightx,righty)
        best,pair=(dl,pl) if dl<=dr else (dr,pr)
        strip=[p for p in ys if abs(p[0]-midx)<best]
        for i in range(len(strip)):
            j=i+1
            while j<len(strip) and strip[j][1]-strip[i][1]<best:
                count[0]+=1; d=dist(strip[i],strip[j])
                if d<best: best,pair=d,(strip[i],strip[j])
                j+=1
        return best,pair
    if len(points)<2: raise ValueError("At least two points required")
    result,pair=rec(px,py)
    return result,pair,count[0]
def main():
    pts=[(2,3),(12,30),(40,50),(5,1),(12,10),(3,4),(8,8),(9,9)]
    b,bp,bc=brute_force(pts); d,dp,dc=closest_pair(pts)
    print("Q5 - CLOSEST PAIR")
    print("Points:",pts)
    print(f"Brute force: distance={b:.4f}, pair={bp}, distance calculations={bc}")
    print(f"Divide & conquer: distance={d:.4f}, pair={dp}, distance calculations={dc}")
    print("Distances match:", math.isclose(b,d))
    print("Expected complexity: brute force O(n^2); divide and conquer O(n log n) with y-sorted strip processing.")
if __name__=="__main__": main()
