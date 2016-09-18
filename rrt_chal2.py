import rrt_chal
import sys
import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as mp

def main(q_init,k_round_q_delta):
    bg_array = get_array_from_pict("N_map.png")
    # state the origin
    basic_rrt_w_block(q_init,k_round,q_delta,block_array)
    

def get_array_from_pict(pict_dr):
    world = imread(pict_dr) #turn pict into arrays of 1 and 0
    world = np.flipud(world) #flip array in up-down direction
    return world

def read_pict(pict_dr):
    world = get_array_from_pict(pict_dr)
    Xmax = world.shape[0] #return the size of an array
    Ymax = world.shape[1]
    # set the origin at the lower
    mp.imshow(world, cmap=mp.cm.binary, interpolation='nearest', origin='lower',
              extent=[0,Xmax,0,Ymax])
    mp.show()
    

def basic_rrt_w_block(q_init,k_round,q_delta,block_array):
    g_vertex[q_init] = 0
    
    # loop of K rounds
    for loop_no in range(k_round):
    
        # random a point
        import random
        q_rand = (int(random.uniform(0,100)),int(random.uniform(0,100)))

        # calculate all distance compared with q_init
        for i in g_vertex:
            g_vertex[i] = rrt_chal.dist_calc(i,q_rand)

        # get the nearest point
        nearest_d = min(g_vertex.itervalues())
        for i in g_vertex:
            if g_vertex[i] == nearest_d:
                q_near = i

        # plot a new point according to q_delta
        
        q_new = rrt_chal.new_point_from_delta(q_near, q_rand, q_delta)

        # check whether any points penetrate a block
        if not_in_block(q_new,q_near):
        #append the new point to tree list
            g_edge.append(list(q_near))
            g_edge.append(list(q_new))
            g_vertex[q_new] = 0

    # after all k loops, print the figure
    print_fig(g_edge)


if __name__=="__main__":
    q_init = (int(sys.argv[1]),int(sys.argv[2])
    k_round = int(sys.argv[3])
    q_delta = float(sys.argv[4])
    main(q.init, k_round, q_delta)
    
