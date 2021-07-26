# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:37:57 2021

@author: talha
"""

import matplotlib.pyplot as plt

class Tk_Visualize:
    
    def acc_val_graph(train_data,validation_data):
        fig, ax1 = plt.subplots()
        plt.title('Training and validation Accuracy')
        color = 'tab:red'
        ax1.set_xlabel('Epochs')
        ax1.set_ylabel('Training accuracy', color=color)
        ax1.plot(train_data, 'b',color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx() 

        color = 'tab:blue'
        ax2.set_xlabel('Epochs')
        ax2.set_ylabel('Validation accuracy', color=color)  
        ax2.plot(validation_data,'b' ,color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()  
        plt.show()