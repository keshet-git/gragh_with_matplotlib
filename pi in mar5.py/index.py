import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(4, 4), dpi=100)

# 1st
#---------------------------------------------------------------------------------------
sizes1 = [78, 15, 7]
colors1 = ['#e6ccff', '#b366ff', '#cc99ff'] 
explode1 = (0, 0.1, 0)
labels1 = '78%  Na Na Na Na', '15%  Hey Jude', '7%   Other words'

patches1, texts = axes[0,0].pie(sizes1, colors=colors1, explode=explode1, startangle=90)
axes[0,0].legend(patches1, labels1, loc=(-2,0), fontsize=12)
axes[0,0].set_title("Breakdown of Lyrics\nto \"Hey Jude\"", fontsize=12)
axes[0,0].set_aspect('equal')


#2nd
#---------------------------------------------------------------------------------------
sizes2 = [20, 74, 6]
colors2 = ['#9fdfbf', '#339966', '#79d2a6']
explode2 = (0.1, 0, 0)
labels2 = '20%  To Get Some', '74%  To Get Lucky', '6%   For Good Fun'

patches2, texts = axes[0,1].pie(sizes2, colors=colors2, explode=explode2, startangle=90)
axes[0,1].legend(patches2, labels2, loc=(1, 0), fontsize=12)
axes[0,1].set_title("Reasons we're up\nall night", fontsize=12)
axes[0,1].set_aspect('equal')


#3rd
#---------------------------------------------------------------------------------------
sizes3 = [100, 0, 0, 0]
colors3 = ['#ff99dd', '#ff66cc', '#ff33bb', '#cc0088']
labels3 = '100% You', '0%    Presents', '0%    To hang my stocking', '0%    Snow'

patches3, texts = axes[1,0].pie(sizes3, colors=colors3, startangle=90)
axes[1,0].legend(patches3, labels3, loc=(-2, 0), fontsize=12)
axes[1,0].set_title("What I want for Christmas", fontsize=12)
axes[1,0].set_aspect('equal')


#4th
#---------------------------------------------------------------------------------------
sizes4 = [5, 95]
colors4 = ['#e6f2ff', '#3399ff']
labels4 = '5%  EHHH MACARENA!', '95%  wjfsklfjsmljasedfjzena'

patches4, texts = axes[1,1].pie(sizes4, colors=colors4, startangle=90)
axes[1,1].legend(patches4, labels4, loc=(1, 0), fontsize=12)
axes[1,1].set_title("Macarena", fontsize=12)
axes[1,1].set_aspect('equal')

fig.suptitle("Graphs of Songs", y=1.1, fontsize=16)
plt.show()