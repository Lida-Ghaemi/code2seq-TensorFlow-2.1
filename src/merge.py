import argparse

from data_set_merge import DataSetMerge
from pathlib import Path


def main():
    args_parser = argparse.ArgumentParser(
        description='merge resources generated by cppminer to a code2seq dataset')

    args_parser.add_argument('DataPath',
                             metavar='path',
                             type=str,
                             help='the dataset sources path')

    args_parser.add_argument('-c', '--clear_resources',
                             metavar='clear_resources_flag',
                             type=bool,
                             help='if True clear resource files',
                             default=False,
                             required=False)

    args_parser.add_argument('-m', '--map_size',
                             metavar='map_file_size',
                             type=int,
                             help='size of the DB file, default(6442450944 bytes)',
                             default=100000000000,
                             required=False)

    args = args_parser.parse_args()

    output_path = Path(args.DataPath).resolve().as_posix()
    print('Path: ' + output_path)

    map_size = args.map_size
    print('Map size: ' + str(map_size))

    print('Clear resources: ' + str(args.clear_resources))

    # shuffle and merge samples
    print("Merging samples ...")
    merge = DataSetMerge(output_path, map_size)
    merge.merge(args.clear_resources)
    print("Dumping datasets ...")
    merge.dump_datasets(0.7)
    print("Merging done")


if __name__ == '__main__':
    main()
