from fx import x2, lnx, mb1
import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
# %matplotlib inline
from ipywidgets import interact, interactive, fixed
from bokeh import Scatter

def i1():
    n = 1000
    vec_x = np.linspace(0,1,n)
    vec_r = np.linspace(2.8,3.4,n)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    xn = []
    rn = []
    for x in vec_x:
        print(x)

        for r in vec_r:
            xn0 = mb1(x, r, 20)
            rn.append(r)
            xn.append(xn0)
            # print(r)
            
    rn = np.asarray(rn)
    xn = np.asarray(xn)

    plt.scatter(rn, xn, s=1, marker="o")
    plt.show()
    plt.savefig("img_matplotlib.png", dpi=100)
    pass




if __name__ =="__main__":
    i1()
    

