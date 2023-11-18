def gst(items,ui,gs,q):
	max = 0
	qwe = 0 
	for i in range(len(ui)):
		a = ui[i]*q[i]*gs[i]//100
		if(a>max):
			max = a
			qwe = i
	return items[qwe],max
	

def pay(ui,gs,q):
	ans = 0
	for i in range(len(ui)):
		if(ui[i]>=500):
			ans += ui[i]*q[i] + ui[i]*q[i]*gs[i]//100- ui[i]*q[i]*(5//100)
		else:
			ans += ui[i]*q[i] + ui[i]*q[i]*gs[i]//100 
	return ans

items = ["Leather Wallet","Umbrella","Cigarette","Honey"]
ui = [1100,900,200,100]
gs = [18,12,28,0]
q = [1,4,3,2]


print("Max GST : " ,gst(items,ui,gs,q))

print("Total amount to be paid : ",pay(ui,gs,q))