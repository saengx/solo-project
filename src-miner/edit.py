import os, time, json
from config import banneredit
from multiprocessing import cpu_count


cpu_thread = cpu_count()


def OffMiner():
  
   banneredit()
   try:
       print("ชื่อคนงานขุด เช่น \033[93mMiner01\033[00m")
       name = input("[-n]: ")
       print("\033[35m-----------------------------------------\033[0m")
   except:
            os.system("@cls||clear")
            print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
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
