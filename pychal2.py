import sys


#for i,arg in enumerate(sys.argv[1:]):
 #   print "arg = ",arg
  #  if arg == "-n":
   #     print "n found"
    #    lights = int(sys.argv[i+2])
   # elif arg == "-p":
    #    print "p found"
     #   msg_no = int(sys.argv[i+2])


def print_light(room):
    for light in range(len(room)):
        if room[light] == True:
            room[light] = 1
        else:
            room[light] = 0
    return room        
    

def process_lights(lights, msg_no):
    room = [False]*lights

    for order in range(lights):
        for light in range(len(room)):
            if ((light+1) % (order+1)) == 0:
                room[light] = not(room[light])
        if order < (msg_no + 1):
            print "The first 100th lights in the room at the order of ", order + 1
            print print_light(room[:lights])

if __name__ == "__main__":
    print sys.argv
    lights = int(sys.argv[1])
    msg_no = int(sys.argv[2])
    process_lights(lights, msg_no)

