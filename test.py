# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 
import math

a='\t\tThe The value of Inductance is: 2 H \n\t\tThe value of Capaciatnce is:0.00000507 uF \n\t\tThe vaue of resistance is 10 Ω'
print(a)

Inductance=  float (2)
Capacitance= float(0.00000507)
Resistance= float (10)


print("\n\n\n\t\tCalculating Resonance frequency, Bandwidth & Quality Factor ")


rf=1/((math.sqrt(Inductance))*(math.sqrt(Capacitance))*6.28)
s1='\n\t\tThe Value of the Resonance frequency is: '+repr(rf)
print(s1)

bw=Inductance/Capacitance
s2='\t\tThe Bandwidth of the circuit is: '+repr(bw)
print(s2)




qf=1/Resistance*(math.sqrt(bw))
pua='\t\tThe Value of Quality Factor is: '+repr(qf)
print(pua)

print("\t\t\nPress enter to see graph")
value=input("")


X = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
Y = [0.00318523,0.00637812,0.00958639,0.0128179,0.0160806,0.0193828,0.0227332,0.0261408,0.0296151,0.0331661,0.0368047,0.0405425,0.0443921,0.048367,0.0524823,0.0567545,0.0612016,0.0658439,0.070704,0.0758073,0.0811826,0.0868623,0.0928838,0.0992897,0.10613,0.113461,0.121351,0.129879,0.139139,0.149245,0.160333,0.17257,0.186162,0.201366,0.21851,0.23801,0.260417,0.286461,0.317138,0.353846,0.398604,0.454445,0.526143,0.621679,0.755483,0.956636,1.29402,1.98176,4.25753,7,4.42168,2.07889,1.38122,1.04056,0.837959,0.703424,0.6075,0.535605,0.479683,0.434924,0.398272,0.367695,0.341789,0.319551,0.300247,0.283328,0.268371,0.255051,0.243109,0.232339,0.222573,0.213676,0.205534,0.198053,0.191154,0.18477,0.178845,0.17333,0.168182,0.163365,0.158848,0.154601,0.150602,0.146828,0.14326,0.139882,0.136678,0.133634,0.130739,0.127981,0.125351,0.122839,0.120438,0.118139,0.115937,0.113825,0.111797,0.109849,0.107975,0.106171]
plt.plot(X,Y)
# Labeling the X-axis 
plt.xlabel('X-axis     Frequency (Hz) -->') 
# Labeling the Y-axis 
plt.ylabel('Y-axis       Current (A) -->') 
# Give a title to the graph
plt.title('Graph Between Current and Frequency in LCR circuit.') 
plt.show()
