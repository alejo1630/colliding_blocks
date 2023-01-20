# Colliding Blocks

This Python code computes the kinematics data (linear momentum and kinetic energy) for the 2D collission between 2 blocks and a rigid wall taking into account the [coefficient of restitution](https://en.wikipedia.org/wiki/Coefficient_of_restitution) but ignoring the friction. 

## 🔰 How does it work?

- The code uses [VPython](https://vpython.org/) library to create the 2D-3D interactive environment and the physics interactions.
  
<img src = "https://github.com/alejo1630/colliding_blocks/blob/main/Image_readme/1.png" width="600">

- Letter A is set for the red block and the letter B is set for the green block.
- User has to enter the following parameters
  - Blocks' mass.
  - Initial velocity of the blocks (in the main case the red block doesn't have initial velocity).
  - Coefficient of restitution between the red and the green block.
  - Coefficient of restitution between the red block and the rigid wall.

- After each collision the kinematic data is computed using the following equations (Notation: 1-Before collision, 2-After collision):
  - Conservation of momentum:
  $$m_A (v_A)_1 + m_B (v_B)_1  = m_A (v_A)_2 + m_B (v_B)_2$$
  
  - Conservation of energy:
  $$\frac{1}{2} m_A {(v_A)_1}^2 + \frac{1}{2} m_B {(v_B)_1}^2  = \frac{1}{2} m_A {(v_A)_2}^2 + \frac{1}{2} m_B {(v_B)_2}^2 $$
  
  - Coefficien of restitution between blocks:
  $$e = \frac{(v_B)_2 - (v_A)_2}{(v_B)_1 - (v_A)_1}$$
  
  - Coefficient of restitution between the red block and the rigid wall:
  $$e = -\frac{(v_A)_2}{(v_A)_1}$$

- Kinematic data for both blocks is computed for each step of time during the simulation:
  - Linear momentum
  
  <img src = "https://github.com/alejo1630/colliding_blocks/blob/main/Image_readme/2.png" width="400">
  
  - Kinetic energy
  
  <img src = "https://github.com/alejo1630/colliding_blocks/blob/main/Image_readme/3.png" width="400">
  
- There is an special set of parameters which could be used to calculated the digits of Pi $(\pi)$.
  - All the coefficients of restitution muts be equal to 1 (perfectly elastic)
  - Mass' A must be equal to 1.
  - Mass' B bust be equal to $100^{n-1}$, where $n$ is the number of digits of Pi computed based on the number of collision between all the bodies during the simulation. For example:
    - If $n = 1$ $(m_B = 1 kg)$, the number of collision would be $3$
    
    - If $n = 2$ $(m_B = 100 kg)$, the number of collision would be $31$
    
    - If $n = 3$ $(m_B = 10000 kg)$, the number of collision would be $314$
    
 - An explanation of this peculiar phenomenon is described by [G.Galperin](https://www.maths.tcd.ie/~lebed/Galperin.%20Playing%20pool%20with%20pi.pdf) with a lot of math, but there is an incredible and illustrative explanation in the [3Blue1Browm Youtube Channel](https://www.youtube.com/watch?v=jsYwFizhncE)
 
    
## 🔶 What is next?

- Increase the number of blocks and rigid walls. 
