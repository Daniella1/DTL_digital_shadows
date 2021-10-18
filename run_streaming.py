import subprocess

# start ur communication
# start kuka communication
# start unity application
# subprocess.run("python communication_ur/run_experiment.py & python communication_kuka/nonblockingTCPserver.py", shell=True)
subprocess.run("python communication_ur/run_experiment.py & .\LiveMovementUnity\\3D Project.exe", shell=True)


