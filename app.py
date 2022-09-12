
from analizador.parser import parser

result = parser.parse('2 * 3\n + 4 * \n(5 - 4)\n / 23')

print(result)