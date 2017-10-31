###############################################################################################################
#																										      #
#																										      #
#																										      #
#																										      #
# 	   NAME: REESHABH KUMAR RANJAN																	 	      #
# 	   ROLL NUMBER: 2017086																		 	 	      #
# 												 	      													  #
#        		       																						  #
#																										      #
#																										      #
#																										      #
#																										      #
###############################################################################################################



from sys import maxsize as infinity
undefined=-1

def input_elements():

	"""

	Precondition: Please enter positive weights.

	Function to input elements. It processes the input and assigns them to proper lists, namely masterNodeList and masterWeightList.
	It returns both.

	"""

	n=int(input())
	
	next_jump=[0]
	tracked=[0]

	masterNodeList=[]
	masterWeightList=[]

	while len(next_jump)>0:

		t=int(input())
		
		rawNodeInput=[]
		rawWeightInput=[]

		for i in range(t):
			
			temp=input()
			rawInput=[int(j) for j in temp.split()]

			rawNodeInput.append(rawInput[0])
			rawWeightInput.append(rawInput[1])

		for i in rawNodeInput:
			
			if distinct(i,tracked):
				tracked.append(i)
				next_jump.append(i)

		next_jump.pop(0)	
		masterNodeList.append(rawNodeInput)
		masterWeightList.append(rawWeightInput)

	source=int(input("\nNow enter source: "))

	print()
	print("___________________________________")
	print("Entered information:")
	print("Number of nodes:",n)
	print("Source:",source)
	print("Connections:",masterNodeList)
	print("weights:",masterWeightList)
	print("___________________________________")
	print()

	choice=input("Want to start inputting all over again? (y for 'yes', otherwise 'no')")

	if choice=='y':
		n,source,masterNodeList,masterWeightList=input_elements()

	return n,source,masterNodeList,masterWeightList

def find_min(x):

	"""

	Precondition: x is a list

	Finds the minimum value in a given list.

	"""

	minimum=infinity
	for i in x:
		if i<minimum:
			minimum=i

	return minimum

def empty_list(x):

	"""

	Preconditions: x is a list

	Checks if all the values in x are popped or not.
	If yes, then it returns True, otherwise False.

	"""

	global infinity
	global undefined

	condition=True
	for i in x:
		if i!="popped":
			condition=False
			return condition
	return condition

def distinct(a,b): # to check if a is in b or not
	
	"""

	Preconditions: b is a list

	Checks the presence of an element a in the list b.
	It returns True if a is absent in b, otherwise returns False (that a is already present in b)

	"""

	global infinity
	global undefined

	if a not in b:
		return True
	else:
		return False

def dijkstra(n,source,connections,weights):

	"""

	Preconditions: 	n is a whole number
			source is an integer
			connections is nested list
			weights is nested list
			connections and weights should have same dimensions
			weights are positive

	This functions calculates distances as per the Dijkstra algorithm and returns the list of calculated distances.

	"""
	
	Q=[]
	dist=[]

	for i in range(n):
		Q.append(i)
		dist.append(infinity)

	for i in range(len(Q)):
		if Q[i]==source:
			dist[i]=0

	sequence=Q[:]
	
	prev=[-1]
	visited=[]

	dist2=dist[:]

	while not empty_list(Q):

		index=dist.index(find_min(dist))

		if index>len(connections)-1:
			dist2[index]=dist[index]
			Q[index]="popped"
			dist[index]=infinity+1
			break


		child=connections[index]

		for j in range(len(child)):

				possible_dist=dist2[index]+weights[index][j]
				
				current_value=child[j]
				current_index=sequence.index(current_value)
				current_dist=dist2[current_index]

				if possible_dist<current_dist:
					dist[current_index]=possible_dist
					dist2[current_index]=possible_dist					

		Q[index]="popped"
		dist[index]=infinity+1

	for i in range(len(dist2)):
		if dist2[i]>=infinity:
			dist2[i]="infinity"

	if __name__ == '__main__':
		print("Nodes:",sequence)
	else:
		print("\t\tNodes:",sequence)

	return dist2

def bfs(n,source,connections,weights):

	"""

	Preconditions: 	n is a whole number
			source is an integer
			connections is nested list
			weights is nested list
			connections and weights should have same dimensions
			weights are positive

	This functions calculates distances as per the BFS algorithm and returns the list of calculated distances.

	"""

	Q=[source]
	visited=[source]

	sequence=[]
	dist=[]

	for i in range(n):
		sequence.append(i)
		dist.append(infinity)

	for i in range(len(sequence)):
		if sequence[i]==source:
			dist[i]=0

	while(len(Q)>0):
		jump=sequence.index(Q[0])

		if jump>len(connections)-1:
			Q.remove(Q[0])
			break

		for x in connections[jump]:


			if distinct(x,visited):
				Q.append(x)
				visited.append(x)

				curr_index=connections[jump].index(x)
				curr_index2=sequence.index(x)
				current_distance=dist[curr_index2]
				possible_distance=dist[jump]+weights[jump][curr_index]

				if possible_distance<current_distance:
					dist[curr_index2]=possible_distance

		Q.remove(Q[0])

	for i in range(len(dist)):
		if dist[i]>=infinity:
			dist[i]="infinity"

	if __name__ == '__main__':
		print("Nodes:",sequence)
	else:
		print("\t\tNodes:",sequence)
		
	return dist

if __name__ == '__main__':

	n,source,connections,weights=input_elements()

	print("Dijkstra:",dijkstra(n,source,connections,weights))
	print("BFS",bfs(n,source,connections,weights))