slurm
=====

This role installs SLURM, the HPC cluster resource manager.

Things you should change:

- This role is dependent on the presence of a yum repo
  which contains the slurm packages. The easiest way to 
  do this (for me) is to have another role which sets up 
  the appropriate repo, and include it as a role dependency
  in meta/main.yml

- You need to have a file munge.key for cluster node
  authentication in files/munge.key. Run,

  dd bs=1 if=/dev/urandom count=1024 of=files/munge.key
