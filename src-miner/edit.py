import os, time, json
from config import banneredit
from multiprocessing import cpu_count


cpu_thread = cpu_count()


def OffMiner():
  
   banneredit()
   try:
       print("ตัวอย่าง:")
       print(" \033[92mstratum+tcp://public-pool.io:21496\033[00m")
       print(" \033[92mstratum+tcp://doge.solopool:4620\033[00m")
       pool = input(" pool : ")
       print("\033[36m-----------------------------------------\033[0m")
        
       print("ตัวอย่าง:  \033[92msha256d,scrypt\033[00m")
       algo = input(" algo : ")
       print("\033[36m-----------------------------------------\033[0m")

       print("ตัวอย่าง: \033[92m1Jykw3Pqou9z2498D3YncCHRCE4Xa8Disf\033[00m")
       print("ตัวอย่าง: \033[92mDCYiQottcGcnmzkp9KqqJwowc3ifEZUxm1\033[00m")
       wallet = input("wallet: ")
       print("\033[36m-----------------------------------------\033[0m")

       print("ตัวอย่าง:  \033[92mx \033[00m")
       password = input("password : ")
       print("\033[36m-----------------------------------------\033[0m")

       print("ชื่อคนงานขุด เช่น \033[92mMiner01\033[00m")
       name = input("[-n]: ")
       print("\033[36m-----------------------------------------\033[0m")
        
       print(f"จำนวนthread \033[92mค่าที่ใส่ได้คือ 0 ถึง {cpu_thread}\033[00m")
       cpu = int(input("[-t]: "))
       print("\033[36m-----------------------------------------\033[0m")

       if pool == "" or wallet == "":
          raise Exception()
       if password == "":
          raise Exception()
   except:
            os.system("@cls||clear")
            print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
            time.sleep(3)
            os.system("edit")   
   push = {
         'pool': pool,
         'algo': algo,
         'wallet': wallet,
         'pass': password,
         'name': name,
         'cpu': cpu
          }
   with open("set-miner/online.json", "w") as set:
        json.dump(push, set, indent=4)

     
while True:
  banneredit()
  OffMiner()
  os.system("run")     
  break
