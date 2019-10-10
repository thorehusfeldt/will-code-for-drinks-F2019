#!/usr/bin/env bash

USE_SCORING=0
. ../../testdata_tools/gen.sh

use_solution sl.cpp

compile gen_random.py
compile gen_handcrafted.py

sample 1
sample 2

tc handcrafted-0  gen_handcrafted 0
tc handcrafted-1  gen_handcrafted 1
tc handcrafted-2  gen_handcrafted 2
tc handcrafted-3  gen_handcrafted 3
tc handcrafted-4  gen_handcrafted 4
tc handcrafted-5  gen_handcrafted 5
tc handcrafted-6  gen_handcrafted 6
tc handcrafted-7  gen_handcrafted 7
tc handcrafted-8  gen_handcrafted 8
tc handcrafted-9  gen_handcrafted 9
tc handcrafted-10 gen_handcrafted 10
tc handcrafted-11 gen_handcrafted 11
tc handcrafted-12 gen_handcrafted 12
tc handcrafted-13 gen_handcrafted 13
tc handcrafted-14 gen_handcrafted 14
tc handcrafted-15 gen_handcrafted 15
tc random-0 gen_random -L 11 -F 0 -W 10 -H 10 
tc random-1 gen_random -L 11 -F 1 -W 10 -H 10 
tc random-2 gen_random -L 10000 -F 0 -W 10 -H 10 
tc random-3 gen_random -L 10000 -F 9990 -W 10 -H 10 
tc random-4 gen_random -L 10000 -F 5000 -W 10 -H 10 
tc random-5 gen_random -L 10000 -F 5000 -W 3 -H 3
tc random-6 gen_random -L 5000 -F 2500 -W 200 -H 200
tc random-7 gen_random -L 5000 -F 0 -W 200 -H 200
tc random-8 gen_random -L 5000 -F 4800 -W 200 -H 200
tc random-9 gen_random -L 10000 -F 4800 -W 200 -H 200
