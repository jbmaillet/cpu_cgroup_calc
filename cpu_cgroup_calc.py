#!/usr/bin/python3

import sys
import argparse

def percent_to_share(percent_list):
    percent_list = [percent for percent in percent_list if percent != 0]
    total_percent = sum(percent_list)
    if total_percent < 100:
        added_group_share_percent = 100 - total_percent
        print("Adding a group with {0}% of shares to reach mandatory 100%..."
              .format(added_group_share_percent))
        percent_list.append(added_group_share_percent)
    elif total_percent > 100:
        print("Total is {0}% cpu shares - reconsider your figures, we only have 100% CPU at best!"
              .format(total_percent))
        sys.exit(1) # TODO a cleaner way to do this
    percent_list.sort(reverse=True)
    one_percent_cpu_share = 1024 / percent_list[0]
    for share_percent in percent_list:
        print("Group with {0:3d}% of CPU shares should be setup with a 'cpu.shares' of {1:4d}"
              .format(share_percent,
                      int(share_percent * one_percent_cpu_share)))

def share_to_percent(share_list):
    share_list = [share for share in share_list if share != 0]
    total_share = sum(share_list)
    share_list.sort(reverse=True)
    for share in share_list:
        print("group with {0:4d} 'cpu.shares' have {1:3d}% of CPU shares"
              .format(share,
                      round((share / total_share) * 100)))

def main():
    parser = argparse.ArgumentParser(description="Compute cpu.shares values from a list of CPU %, and the reverse.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p2s",
                       "--percent_to_share",
                       help="from CPU %% to cpu.shares",
                       metavar='percent', type=int, nargs='+')
    group.add_argument("-s2p",
                       "--share_to_percent",
                       help="from cpu.shares to CPU %%",
                       metavar='share', type=int, nargs='+')
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
