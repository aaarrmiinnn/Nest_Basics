# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:53:55 2016

@author: Armin
"""

import numpy as np
import nest
import pylab

neuron = nest.Create("iaf_neuron")
multimeter = nest.Create("multimeter")
nest.SetStatus(neuron, {"I_e": 376.0})

nest.SetStatus(multimeter, {"withtime":True,"record_from":["V_m"]})

spikedetector = nest.Create("spike_detector", params={"withgid":True, "withtime": True})

nest.Connect(multimeter, neuron)
nest.Connect(neuron, spikedetector)

Armin = nest.Simulate(1000.0)

dmm = nest.GetStatus(multimeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]
