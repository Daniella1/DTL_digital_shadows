# Kuka external commands
## these commands make specific movements for testing purposes
- send_command("move1\n")  `move to center position of TCP`
- send_command("move2\n")  `lemniscaste motion`
- send_command("move3\n")  `null space`
- send_command("move4\n")  `inverse null space`
- send_command("move5\n")  `start position`

## Radian-based (joint-based) PTP movement commands - Always work
It requires 7 parameters, from Axis1 to Axis7. The parameters should be entered in degrees and the software convert them into radians.  

- send_command("moveptprad(0,20,0,-90,0,-45,90)\n")
- send_command("moveptprad(0,45,0,-90,0,-40,90)\n")
- send_command("moveptprad(0,40,0,-80,0,-40,80)\n")
- send_command("moveptprad(0,60,0,-80,15,-40,80)\n")
- send_command("moveptprad(0,30,30,-45,15,-40,80)\n")
- send_command("moveptprad(30,45,60,0,35,-10,50)\n")

### (For pick&place app)
- send_command("moveptprad(169,-40,8,111,-2,-25,90)\n") `init position`
- send_command("moveptprad(169.9,-35,8,111,-2,-25,90)\n") `up`
- send_command("movelrel(450,-240,-20,126.8,84.8,41.3)\n") `up lin rel`
- send_command("movelrel(300,-230,-300,126.8,84.8,41.3)\n") `towards outside the table`
- send_command("movelrel(300,-350,-670,126.8,84.8,41.3)\n") `above external table`
- send_command("movelrel(320,-350,-670,126.8,84.8,41.3)\n") `above recipient`
- send_command("movelrel(320,-240,-670,126.8,84.8,41.3)\n") `at recipient`
- send_command("movelrel(450,-240,-20,126.8,84.8,41.3)\n") `picking and placing`

- send_command("movelrel(575,-270,70,126.8,84.8,41.3)\n") `above the piece`
- send_command("movelrel(575,-160,70,126.8,84.8,41.3)\n") `at the piece`
- send_command("movelrel(600,-270,-180,126.8,84.8,41.3)\n") `at the corner above`
- send_command("movelrel(600,-160,-180,126.8,84.8,41.3)\n") `at the corner`

- send_command("movelrel(320,-350,-670,126.8,84.8,41.3)\n") `above recipient initial place`
- send_command("movelrel(320,-240,-670,126.8,84.8,41.3)\n") `placing recipient into the start position`

## Cartesian-based PTP movement commands - Can violate limits
it requires 6 parameters representing a frame (x,y,z,a,b,c)  
- send_command("moveptpcart(0,0,0,90,0,90)\n")

## Linear LIN movement commands - Can violate limits
it requires 6 parameters representing a frame (x,y,z,a,b,c)
- send_command("movelin(-100,100,0,0,90,180)\n")

## Linear relative LINREL movement commands - Can violate limits
it requires 6 parameters representing a frame (x,y,z,a,b,c). An additional parameter is optional but not implemented (ref.system).
- send_command("movelrel(-10,-10,-10,0,0,0)\n")
- send_command("movelrel(-10,10,0,0,0,0)\n")

## Circular CIRC movement commands - Can violate limits
it requires 6 parameters representing a frame (x,y,z,a,b,c). It considers the initial point as the start point.
- send_command("movecirc(10,10,10,0,0,0)\n")

## SPL movement commands - Can violate limits
it requires 6 parameters representing a frame (x,y,z,a,b,c)
- send_command("movespl(10,10,10,0,0,0)\n")

## SPLINE movement commands - Not yet implemented (a full path with several points)

## Stop execution
- send_command("stop\n")
