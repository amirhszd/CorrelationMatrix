# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:58:50 2019

@author: Amirh

correlation matrix, collinearity problem

"""
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import interpolate
#%%
def correlation_plot(data):
    """
    data: is MxN numpy array where M is the number of samples and N is the 
    number of features per sample.
    
    """
    data = data.T
    ds = data.shape
    
    fig,ax = plt.subplots(nrows=ds[0], ncols=ds[0],figsize=(ds[0],ds[0]))
    
    # Changing the number of ticks per subplot
    for axi in ax.flat:
        axi.xaxis.set_major_locator(plt.MaxNLocator(2))
        axi.yaxis.set_major_locator(plt.MaxNLocator(2))                        
    
    # plotting each subplot             
    for i in range(ds[0]):
        for j in range(ds[0]):
            if i == j:
                # plotting histograms of each variable
                n, bins, patches=ax[i,j].hist(data[i],density=True)
                
                # plotting distribution function and using it to fit a gaussian
                mu, std = norm.fit(data[i])
                p = norm.pdf(bins, mu, std)
                ax[i,j].plot(bins, p, 'r--', linewidth=2)
                ax[i,j].set_xticks([])
                ax[i,j].set_yticks([])
                if j == ds[0]-1:
                    ax[i,j].set_ylabel("var_%s"%(i+1),fontsize=11).set_color("red")
                    ax[i,j].yaxis.set_label_position("right")
                
                if i == 0 and j == 0:
                    ax[i,j].set_title("var_%s"%(i+1),fontsize=11).set_color("red")
    
            elif i < j:
                prs=pearsonr(data[i],data[j])[0]
                if prs >= 0.5 or prs <= -0.5:
                    ax[i,j].text(0.5,0.5,str(prs)[0:4],fontsize=24,horizontalalignment='center',verticalalignment='center')                      
                    ax[i,j].text(0.8,0.8,"***",color='r',fontsize=16,horizontalalignment='center',verticalalignment='center')                      
                elif (prs <= -0.45 and prs >= -0.50) or (prs >= 0.45 and prs <= 0.50):
                    ax[i,j].text(0.5,0.5,str(prs)[0:4],fontsize=18,horizontalalignment='center',verticalalignment='center')                      
                    ax[i,j].text(0.8,0.8,"**",color='r',fontsize=16,horizontalalignment='center',verticalalignment='center')                      
                elif (prs <= -0.4 and prs > -0.45) or (prs >= 0.4 and prs < 0.45):
                    ax[i,j].text(0.5,0.5,str(prs)[0:4],fontsize=16,horizontalalignment='center',verticalalignment='center')                      
                    ax[i,j].text(0.8,0.8,"*",color='r',fontsize=16,horizontalalignment='center',verticalalignment='center')
                else:                    
                    ax[i,j].text(0.5,0.5,str(pearsonr(data[i],data[j])[0])[0:4],fontsize=10,horizontalalignment='center',verticalalignment='center')                      
    
                ax[i,j].set_xticks([])
                ax[i,j].set_yticks([])
    
                if i ==0:
                    ax[i,j].set_title("var_%s"%(j+1),fontsize=11).set_color("red")
                    ax[i,j].set_xticks([])
                    ax[i,j].set_yticks([])
                if j == ds[0]-1:
                    ax[i,j].set_ylabel("var_%s"%(i+1),fontsize=11).set_color("red")
                    ax[i,j].yaxis.set_label_position("right")
    
            elif i > j:
                ax[i,j].scatter(data[i],data[j],s=10,c='k')      
                rnge= data[i].max()-data[i].min()
                ax[i,j].set_ylim(-0.2*rnge,1.2*rnge)
                ax[i,j].set_xlim(-0.2*rnge,1.2*rnge)                      
                    
                if i!=0 and i!=ds[0]-1:
                    if j==0:
                        ax[i,j].set_xticks([])
                    elif j!=0:
                        ax[i,j].set_xticks([])
                        ax[i,j].set_yticks([])
                        
                if j!=0 and j!=ds[0]-1 and i==ds[0]-1:
                    ax[i,j].set_yticks([])
    
    plt.subplots_adjust(wspace=0, hspace=0)

    
