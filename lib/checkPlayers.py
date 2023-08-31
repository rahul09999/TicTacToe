def Players(userInput):
    userTemp = userInput[1:len(userInput)-1]
    userList = []
    ValidateSymbol = []
    ValidateUserId = []
    symbols = "XO#@$%&ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbolsToAssign = 0
    isComputer = False
    i = 0
    while i < len(userTemp):
        # handling computer case

        if isComputer == True:
            if userTemp[i] == "C":
                return "Error: Computer can't be more than one"
        if userTemp[i] == "C":
            isComputer = True
            if userTemp[i+1] != "C":
                return "Error: Computer's symbol should be 'C'"
            elif userTemp[i+1] == "C":
                userList.append([userTemp[i], userTemp[i+1]])
                ValidateSymbol.append(userTemp[i+1])
                i += 2
                continue
            elif i+1 == len(userTemp):
                userList.append([userTemp[i], userTemp[i+1]])
                ValidateSymbol.append(userTemp[i+1])
                return userList
            
        if len(userTemp[i]) == 1:
            return "Error: User Id should be more than one character, for example 'u1', 'u2' etc."
        
        if i+1 != len(userTemp) and len(userTemp[i+1]) == 1 and userTemp[i+1] != "C":
            userList.append([userTemp[i], userTemp[i+1]])
            ValidateSymbolUnique(userTemp[i+1], ValidateSymbol)
            ValidateUserIdUnique(userTemp[i], ValidateUserId)
            i = i + 2
            continue
        else:
            while True:
                # handling if symbol not provided
                if( symbols[symbolsToAssign] not in ValidateSymbol
                   or symbols[symbolsToAssign] not in userTemp ):
                    userList.append([userTemp[i], symbols[symbolsToAssign]])
                    sumbolsToAssign += 1
                    break
                symbolsToAssign += 1

            # Check for unique symbol
            ValidateSymbolUnique(symbols[symbolsToAssign], ValidateSymbol)
            # check for unique userId
            ValidateUserIdUnique(userTemp[i], ValidateUserId)
            i = i + 1
            continue

    return userList



def ValidateSymbolUnique(symbol, ValidateSymbol):
    if symbol not in ValidateSymbol:
        ValidateSymbol.append(symbol)
    else:
        return "Error: Symbol should be unique for each player"
    
def ValidateUserIdUnique(userId, ValidateUserId):
    if userId not in ValidateUserId:
        ValidateUserId.append(userId)
    else:
        return "Error: User Id should be unique for each player"