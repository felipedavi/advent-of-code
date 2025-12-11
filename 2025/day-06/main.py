#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


"""Advent of Code 2025
    Day 6
    Trash Compactor
	Part 1
"""

def part1(items):
    total = 0
    for column in items:
        numbers, symbols = [],[]
        
        for elem  in column:
            if elem .isdigit():
                numbers.append(int(elem))
            else:
                symbols.append(elem )
                
        if not symbols or not numbers:
            continue

        op = symbols[0]
        
        
        result = numbers[0]
        for n in numbers[1:]:
            if op == '+':
                result += n
            else:
                result *= n
        total += result
    return total

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.strip().split() for line in lines]
    items = list(zip(*lines))
    return items

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    return result, elapsed_time

def main():
    print('Advent of Code 2025 - Day 6')
    values = read_file('input.txt')
    
    print("Part 1: ", end="")
    total, elapsed_time = measure_time(part1, values)
    print(f'This {total} is a grand total of individual problems. ({elapsed_time:.8f} seconds)')

if __name__ == '__main__':
    main()
