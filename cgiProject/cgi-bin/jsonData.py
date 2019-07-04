import json
import time
import random

now = time.strftime("%H:%M:%S",time.localtime())
num = random.randint(1,10)

result = {"now":now,"num":num}

json_result = json.dumps(result)

print("content-type:application/json")
print('\n')
print(json_result)
