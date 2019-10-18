bottles 1 beverage = "1 bottle" ++ " of " ++ beverage
bottles n beverage = show n ++ " bottles " ++ " of " ++ beverage

firstline n beverage = bottles n beverage ++ " on the wall, " ++ bottles n beverage ++ ".\n"

secondline 1 beverage  = 
    "Take it down, pass it around, no more bottles of "++beverage++".\n"
secondline n beverage  = 
    "Take one down, pass it around, "  ++ bottles (n-1) beverage ++ " on the wall.\n"

verse n beverage = firstline n beverage ++ secondline n beverage

main  = do
    n    <- getLine
    let nn = read n :: Int
    bev  <- getLine
    
    mapM  ( \n -> putStrLn (verse n bev) ) [nn, nn-1 ..1]

