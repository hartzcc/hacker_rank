#%%
import numpy as np
import matplotlib.pyplot as plt

def test_plot():
    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)



#%%
def wrapper(f):
    def fun(l):
        f(l)
        return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


#%%
if __name__ == '__main__':

    N = 3
    i1 = '07895462130'
    i2 = '919875641230'
    i3 = '9195969878'
    l = [int(i1), int(i2), int(i3)]

# %%
test_plot()

# %%
