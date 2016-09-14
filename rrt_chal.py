# import numpy as np
# import matplotlib.pyplot as mp
# from matplotlib.path import Path
# import matplotlib.patches as patches
# # let's plot a triangle:
# tree = [
#     [-1,0],
#     [1, 0],
#     [0,1.5]
#     ]
# verts = []
# codes = []
# tree.append(tree[0])

# for i,t in enumerate(tree[:-1]):
#     verts.append(t)                
#     verts.append(tree[i+1])
#     codes.append(Path.MOVETO)
#     codes.append(Path.LINETO)
# #MOVETO = put a pen on the point
# #LINETO = mark line between 2 points

# fig = mp.figure() #build figure from matplotlib.pyplot
# path = Path(verts, codes) #generate path
# patch = patches.PathPatch(path) #generate path
# ax = fig.add_subplot(1,1,1) #adjust the figure scale
# ax.add_patch(patch) #add line
# ax.set_xlim([-1.5,1.5]) #set grid
# ax.set_ylim([-1.5,1.5]) #set grid 
# mp.show()
# -----------------------------------------------------------

g_vertex = {} #points >> g_vertex
q_init = (50,50)
g_edge = [] #tree >>  g_edge
k_round = 10000
q_delta = 0.5

def print_fig(tree):
    import numpy as np
    import matplotlib.pyplot as mp
    from matplotlib.path import Path
    import matplotlib.patches as patches
     
    verts = tree
    codes = []

    for i in range(len(verts)):
        if i % 2 == 0:
            codes.append(Path.MOVETO)
        else:
            codes.append(Path.LINETO)

    #tree.append(tree[0])
    print tree,"len = ",len(tree)
    
    # for i,t in enumerate(tree[:-1]):
    #     verts.append(t)                
    #     verts.append(tree[i+1])
    #     codes.append(Path.MOVETO)
    #     codes.append(Path.LINETO)

    print verts,"len = ",len(verts)
    print codes,"len = ",len(codes)
    fig = mp.figure() #build figure from matplotlib.pyplot
    path = Path(verts, codes) #generate path
    patch = patches.PathPatch(path) #generate path
    ax = fig.add_subplot(1,1,1) #adjust the figure scale
    ax.add_patch(patch) #add line
    ax.set_xlim([0,100]) #set grid
    ax.set_ylim([0,100]) #set grid 
    mp.show()


def dist_calc(p0,p1):
    import math
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


def new_point_from_delta(p0,p1,delta):
    q_near_x = abs(p1[0]-p0[0])
    q_near_y = abs(p1[1]-p0[1])

    qx = delta*q_near_x
    qy = delta*q_near_y
    print 'qx = ',qx,' qy = ',qy
    #find x1_new
    if p0[0] > p1[0]:
        qx = -1*qx
    if p0[1] > p1[1]:
        qy = -1*qy

    q_new_x = p0[0] + qx
    q_new_y = p0[1] + qy

    return (int(q_new_x), int(q_new_y))


def basic_rrt(q_init, k_round, q_delta):
    g_vertex[q_init] = 0
    #tree.append(list(q_init))
    
    # loop of K rounds
    for loop_no in range(k_round):
    
        # random a point
        import random
        q_rand = (int(random.uniform(0,100)),int(random.uniform(0,100)))

        # calculate all distance compared with q_init
        for i in g_vertex:
            g_vertex[i] = dist_calc(i,q_rand)

        # get the nearest point
        nearest_d = min(g_vertex.itervalues())
        for i in g_vertex:
            if g_vertex[i] == nearest_d:
                q_near = i
    
        # plot a new point according to q_delta
        
        q_new = new_point_from_delta(q_near, q_rand, q_delta)

        #append the new point to tree list
        g_edge.append(list(q_near))
        g_edge.append(list(q_new))
        g_vertex[q_new] = 0

    # after all k loops, print the figure
    print_fig(g_edge)
 

basic_rrt(q_init, k_round, q_delta)


