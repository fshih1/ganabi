# This script is meant as an end to end, data creator, trainer, and evaluater.
# It is set up so that the tasks within can easily be done manually as well,
# by splitting up the tasts into separate scripts/modules.

#import statements
from utils import parse_args, dir_utils
import create_load_data
import train
#import evaluate
import tensorflow as tf
import keras


def main():
    args = parse_args.parse()
    args = dir_utils.resolve_run_directory(args)

    #create/load data
    loader = create_load_data.main(args)

    #train model/load model
    model = train.main(loader, args)

    #evaluate model
    evaluate.main(data, model, args)

if __name__ == "__main__":
    main()
