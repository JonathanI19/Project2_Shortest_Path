import sys
import subprocess

# print("Number of arguments:", len(sys.argv), 'arguments.')
# print("Argument list:", str(sys.argv))

if (len(sys.argv) > 1):
  algorithm = sys.argv[1]

process = subprocess.run(['python', sys.argv[1]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

output = process.stdout.decode()
key_value_list = output.replace('\r', '').split('\n')
key_value_list.reverse()

for key_value_pair in key_value_list:
  try:
    split_key_value_pair = key_value_pair.split(',')
    startingX = split_key_value_pair[0].replace('(', '')
    startingY = split_key_value_pair[1].replace(')', '').replace(' ', '')

    targetX = split_key_value_pair[2].replace('(', '')
    targetY = split_key_value_pair[3].replace(')','').replace(' ', '')

    print(f"{startingX},{startingY} to {targetX},{targetY}")
  except:
    continue


