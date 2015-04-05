ansible-simple-slurm-cluster
============================

This repo contains a set of Ansible roles for setting up a relatively basic
HPC-style compute cluster, along with an example playbook for using them.

'''These scipts should not be considered production-quality!''' (Though
you can always use them or get inspiration from them if you like.) I use
the roles in this repo to set up ephemeral clusters while playing with new
ideas or writing software. I am rarely concerned with stability or user
experience, and more often with seeing what I can break. :) YMMV!

They have mostly been tested on EC2 but there's
nothing cloud-specific in them, so they should work on normal hardware.


So what does it do?
-------------------

- Set host names and builds an /etc/hosts file
- Configure [SLURM](http://slurm.schedmd.com) as resource manager
- NFS export of /home from head node to computes
- Syslog forwarding to the head node
- [Ganglia](http://ganglia.sourceforge.net/) monitoring system (not using multicast b/c mostly used on EC2)
- Install some common HPC dev tools

This is usually enough to get me started on whatever other project I'm working
on.


Prerequisites
-------------

- All the roles assume you're using EL6 (i.e. CentOS, RHEL, Scientific Linux)

- [SLURM](http://slurm.schedmd.com) and [Munge](https://code.google.com/p/munge/) 
  are not distributed as RPMs, so I built those RPMs and stuck
  them in a repository on S3. The "ajdecon-repo" role configures each node of
  the cluster to include this repo when installing software.
  
  The S3 bucket is not public because I like low bandwidth bills. :) The RPMs
  themselves are very easy to build, so I suggest just setting up your own
  YUM repo to install them from.


How do I use the playbook?
--------------------------

1. Set up an Ansible [inventory file](http://docs.ansible.com/intro_inventory.html)
   similar to the included hosts.test. Each host can have a "setname="
   parameter included next to it, and the "sethostname" role will use that
   to configure the hostname.

   Note that many of the roles assume your head node will be named "head", and
   that the "compute" and "cluster" groups exist. However this can generally be
   changed for each role: see the variables in `defaults/main.yml` for each one.

2. Run `ansible-playbook -i <inventory_file> cluster.yml` and wait for your
   cluster to be ready!


Other notes
-----------

Many of the roles have variables you can set to control their behavior. (For
example, there are a few knobs to turn on the "slurm" role.) You can change
their values by setting them in "config.yml" and they'll get picked up
in "cluster.yml". See the `defaults/main.yml` file in each role to see what
variables are available to change.


