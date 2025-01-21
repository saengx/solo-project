import os, time, json
from config import banneredit
from multiprocessing import cpu_count


cpu_thread = cpu_count()


def OffMiner():
  
   banneredit()
   try:
       print("ตัวอย่าง:")
       print("ชื่อคนงานขุด เช่น \033[92mMiner01\033[00m")
       name = input("[-n]: ")
       print("\033[36m-----------------------------------------\033[0m")
       print("\033[36m-----------------------------------------\033[0m")
            time.sleep(3)
            os.system("edit")   
   push = {
         'name': name
          }
   with open("set-miner/name.json", "w") as set:
        json.dump(push, set, indent=4)

     
while True:
  banneredit()
  OffMiner()
  os.system("run")     
  break
