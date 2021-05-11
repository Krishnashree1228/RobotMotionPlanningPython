from TMapping import*


xs=[[1,1.5,3],[9,4,3,7]]
ys=[[6,8,7],[6,5,2,1]]
polygons=MultiPolygon([Polygon([(j1,j2) for j1,j2 in zip(i1,i2)])for i1,i2 in zip(xs,ys)])   
   
l=20
b=20

axs=create(polygons,l,b)

strips=createStrips(polygons,l,b)
#PlotStrips(axs,polygons,l,b)

t=createTrapeziums(strips,polygons)
#plotTrapezium(t,polygons,l,b)

pathPoints=createPathPoints(t)
#PlotPathPoints(pathPoints,polygons,l,b)
#createPath(triangulate(MultiPoint(pathPoints)),l,b,polygons)
#plt.show()


try:
    startx=float(input("enter x of start"))
    starty=float(input("enter y of start"))
    endx=float(input("enter x of end"))
    endy=float(input("enter y of end"))
    start=Point(startx,starty)
    end=Point(endx,endy)
    points=STRtree(pathPoints)
    if(start.within(polygons) or end.within(polygons)):
        raise "start or end invalid"
    
    S=points.nearest(start)
    E=points.nearest(end)
    createPathFinal(triangulate(MultiPoint(pathPoints)),l,b,polygons,start,S,end,E)
    
except :
    print("\n!!!!!!!!!!start or end invalid!!!!!!!!")



"""pathRec=pathRecord(polygons,pathPoints)
plotRoute(pathRec,pathPoints,polygons,l,b)
route=Route(pathRec,pathPoints)"""

plt.show()

