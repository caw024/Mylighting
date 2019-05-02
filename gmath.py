import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normalize(light[0])
    normalize(normal)
    Iamb = calculate_ambient(light,areflect)
    Idif = calculate_diffuse(light,dreflect,normal)
    Ispec = calculate_specular(light,sreflect,view,normal)
    Isum = [ Iamb[i] + Idif[i] + Ispec[i] for i in range(0,3) ]
    Isum = limit_color(Isum)
    print(Isum)
    return Isum

def calculate_ambient(light, areflect):
    return [areflect[i] * light[1][i] for i in range(0,3) ]

def calculate_diffuse(light, dreflect, normal):
    return [light[0][i] * dreflect[i] * dot_product(normal,light[1]) for i in range(0,3)]

def calculate_specular(light, sreflect, view, normal):
    dot = dot_product( [2*normal[k]*(normal[k]-light[1][k]) - light[1][k] for k in range(0,3) ] , view)
    return [light[0][i] * sreflect[i] * dot for i in range(0,3)]

def limit_color(color):
    k = 0
    while k < 3:
        if color[k] > 255:
            color[k] = 255
        if color[k] < 0:
            color[k] = 0
        k += 1
    return color

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
