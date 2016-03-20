#!/usr/bin/python3

import sys
import argparse

def percent_to_share(percent_list):
    total_percent = sum(percent_list)
    if total_percent < 100:
        added_group_share_percent = 100 - total_percent
        print("Adding a group with {0}% of shares to reach mandatory 100%..."
              .format(added_group_share_percent))
        percent_list.append(added_group_share_percent)
    elif total_percent > 100:
        print("Total is {0}% cpu shares - reconsider your figures, we only have 100% CPU at best!"
              .format(total_percent))
        sys.exit(1)
    percent_list.sort(reverse=True)
    one_percent_cpu_share = 1024 / percent_list[0]
    for share_percent in percent_list:
        print("Group with {0:3d}% of CPU shares should be setup with a 'cpu.shares' of {1:4d}"
              .format(share_percent,
                      int(share_percent * one_percent_cpu_share)))

def share_to_percent(share_list):
    total_share = sum(share_list)
    share_list.sort(reverse=True)
    for share in share_list:
        print("group with {0:4d} 'cpu.shares' have {1:3d}% of CPU shares"
              .format(share,
                      round((share / total_share) * 100)))

def strictly_positive_integer(value):
    error_msg = "'%s' is not a positive integer value" % value
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(error_msg)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(error_msg)
    return ivalue

def main():
    parser = argparse.ArgumentParser(description="Compute cgroup cpu.shares values from a list of CPU %, and the reverse.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p2s",
                       "--percent_to_share",
                       help="from CPU %% to cpu.shares",
                       metavar='percent',
                       type=strictly_positive_integer,
                       nargs='+')
    group.add_argument("-s2p",
                       "--share_to_percent",
                       help="from cpu.shares to CPU %%",
                       metavar='share',
                       type=strictly_positive_integer,
                       nargs='+')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    if args.percent_to_share:
        percent_to_share(args.percent_to_share)
    if args.share_to_percent:
        share_to_percent(args.share_to_percent)
    sys.exit(0)

if __name__ == "__main__":
    main()
