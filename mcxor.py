#make prediction with weights
def predict(row,weights):
	activation=0.0
	for i in range(len(row)-1):
		activation+=weights[i]*row[i]
	return 1.0 if activation>=1.0 else 0.0

#test predictions
d1=[[0,0,0],[0,1,0],[1,0,1],[1,1,0]]
w1=[1,-1]
print("Values of Z1")
for row in d1:
	z1=predict(row,w1)
	print("Expected_Z1=%d,Predicted_Z1=%d" %(row[-1],z1))

d2=[[0,0,0],[0,1,1],[1,0,0],[1,1,0]]
w2=[-1,1]
print("Values of Z2")
for row in d2:
	z2=predict(row,w2)
	print("Expected_Z2=%d,Predicted_Z2=%d" %(row[-1],z2))

dataset=[[0,0,0],[0,1,1],[1,0,1],[0,0,0]]
weights=[1,1]
print("Output of XOR")
for row in dataset:
	y=predict(row,weights)
	print("Expected_Y=%d,Predicted_Y=%d" %(row[-1],y))