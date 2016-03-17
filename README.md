# cpu_cgroup_calc

A small Python utility for Linux cpu cgroup controller:

Compute cpu.shares values from a list of CPU %, and the reverse.

## Usage

	$ ./cpu_cgroup_calc.py
	usage: cpu_cgroup_calc.py [-h] [-p2s percent [percent ...] | -s2p share
	                          [share ...]]
	
	Compute cpu.shares values from a list of CPU %, and the reverse.
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -p2s percent [percent ...], --percent_to_share percent [percent ...]
	                        from CPU % to cpu.shares
	  -s2p share [share ...], --share_to_percent share [share ...]
	                        from cpu.shares to CPU %

## Sample outputs

	$ ./cpu_cgroup_calc.py -p2s 50 30 15 5
	group with 50% of CPU shares should be setup with a 'cpu.shares' of 1024
	group with 30% of CPU shares should be setup with a 'cpu.shares' of 614
	group with 15% of CPU shares should be setup with a 'cpu.shares' of 307
	group with 5% of CPU shares should be setup with a 'cpu.shares' of 102

	$ ./cpu_cgroup_calc.py -s2p 1024 614 307 102
	group with 1024 cpu.shares have 50% of CPU shares
	group with 614 cpu.shares have 30% of CPU shares
	group with 307 cpu.shares have 15% of CPU shares
	group with 102 cpu.shares have 5% of CPU shares

## About cgroups

https://www.kernel.org/doc/Documentation/cgroup-v2.txt

...or for older kernels:

https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt
