### Import libraries

from vpython import *

#-----------------------------------------------------------------------------#
### Parameters
m_A = 1 # Mass' A [kg]
m_B = 100**2 # Mass' B[kg]
v_A = 0 # Speed's A [m/s]
v_B = -10 # Speed's B [m/s]
e_pp = 1 # Coefficient of Restitution particle-particle
e_pw = 1 # Coefficient of Restitution particle-wall


#-----------------------------------------------------------------------------#
### Velocity after impact between particles A and B
def vel_pp(m_A, m_B, v_A, v_B, e_pp):

    v_A_2 = (m_A*v_A+m_B*v_B - e_pp*m_B*(v_A-v_B))/(m_A+m_B)
    v_B_2 = e_pp*(v_A-v_B)+v_A_2
    return v_A_2, v_B_2

#-----------------------------------------------------------------------------#
### Velocity after impact between particle A and wall
def vel_pw(v_A, e_pw):
    
    v_A_2 = -e_pw*v_A
    return v_A_2

#-----------------------------------------------------------------------------#
### Set display and background

scene = canvas(title = 'Collisions', x = 0, y = 0,
     width = 1000, height = 300,
     center = vector(0,0,0), background = color.black,
     fov = 0.05)

# fov : Field of view of the camera in radians

#-----------------------------------------------------------------------------#
### Create floor and wall

floor = box(pos = vector(0,-10.5,0), length = 50, height = 1, width = 5, color = color.blue)
wall = box(pos = vector(-25.5,-6,0), length = 1, height = 10, width = 5, color = color.blue)

#-----------------------------------------------------------------------------#
### Create cubes

side = 2 # Distance from center of cube to the side

cube_A = box(pos = vector(0,-8,0), 
    length = 2*side, height = 2*side, width = 2*side, 
    color = color.red)

cube_A.velocity = vector(0,0,0)

cube_B = box(pos = vector(23,-8,0), 
    length = 2*side, height = 2*side, width = 2*side, 
    color = color.green)

cube_B.velocity = vector(v_B,0,0)

#-----------------------------------------------------------------------------#

## Linear Momentum plot
g1 = graph(width = 500, height = 500,
    xtitle = 'time [s]', ytitle = "Linear Momentum [kg-m/s]")
mvA = gcurve(color = color.red) # a graphics curve
mvB = gcurve(color = color.green)

## kinetic energy plot
g2 = graph(width = 500, height = 500,
    xtitle = 'time [s]', ytitle = "Kinetic Energy [J]")
kA = gcurve(color = color.red) # a graphics curve
kB = gcurve(color = color.green)

#-----------------------------------------------------------------------------#
### Motion

t = 0 # Time
dt = 0.01 # Delta of time
run = True # Running condition
col = 0 # Collision
con = 0 # Counter to stop simulation

while run:
    rate(100) # Rate of frames

    ## Not Collision
    if (cube_B.pos.x-side) >= (cube_A.pos.x+side):

        cube_B.pos = cube_B.pos + cube_B.velocity*dt # Change B position
        cube_A.pos = cube_A.pos + cube_A.velocity*dt # Change A position

    ## Collision A-B
    elif (cube_B.pos.x-side) < (cube_A.pos.x+side):

        v_A, v_B = vel_pp(m_A, m_B, v_A, v_B, e_pp) # Velocities after impact
        
        col += 1 # Add +1 to the collision counter

        cube_A.velocity = vector(v_A,0,0) # Set new A velocity
        cube_B.velocity = vector(v_B,0,0) # Set new B velocity

        cube_B.pos = cube_B.pos + cube_B.velocity*dt # Change B position
        cube_A.pos = cube_A.pos + cube_A.velocity*dt # Change A position



    ## Collision A-Wall
    if (cube_A.pos.x-side) <= wall.pos.x+0.5:

        v_A = vel_pw(v_A,e_pw) # Velocity after impact

        col += 1 # Add +1 to the collision counter

        cube_A.velocity = vector(v_A,0,0) # Set new A velocity

        cube_A.pos = cube_A.pos + cube_A.velocity*dt # Change A position

    ## Stop Condition
    if v_A >= 0  and v_B >= 0 and v_B > v_A:

        con += 1

        if con == 100: # Stop after 100 time steps

            break

    ## Don't show B after go outside frame of vpython
    if cube_B.pos.x > 25:

        cube_B.visible = False

    t += dt # Current time

    # Show Number of impacts
    label(pos=vector(0,8,0), text='Impactos: {}'.format(col), color = color.white,linecolor=color.black)

    # Show Velocity of A
    label(pos=vector(0,5,0), text='Velocidad A: {:.2f} m/s'.format(cube_A.velocity.x), color = color.red, linecolor=color.black)
    
    # Show Velocity of B
    label(pos=vector(0,2,0), text='Velocidad B: {:.2f} m/s'.format(cube_B.velocity.x), color = color.green, linecolor=color.black)


    ## Plots
    mvA.plot(t,m_A*cube_A.velocity.x)
    mvB.plot(t,m_B*cube_B.velocity.x)

    kA.plot(t,(m_A*cube_A.velocity.x**2)/2)
    kB.plot(t,(m_B*cube_B.velocity.x**2)/2)
