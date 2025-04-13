'''
ou're given a list of logs that represent function calls in a single-threaded CPU.

Each log is in this format:

"<function_id>:<start|end>:<timestamp>"
You have to compute the exclusive time each function spent executing, excluding time when it was paused because another function ran (nested calls).
'''

n = 2
logs = [
  "0:start:0",
  "1:start:2",
  "1:end:5",
  "0:end:6"
]

def func_time(logs, n):
    stack = []
    result = [0] * n
     
    curr_t = 0
    for log in logs:
        id, op, t = log.split(':')
        
        t = int(t)
        
        if op == 'start':
            stack.append([id, t])
        
        if op == 'end':
            f = stack.pop()
            f_total = (t - f[1]) + 1
            result[int(f[0])] = f_total
            if stack:
                f2 = stack[-1]
                f2[1] = f_total + int(f2[0]) 
    
    return result

print(func_time(logs, n))

logs = [
  "0:start:0",
  "1:start:2",
  "2:start:3",
  "2:end:4",
  "1:end:6",
  "0:end:7"
]

print(func_time(logs, 3))