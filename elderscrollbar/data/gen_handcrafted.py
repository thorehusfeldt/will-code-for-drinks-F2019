import sys

i = int(sys.argv[1])

edgecase = []
edgecase.append('10 3 0 1\nxyxyxyxyx x xyxyxyxyx z')
edgecase.append('10 3 0 1\nxyxyxyxyxy x xyxyxyxyxy z')
edgecase.append('10 3 0 1\nxyxyxyxyxy xyxyxyxy x xyxyxyxy x z')
edgecase.append('10 3 0 1\nxyxyxyxyxy xyxyxyxyxy x xyxyxyxy z')
edgecase.append('10 3 0 1\nxyxyxyxyxy xyxyxyxy x xyxyxyxy zz')
edgecase.append('3 3 0 1\nxya xyb xyc xyd xye')
edgecase.append('3 3 1 1\nxya xyb xyc xyd xye')
edgecase.append('3 3 2 1\nxya xyb xyc xyd xye')
edgecase.append('3 5 0 1\nxyx xyx xyx xyx xyx xyx xyx')
edgecase.append('3 5 1 1\nxya xyb xyc xyd xye xyf xyg')
edgecase.append('3 5 2 1\nxya xyb xyc xyd xye xyf xyg')
edgecase.append('8 6 0 1\nLorem ipsum dolor sit amet consectetur adipisicing elit sed do')
edgecase.append('8 6 2 1\nLorem ipsum dolor sit amet consectetur adipisicing elit sed do')
edgecase.append('3 3 1 5\nx\nxxxxxxxxxxx\nx\nxxxxxxxxxxx\nx')
edgecase.append('3 3 0 1\nx xy x zz')
edgecase.append('200 200 0 10000\n' +  '\n'.join(['xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy']*10000))
edgecase.append('200 200 0 10000\n' +  '\n'.join(['x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x'] * 10000))

print(edgecase[i])
