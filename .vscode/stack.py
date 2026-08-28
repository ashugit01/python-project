stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack[-1])
print(stack.pop())
print(stack)


#reverse a string using stacks
stack=[]
stack.append(10)
stack.append(20)
stack.append(25)
print(stack.pop())
print(stack.pop())
print(stack.pop())





#implement stack using queue
import queue
st=queue.LifoQueue()
st.put(10)
st.put(20)
st.put(30)
print(st.get())
print(st.queue)