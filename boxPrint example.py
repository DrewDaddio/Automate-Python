# Raise And Assert
# Create a box printing function


def boxPrint(symbol, width, height):
             print(symbol * width)

             for i in range(height - 2):
                 print(symbol + (' ' * (width - 2)) + symbol)

             print(symbol * width)

boxPrint('*', 10, 5)
