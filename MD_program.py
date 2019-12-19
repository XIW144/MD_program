#This is my MD program!

# Making more changes.

import csv
import numpy as np
from random import random

# Define functions
def load_positions(filename):

 with open(filename,newline='') as csvfile:
  output_data = csv.reader(csvfile, delimiter="\t")
  output_data = list(output_data)

  positions_list = []
  for i in range(1,len(output_data)):
   row = output_data[i]
   temp_dict = {}
   temp_dict['num'] = i
   temp_dict['type'] = row[0]
   temp_dict['pos_vect'] = np.array([float(item) for item in row[1:4]])
   positions_list.append(temp_dict)
  return positions_list


# Define functions
def load_positions(filename):

 with open(filename,newline='') as csvfile:
  output_data = csv.reader(csvfile, delimiter="\t")
  output_data = list(output_data)

  positions_list = []
  for i in range(1,len(output_data)):
   row = output_data[i]
   temp_dict = {}
   temp_dict['num'] = i
   temp_dict['type'] = row[0]
   temp_dict['pos_vect'] = np.array([float(item) for item in row[1:4]])
   positions_list.append(temp_dict)
  return positions_list

load_positions("/ihome/cwilmer/xiw144/MD/test_pos.xyz")

import numpy as np

def load_position():
    return
def load_parameters():
    return
def initialize_MD():
    """
    takes in the temperature to define a set of initial velocity vectors.
    """
    return
def calculate_forces():
    """
    Evaluates Lennard-Jones potentials for all particles and assigns forces.
    Update later to include charge-charge interactions.
    """cc
    return
def integrate_forces():

    """
    use the calculate forces and the time step to update the position of the particles in the system.
    """

    return
def check_boundaries():
    """
    check if any particle has gone beyond the boundary, and if so update position through periodic boundary positions.
    """
    return

def run_MD(init_cycles, prod_cycles, position, parameters, temperature, r_cutoff):
    particels = load_positions
    parameters = load_parameters
    initialize_MD()

    for i in range(init_cycles):
        calculate_forces()
        integrate_forces()
        check_boundaries()

    for i in range(production_cycles):
        calculate_forces()
        integrate_forces()
        check_boundaries()

    return
# Exeute Program
init_cycles =100
prod_cycles =200
r_cutoff = 10
temperature =300
