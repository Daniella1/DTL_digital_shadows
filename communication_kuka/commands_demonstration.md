# Kuka external commands
## these commands make specific movements for testing purposes
- send_command("move1\n")  `move to center position of TCP`
- send_command("move2\n")  `lemniscaste motion`
- send_command("move3\n")  `null space`
- send_command("move4\n")  `inverse null space`
- send_command("move5\n")  `start position`

### (For pick&place app)
#### First group of commands
- send_command("movelrel(633,-13,255,-125,-27,-169)\n") `start position`
- send_command("movelrel(645,44,258,-149,-1.39,-179.40)\n") `tool aligned`
- send_command("movelrel(445,-570,350,-149,-1.39,-179.40)\n") `towards outside - above the item`
- send_command("movelrel(445,-570,240,-149,-1.39,-179.40)\n") `picking the item`
- send_command("movelrel(445,-570,350,-149,-1.39,-179.40)\n") `above the item`
- send_command("movelrel(400,0,230,-149,-1.39,-179.40)\n") `ready to locate`
- send_command("movelrel(400,0,150,-149,-1.39,-179.40)\n") `placing the item`
- send_command("movelrel(400,0,280,-149,-1.39,-179.40)\n") `finished`


#### Using corners
- send_command("movelrel(600,-150,200,-149,-1.39,-179.40)\n") `at the corner`
- send_command("movelrel(600,80,200,-149,-1.39,-179.40)\n") `border center`
- send_command("movelrel(600,250,200,-149,-1.39,-179.40)\n") `at the column`
- send_command("movelrel(450,-150,200,-149,-1.39,-179.40)\n") `border`
- send_command("movelrel(400,80,200,-149,-1.39,-179.40)\n") `center`
- send_command("movelrel(450,250,200,-149,-1.39,-179.40)\n") `opposite`

#### Movements in a row `execute_example(1.5)`
- send_command("movelrel(600,-150,200,-149,-1.39,-179.40)\n") `at the corner`
- send_command("movelrel(600,-150,150,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,-150,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,-100,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,-100,150,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,-100,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,-50,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,-50,150,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,-50,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,0,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,0,150,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,0,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,50,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,50,150,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,50,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,100,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,100,150,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,100,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,150,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,150,150,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,150,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,200,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,200,150,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,200,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,250,200,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,250,150,-149,-1.39,-179.40)\n")
- send_command("movelrel(600,250,200,-149,-1.39,-179.40)\n")

#### Pick and place commands:
- execute_pick_and_place_basics(0.5)
- execute_pick_and_place_DT(0.5) `buids a DT on the cell - be sure to set the workpieces where supposed`
- execute_pick_and_place_DT_inverse(0.5) `returns the workpieces to the initial position`

#### To control the gripper (uses ModbusTCP):
- gripper_pick(0.5)
- gripper_place(0.5)

## Stop execution
- send_command("stop\n")
