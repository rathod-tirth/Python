# question and answer

'''
    - ask user to type a short question and then its answer
    - repeat this process about 5 times
    - store the question and answer in a dict, in this format:
    
        dict_name={"q1":{"q":"user question", "a":"user answer"},
                   "q2":{"q":"user question", "a":"user answer"},
                   ...}
'''

QnA={}

for i in range(1,6):
    que=input("\nEnter short fun-fact type question: ")
    ans=input("Now answer the above question: ")

    QnA[f"q{i}"]={"q":que,"a":ans}

print()
for i in QnA.items():
    print(i)
