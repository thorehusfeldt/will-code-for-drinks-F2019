#!/usr/bin/env bash

. ../../testdata_tools/gen.sh

use_solution hybrid.py

compile gen_identicalbottles.py
compile gen_bitonic.py
compile gen_random.py
compile gen_messy.py
compile gen_overflow.cpp

MAXN1=10
MAXN2=100
MAXN3=1000
MAXN4=10000
MAXN5=100000
MAXM=1000000000

samplegroup
limits n=10
sample 1

group group1 1
limits n=$MAXN1
tc 1
tc 1-tiny-identical0 gen_identicalbottles n=1 h=1 
tc 1-tiny-identical1 gen_identicalbottles n=1 h=$MAXM
tc 1-tiny-bitonic_uu gen_bitonic n=$MAXN1 first=up second=up
tc 1-tiny-bitonic_ud gen_bitonic n=$MAXN1 first=up second=down
tc 1-tiny-bitonic_du gen_bitonic n=$MAXN1 first=down second=up
tc 1-tiny-bitonic_dd gen_bitonic n=$MAXN1 first=down second=down
tc 1-tiny-random0 gen_random n=$MAXN1
tc 1-tiny-random1 gen_random n=$MAXN1
tc 1-tiny-messy gen_messy n=$MAXN1

group group2 1
limits n=$MAXN2
tc 2-small-identical0 gen_identicalbottles n=$MAXN2 h=1
tc 2-small-identical1 gen_identicalbottles n=$MAXN2 h=$MAXM
tc 2-small-bitonic_uu gen_bitonic n=$MAXN2 first=up second=up
tc 2-small-bitonic_ud gen_bitonic n=$MAXN2 first=up second=down
tc 2-small-bitonic_du gen_bitonic n=$MAXN2 first=down second=up
tc 2-small-bitonic_dd gen_bitonic n=$MAXN2 first=down second=down
tc 2-small-random0 gen_random n=$MAXN2
tc 2-small-random1 gen_random n=$MAXN2
tc 2-small-random2 gen_random n=$MAXN2
tc 2-small-random3 gen_random n=$MAXN2
tc 2-small-messy gen_messy n=$MAXN2

group group3 1
limits n=$MAXN3
tc 3-medium-identical0 gen_identicalbottles n=$MAXN3 h=1
tc 3-medium-identical1 gen_identicalbottles n=$MAXN3 h=$MAXM
tc 3-medium-bitonic_uu gen_bitonic n=$MAXN3 first=up second=up
tc 3-medium-bitonic_ud gen_bitonic n=$MAXN3 first=up second=down
tc 3-medium-bitonic_du gen_bitonic n=$MAXN3 first=down second=up
tc 3-medium-bitonic_dd gen_bitonic n=$MAXN3 first=down second=down
tc 3-medium-random0 gen_random n=$MAXN3
tc 3-medium-random1 gen_random n=$MAXN3
tc 3-medium-random2 gen_random n=$MAXN3
tc 3-medium-random3 gen_random n=$MAXN3
tc 3-medium-messy gen_messy n=$MAXN3
tc 3-overflow gen_overflow $MAXN3


group group4 1
limits n=$MAXN4
tc 4-large-identical0 gen_identicalbottles n=$MAXN4 h=1
tc 4-large-identical1 gen_identicalbottles n=$MAXN4 h=$MAXM
tc 4-large-bitonic_uu gen_bitonic n=$MAXN4 first=up second=up
tc 4-large-bitonic_ud gen_bitonic n=$MAXN4 first=up second=down
tc 4-large-bitonic_du gen_bitonic n=$MAXN4 first=down second=up
tc 4-large-bitonic_dd gen_bitonic n=$MAXN4 first=down second=down
tc 4-large-random0 gen_random n=$MAXN4
tc 4-large-random1 gen_random n=$MAXN4
tc 4-large-random2 gen_random n=$MAXN4
tc 4-large-random3 gen_random n=$MAXN4
tc 4-large-messy gen_messy n=$MAXN4
tc 4-overflow gen_overflow $MAXN4


group group5 1
limits n=$MAXN5
tc 5-huge-identical0 gen_identicalbottles n=$MAXN5 h=1
tc 5-huge-identical1 gen_identicalbottles n=$MAXN5 h=$MAXM
tc 5-huge-bitonic_uu gen_bitonic n=$MAXN5 first=up second=up
tc 5-huge-bitonic_ud gen_bitonic n=$MAXN5 first=up second=down
tc 5-huge-bitonic_du gen_bitonic n=$MAXN5 first=down second=up
tc 5-huge-bitonic_dd gen_bitonic n=$MAXN5 first=down second=down
tc 5-huge-random0 gen_random n=$MAXN5
tc 5-huge-random1 gen_random n=$MAXN5
tc 5-huge-random2 gen_random n=$MAXN5
tc 5-huge-random3 gen_random n=$MAXN5
tc 5-huge-messy gen_messy n=$MAXN5
tc 5-overflow gen_overflow $MAXN5

