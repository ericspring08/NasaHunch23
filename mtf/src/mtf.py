# Imports
# Prep

# Utility
import warnings
from art import text2art
import time

# Arg Parse
from argparse import ArgumentParser

# Import SubModules
from graph import graph
from loop import MTF
import builtins
from datetime import datetime

title = text2art("MTF", font="3d_diagonal")
print(title)
print("Model Training Platform")
print("By Eric Zhang, 2023")
print('-' * 100)
warnings.filterwarnings('ignore')
start_time = time.perf_counter()

# All prints have a timestamp
_print = print


def time_print(*args, **kwargs):
    curr_time = datetime.now().strftime("%H:%M:%S")
    _print(f"[{curr_time}]", *args, **kwargs)


builtins.print = time_print


# Experiment
def experiment(args):
    print(f"Running experiment {args.config}")
    mtf = MTF(args.config, args.dataset)
    mtf.run()
    print('-' * 100)


# Parser
parser = ArgumentParser(description="Prototype Training Platform")
subparsers = parser.add_subparsers(dest="command")

# Subcommand for analysis
parser_experiment = subparsers.add_parser(
    "experiment", help="Run an experiment")
parser_experiment.add_argument(
    "-c", "--config", help="Specify an experiment config file (.json) to run",
)
parser_experiment.add_argument(
    "-d", "--dataset", help="Specify a dataset to use")

parser_experiment.set_defaults(func=experiment)

parser_graph = subparsers.add_parser("graph", help="Analyze a results file")
parser_graph.add_argument("file", help="Specify a results file to analyze")
parser_graph.add_argument(
    "-o", "--output", help="Specify an output folder to save to")
parser_graph.add_argument(
    "-r", "--ranking", help="Generate ranking graphs", action="store_true")
parser_graph.add_argument(
    "-d", "--distribution", help="Generate distribution graphs", action="store_true")
parser_graph.set_defaults(func=graph)

args = parser.parse_args()

args.func(args)