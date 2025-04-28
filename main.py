#Subplots practise
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
x=np.arange(100)
#koto ta subplots dorkar 
fig, axs=plt.subplots(2,2)#2,2 means row and column

axs[0,0].plot(x,np.sin(x))
axs[0,0].set_title("Sin Wave")

axs[0,1].plot(x,np.cos(x))
axs[0,1].set_title("Cosine wave")

axs[1,0].plot(x,np.random.random(100))
axs[1,0].set_title("Random Function")

axs[1,1].plot(x,np.log(x))
axs[1,1].set_title("Log Function")
axs[1,1].set_xlabel("Test")
plt.tight_layout()
plt.suptitle("Four Waves")
#subplots save method
plt.savefig("plots.png", transparent=False, dpi=720,bbox_inches="tight")
plt.show()
