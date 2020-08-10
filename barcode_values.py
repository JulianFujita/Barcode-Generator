# Code-128
from BarcodeValue import BarcodeValue

# Functional Characters
START = BarcodeValue('START', 103, '11010000100')
STOP = BarcodeValue('STOP', 106, '11000111010')

# Special Characters
EXCLAMATION = BarcodeValue('!', 1, '11001101100')
DOUBLE_QUOTE = BarcodeValue('"', 2, '11001100110')
HASHTAG = BarcodeValue('#', 3, '10010011000')
DOLLAR = BarcodeValue('$', 4, '10010001100')
PERCENT = BarcodeValue('%', 5, '10001001100')
AMPERSAND = BarcodeValue('&', 6, '10011001000')
SINGLE_QUOTE = BarcodeValue("'", 7, '10011000100')
LEFT_PARENTHESIS = BarcodeValue('(', 8, '10001100100')
RIGHT_PARENTHESIS = BarcodeValue(')', 9, '11001001000')
ASTERISK = BarcodeValue('*', 10, '11001000100')
PLUS = BarcodeValue('+', 11, '11000100100')
COMMA = BarcodeValue(',', 12, '10110011100')
HYPHEN = BarcodeValue('-', 13, '10011011100')
PERIOD = BarcodeValue('.', 14, '10011001110')
FORWARD_SLASH = BarcodeValue('/', 15, '10111001100')

COLON = BarcodeValue(':', 26, '11100100110')
SEMICOLON = BarcodeValue(';', 27, '11101100100')
LEFT_ANGLE_BRACKET = BarcodeValue('<', 28, '11100110100')
EQUAL = BarcodeValue('=', 29, '11100110010')
RIGHT_ANGLE_BRACKET = BarcodeValue('<', 30, '11011011000')
QUESTION_MARK = BarcodeValue('?', 31, '11011000110')
AT = BarcodeValue('@', 32, '11000110110')

LEFT_BRACKET = BarcodeValue('[', 59, '11100011010')
BACK_SLASH = BarcodeValue('\\', 60, '11101111010')
RIGHT_BRACKET = BarcodeValue(']', 61, '11001000010')
CARET = BarcodeValue('^', 62, '11110001010')
UNDERSCORE = BarcodeValue('_', 63, '10100110000')
BACK_TICK = BarcodeValue('`', 64, '10100001100')

LEFT_CURLY_BRACKET = BarcodeValue('{', 91, '11110110110')
PIPE = BarcodeValue('|', 92, '10101111000')
RIGHT_CURLY_BRACKET = BarcodeValue('}', 93, '10100011110')
TILDE = BarcodeValue('~', 94, '10001011110')

# Numerical Values
ZERO = BarcodeValue('0', 16, '10011101100')
ONE = BarcodeValue('1', 17, '10011100110')
TWO = BarcodeValue('2', 18, '11001110010')
THREE = BarcodeValue('3', 19, '11001011100')
FOUR = BarcodeValue('4', 20, '11001001110')
FIVE = BarcodeValue('5', 21, '11011100100')
SIX = BarcodeValue('6', 22, '11001110100')
SEVEN = BarcodeValue('7', 23, '11101101110')
EIGHT = BarcodeValue('8', 24, '11101001100')
NINE = BarcodeValue('9', 25, '11100101100')

# Letters
A_U = BarcodeValue('A', 33, '10100011000')
B_U = BarcodeValue('B', 34, '10001011000')
C_U = BarcodeValue('C', 35, '10001000110')
D_U = BarcodeValue('D', 36, '10110001000')
E_U = BarcodeValue('E', 37, '10001101000')
F_U = BarcodeValue('F', 38, '10001100010')
G_U = BarcodeValue('G', 39, '11010001000')
H_U = BarcodeValue('H', 40, '11000101000')
I_U = BarcodeValue('I', 41, '11000100010')
J_U = BarcodeValue('J', 42, '10110111000')
K_U = BarcodeValue('K', 43, '10110001110')
L_U = BarcodeValue('L', 44, '10001101110')
M_U = BarcodeValue('M', 45, '10111011000')
N_U = BarcodeValue('N', 46, '10111000110')
O_U = BarcodeValue('O', 47, '10001110110')
P_U = BarcodeValue('P', 48, '11101110110')
Q_U = BarcodeValue('Q', 49, '11010001110')
R_U = BarcodeValue('R', 50, '11000101110')
S_U = BarcodeValue('S', 51, '11011101000')
T_U = BarcodeValue('T', 52, '11011100010')
U_U = BarcodeValue('U', 53, '11011101110')
V_U = BarcodeValue('V', 54, '11101011000')
W_U = BarcodeValue('W', 55, '11101000110')
X_U = BarcodeValue('X', 56, '11100010110')
Y_U = BarcodeValue('Y', 57, '11101101000')
Z_U = BarcodeValue('Z', 58, '11101100010')

A_L = BarcodeValue('a', 65, '10010110000')
B_L = BarcodeValue('b', 66, '10010000110')
C_L = BarcodeValue('c', 67, '10000101100')
D_L = BarcodeValue('d', 68, '10000100110')
E_L = BarcodeValue('e', 69, '10110010000')
F_L = BarcodeValue('f', 70, '10110000100')
G_L = BarcodeValue('g', 71, '10011010000')
H_L = BarcodeValue('h', 72, '10011000010')
I_L = BarcodeValue('i', 73, '10000110100')
J_L = BarcodeValue('j', 74, '10000110010')
K_L = BarcodeValue('k', 75, '11000010010')
L_L = BarcodeValue('l', 76, '11001010000')
M_L = BarcodeValue('m', 77, '11110111010')
N_L = BarcodeValue('n', 78, '11000010100')
O_L = BarcodeValue('o', 79, '10001111010')
P_L = BarcodeValue('p', 80, '10100111100')
Q_L = BarcodeValue('q', 81, '10010111100')
R_L = BarcodeValue('r', 82, '10010011110')
S_L = BarcodeValue('s', 83, '10111100100')
T_L = BarcodeValue('t', 84, '10011110100')
U_L = BarcodeValue('u', 85, '10011110010')
V_L = BarcodeValue('v', 86, '11110100100')
W_L = BarcodeValue('w', 87, '11110010100')
X_L = BarcodeValue('x', 88, '11110010010')
Y_L = BarcodeValue('y', 89, '11011011110')
Z_L = BarcodeValue('z', 90, '11011110110')

