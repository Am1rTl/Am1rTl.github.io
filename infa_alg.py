class Stack:
    def __init__ (self):
        self.head = None
        self.size = 0
        
    def push(self, value):
        self.head = {"value": value, "next": self.head}
        self.size += 1
        
    def pop(self):
        if self.head is None:
            raise Exception("Ne pravilno")
        val = self.head["value"]
        self.size -= 1
        self.head = self.head["next"]
        return val

    def size(self):
        return size

               
a = str(input())
s = 0
st = Stack()
for i in range(len(a)):
    if a[i] == "(" or a[i] == "<" or a[i] == "{" or a[i] == "[" :
        st.push(1)
    elif a[i] == ")" or a[i] == ">" or a[i] == "}" or a[i] == "]" :
        if st.size == 0:
            print("All is good")
            s = 1
            break
        else:
            st.pop()
if s != 1:
    if st.size == 0:
        print("All is good")
    elif st.size > 0:
        print("All in not good")       
        
        
        
        
        
        
        
