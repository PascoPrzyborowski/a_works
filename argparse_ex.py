import argparse

parser = argparse.ArgumentParser(description="this is ma app")
parser.add_argument('--greeting', '-g', type=str)

args = parser.parse_args()

print('my proggi')