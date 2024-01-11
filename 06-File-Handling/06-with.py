# with statement closes the file autmatically, it prevents data leakage and corruption

with open('data.txt','r') as file:
   read=file.read()
   
print(read)
   
# no need to close the file and everthing is inside the code block
# this ensures organised code and ensures closing the file