#code for the volumes of a halve sphere or a cylinder with a cone cut out of it, they have the same volume if the radius and height are the same

#imports
import time

#user input and variables
radius = int(input("radius: "))
pi = 3.1415926

#halve sphere calculation
def half_sphere_volume(radius, pi):
    volume = (2/3) * pi * radius**3
    return volume

#cylinder calculation
def cylinder_volume(radius, pi):
    height = radius
    volume = pi * radius**2 * height
    return volume

#cone calculation
def cone_volume(radius, pi):
    height = radius
    volume = (1/3) * pi * radius**2 * height
    return volume

#variable calculation
cylinder_vol = cylinder_volume(radius, pi)
cone_vol = cone_volume(radius, pi)
half_sphere_vol = half_sphere_volume(radius, pi)

#cylinder without cone
cylinder_without_cone_vol = cylinder_vol - cone_vol

#outputs
print("Volumen_Halbe Kugel: ", half_sphere_vol)
print("Volumen_Zylinder mit ausgehültem Kegel", cylinder_without_cone_vol)

#shutdown the code
print("Programm shutdown in 45 seconds")

time.sleep(45)
