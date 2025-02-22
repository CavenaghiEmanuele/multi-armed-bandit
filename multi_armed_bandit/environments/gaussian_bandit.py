import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from numpy.random import uniform, normal
from typing import List

from . import MultiArmedBandit


class GaussianBandit(MultiArmedBandit):

    _mean: List[float]
    _std_dev: List[float]

    def __init__(self, n_arms: int, mean: List[float] = None, std_dev: List[float] = None):

        super().__init__(n_arms)

        if mean == None:
            self._mean = [uniform(0, 1) for _ in range(n_arms)]
        elif mean != None and n_arms == len(mean):
            self._mean = mean
        elif mean != None and n_arms != len(mean):
            raise Exception(
                "Length of mean vector must be the same of number of arms")

        if std_dev == None:
            self._std_dev = [uniform(0.5, 0.9) for _ in range(n_arms)]
        elif isinstance(std_dev, float) or isinstance(std_dev, int):
            self._std_dev = [std_dev for _ in range(n_arms)]
        elif std_dev != None and n_arms == len(std_dev):
            self._std_dev = std_dev
        elif std_dev != None and n_arms != len(std_dev):
            raise Exception(
                "Length of standard deviation vector must be the same of number of arms")

        self._best_action = np.argmax(self._mean)

    def __repr__(self):
        return "Gaussian Multi-armed bandit\n" + \
            "Mean = " + str(self._mean) + \
            "\nStandard Deviation = " + str(self._std_dev)

    def plot_arms(self, render: bool = True):  
        plt.figure()
        for a in range(self._n_arms):
            x = np.linspace(self._mean[a] - 3*self._std_dev[a], self._mean[a] + 3*self._std_dev[a])
            plt.plot(x, 
                     stats.norm.pdf(x, self._mean[a], self._std_dev[a]), 
                     label="Action: " + str(a) + ", Mean: " + str(self._mean[a]) + ", std_dev: " + str(self._std_dev[a]))
        plt.suptitle("Bandit's arms values")
        plt.legend()
        if render:
            plt.show()

    def do_action(self, action: int):
        return normal(loc=self._mean[action], scale=self._std_dev[action])

    def best_action_mean(self):
        return self._mean[self._best_action]
    
    def get_best_action(self):
        return self._best_action

    def action_mean(self, action: int):
        return self._mean[action]
