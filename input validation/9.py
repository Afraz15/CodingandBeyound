                                # MULTIPLICATION PROJRCT

import pyinputplus as p
import time,random

numofques = 1
correct = 0
for quesnum in range(numofques):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = f'{quesnum}: {num1} x {num2} = '
try:
    p.inputStr(prompt,allowRegexes = [f'^{num1 * num2}'], blockRegexes = [('.*','Incorrect!')], timeout = 8, limit = 3)
except p.TimeoutException:
    print('out of time')
except p.RetryLimitException:
    print('out of tries')
else:
    print('correct!')
    correct += 1
    time.sleep(1)
print(f'score: {correct} /  {numofques}')

