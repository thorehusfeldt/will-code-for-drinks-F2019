#!/usr/bin/env bash

PPATH=$(realpath ..)

. ../../testdata_tools/gen.sh

use_solution hybrid.py

compile gen_identicalbottles.py
compile gen_bitonic.py
compile gen_random.py
compile gen_messy.py

MAXNLARGE=100000
MAXN=1000000
MAXM=1000000000

samplegroup
limits n=10
sample 1

group group1 1
limits n=10
tc 1-tiny-identical0 gen_identicalbottles n=1 h=1 
tc 1-tiny-identical1 gen_identicalbottles n=1 h=$MAXM
tc 1-tiny-bitonic_uu gen_bitonic n=10 first=up second=up
tc 1-tiny-bitonic_ud gen_bitonic n=10 first=up second=down
tc 1-tiny-bitonic_du gen_bitonic n=10 first=down second=up
tc 1-tiny-bitonic_dd gen_bitonic n=10 first=down second=down
tc 1-tiny-random0 gen_random n=10
tc 1-tiny-random1 gen_random n=10
tc 1-messy gen_messy n=10

group group2 1
limits n=1000
include_group group1
tc 2-small-identical0 gen_identicalbottles n=1000 h=1
tc 2-small-identical1 gen_identicalbottles n=1000 h=$MAXM
tc 2-small-bitonic_uu gen_bitonic n=1000 first=up second=up
tc 2-small-bitonic_ud gen_bitonic n=1000 first=up second=down
tc 2-small-bitonic_du gen_bitonic n=1000 first=down second=up
tc 2-small-bitonic_dd gen_bitonic n=1000 first=down second=down
tc 2-small-random0 gen_random n=1000
tc 2-small-random1 gen_random n=1000
tc 2-small-random2 gen_random n=1000
tc 2-small-random3 gen_random n=1000
tc 2-messy gen_messy n=1000

group group3 3
limits n=$MAXNLARGE 
include_group group2
include_group group3
tc 3-large-identical0 gen_identicalbottles n=$MAXNLARGE h=1
tc 3-large-identical1 gen_identicalbottles n=$MAXNLARGE h=$MAXM
tc 3-large-bitonic_uu gen_bitonic n=$MAXNLARGE first=up second=up
tc 3-large-bitonic_ud gen_bitonic n=$MAXNLARGE first=up second=down
tc 3-large-bitonic_du gen_bitonic n=$MAXNLARGE first=down second=up
tc 3-large-bitonic_dd gen_bitonic n=$MAXNLARGE first=down second=down
tc 3-large-random0 gen_random n=$MAXNLARGE
tc 3-large-random1 gen_random n=$MAXNLARGE
tc 3-large-random2 gen_random n=$MAXNLARGE
tc 3-large-random3 gen_random n=$MAXNLARGE
tc 3-messy gen_messy n=$MAXNLARGE

group group4 1
tc 4-huge-bitonic_uu gen_bitonic n=$MAXN first=up second=up
tc 4-huge-bitonic_ud gen_bitonic n=$MAXN first=up second=down
tc 4-huge-bitonic_du gen_bitonic n=$MAXN first=down second=up
tc 4-huge-bitonic_dd gen_bitonic n=$MAXN first=down second=down
tc 4-huge-random0 gen_random n=$MAXN
tc 4-huge-random1 gen_random n=$MAXN
tc 4-messy gen_messy n=$MAXN
