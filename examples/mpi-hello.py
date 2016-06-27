#!/usr/bin/env python
from mpi4py import MPI
import socket

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
hostname = socket.gethostname()

print "Hello from process %d of %d on %s" % (rank, size, hostname)
