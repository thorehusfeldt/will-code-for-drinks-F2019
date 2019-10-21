import Data.List (sortBy)

main = do
	getLine
	contents <- getContents
	putStrLn (solve contents)

solve::String -> String
solve ls = (concat . sortBy smallestconcatenation) (map minimize (words ls))

smallestconcatenation:: String -> String -> Ordering
smallestconcatenation x y = compare (x++y) (y++x)

minimize::String -> String
minimize s = if turnable s then min s (turn s) else s

turnable::String -> Bool
turnable (x:xs) = x `elem` "01689" &&  turnable xs
turnable [] = True

turn::String -> String
turn (c:cs) = turn cs ++ [flip c]
	where flip '6' = '9'
	      flip '9' = '6'
	      flip c = c
turn [] = []

