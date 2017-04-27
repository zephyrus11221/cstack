from display import *
from draw import *
from parser import *
from copy import deepcopy
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'save', 'circle', 'bezier', 'hermite', 'box', 'sphere', 'torus' ]

def parse_file( fname, edges, transform, screen, color ):

    f = open(fname)
    lines = f.readlines()

    cstack = []
    m = new_matrix()
    m1 = new_matrix()
    ident(m)
    ident(m1)
    cstack.append(deepcopy(m))
    cstack.append(deepcopy(m1))
    step = 0.1
    c = 0
    while c < len(lines):

        line = lines[c].strip()
        #print ':' + line + ':'

        if line in ARG_COMMANDS:            
            c+= 1
            args = lines[c].strip().split(' ')
            #print 'args\t' + str(args)
            
        if line == 'sphere':
            #print 'SPHERE\t' + str(args)
            add_sphere(edges,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step)
            matrix_mult( cstack[-2], edges )
            matrix_mult( cstack[-1], edges )
            draw_polygons(edges, screen, color)
            edges = []
            
        elif line == 'torus':
            #print 'TORUS\t' + str(args)
            add_torus(edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), step)
            matrix_mult( cstack[-2], edges )
            matrix_mult( cstack[-1], edges )
            draw_polygons(edges, screen, color)
            edges = []
            
        elif line == 'box':
            print 'BOX\t' + str(args)
            add_box(edges,
                    float(args[0]), float(args[1]), float(args[2]),
                    float(args[3]), float(args[4]), float(args[5]))
            print_matrix(cstack[-1])
            print_matrix(cstack[-2])
            matrix_mult( cstack[-2], edges )
            matrix_mult( cstack[-1], edges )
            draw_polygons(edges, screen, color)
            edges = []
            
        elif line == 'circle':
            #print 'CIRCLE\t' + str(args)
            add_circle(edges,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step)
            matrix_mult( cstack[-2], edges )
            matrix_mult( cstack[-1], edges )
            draw_polygons(edges, screen, color)
            edges = []

        elif line == 'hermite' or line == 'bezier':
            #print 'curve\t' + line + ": " + str(args)
            add_curve(edges,
                      float(args[0]), float(args[1]),
                      float(args[2]), float(args[3]),
                      float(args[4]), float(args[5]),
                      float(args[6]), float(args[7]),
                      step, line)                      
            matrix_mult( cstack[-2], edges )
            matrix_mult( cstack[-1], edges )
            draw_polygons(edges, screen, color)
            edges = []
            
        elif line == 'line':            
            #print 'LINE\t' + str(args)

            add_edge( edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )
            matrix_mult( cstack[-2], edges )
            matrix_mult( cstack[-1], edges )
            edges = []

        elif line == 'scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(t, cstack[-1])

        elif line == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(t, cstack[-1])

        elif line == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(args[1]) * (math.pi / 180)
            
            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            print_matrix(cstack[-2])
            print_matrix(t)
            matrix_mult(t, cstack[-2])
            print_matrix(cstack[-2])
                
        elif line == 'clear':
            edges = []
            
        elif line == 'ident':
            ident(transform)

        elif line == 'apply':
            matrix_mult( cstack[-1], edges )

        elif line == 'display' or line == 'save':

            if line == 'display':
                display(screen)
            else:
                save_extension(screen, args[0])
            clear_screen(screen)

        elif line == 'pop':
            print 'pop'
            print len(cstack)
            print_matrix(cstack.pop())
            print_matrix(cstack.pop())
            print len(cstack)

        elif line == 'push':
#            print cstack
            cstack.append(deepcopy(cstack[-2]))
            cstack.append(deepcopy(cstack[-2]))
        c+= 1


parse_file( 'script', edges, transform, screen, color )
'''

for i in range(4):
    edges = []
    add_sphere(edges, 0, 0, 0, 150, .1/(8-i*2+1))
    color = [20+i*10, i*40, i*60]
    matrix_mult(make_rotY(math.pi/2), edges)
    matrix_mult(make_translate(250, 250, 0), edges)
    draw_polygons(edges, screen, color)

for i in range(4):
    edges = []
    add_sphere(edges, 0, 0, 0, 50, .3/(8-i*2+1))
    color = [20+i*10, 0, i*60]
    matrix_mult(make_rotY(math.pi/2), edges)
    matrix_mult(make_translate(50, 50, 0), edges)
    draw_polygons(edges, screen, color)

for i in range(4):
    edges = []
    add_sphere(edges, 0, 0, 0, 50, .3/(8-i*2+1))
    color = [20+i*20, i*40, 0]
    matrix_mult(make_rotY(math.pi/2), edges)
    matrix_mult(make_translate(450, 50, 0), edges)
    draw_polygons(edges, screen, color)

for i in range(4):
    edges = []
    add_sphere(edges, 0, 0, 0, 50, .3/(8-i*2+1))
    color = [20+i*55, 0, i*30]
    matrix_mult(make_rotY(math.pi/2), edges)
    matrix_mult(make_translate(50, 450, 0), edges)
    draw_polygons(edges, screen, color)

for i in range(4):
    edges = []
    add_sphere(edges, 0, 0, 0, 50, .3/(8-i*2+1))
    color = [80, i*60, i*30]
    matrix_mult(make_rotY(math.pi/2), edges)
    matrix_mult(make_translate(450, 450, 0), edges)
    draw_polygons(edges, screen, color)

for i in range(4):
    edges = []
    add_torus(edges, 0, 0, 0, 25, 200, .3/(8-i+1))
    color = [240-i*60, 0, 200-i*30]
    matrix_mult(make_rotX(math.pi/2), edges)
    matrix_mult(make_translate(250, 250, 0), edges)
    draw_polygons(edges, screen, color)

display(screen)
'''




