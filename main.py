from display import *
from draw import *
from parser import *
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
'''





display(screen)
