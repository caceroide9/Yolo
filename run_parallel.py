import subprocess
from threading import Thread

def run_command(cmd):
    subprocess.run(cmd, shell=True)

command1 = "python detect.py --weights runs/train/exp/weights/pisos.pt --img 640 --conf 0.40 --source 1"
command2 = "python detect.py --weights runs/train/exp/weights/agujeros.pt --img 640 --conf 0.40 --source 2"

thread1 = Thread(target=run_command, args=(command1,))
thread2 = Thread(target=run_command, args=(command2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()