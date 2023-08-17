putStrLn "Digite um número: "
numero1 <- getLine
putStrLn "Digite outro número: "
numero2 <- getLine
let resultado = read numero1 + read numero2 :: Int
putStrLn ("A soma é: " ++ show resultado)