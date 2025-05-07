Typewrite comes with two functions. The first is slowPrint(). It prints the given message one character at a time and its parameters are msg, and delay. Msg is what will be printed, delay is the delay between every character. Delay is optional, and by default will be set to 0.2 seconds.

The second function is special. It simply adds variables to your project so you can more easily print Unicode character without having to google the unicode. Every single unicode symbol that is not displayed on a key on your keyboard, and is listed on https://www.rapidtables.com/ has been added, including inverted exclamation marks, copyright signs, and accented letters. The full list of variable names and unicodes can be seen below.

If you want to import only one of the functions, or only one of the variables from special, you can do so with:
from typewrite.special import <variable name>, <variable name>
from typewrite import <function>



inverted_exclamation = u"\u00A1"<br>
cent_sign = u"\u00A2"<br>
pound_sign = u"\u00A3"<br>
currency_sign = u"\u00A4"<br>
yen_sign = u"\u00A5"<br>
broken_bar = u"\u00A6"<br>
section_sign = u"\u00A7"<br>
umlaut = u"\u00a8"<br>
copyright_sign = u"\u00a9"<br>
ordinal_a = u"\u00aa"<br>
left_double_arrow = u"\u00ab"<br>
formal_negation_symbol = u"\u00ac"<br>
blank_space = u"\u00ad"<br>
registered = u"\u00ae"<br>
top_underscore = u"\u00af"<br>
hollow_bullet_point = u"\u00b0"<br>
plus_minus_sign = u"\u00b1"<br>
superscript_2 = u"\u00b2"<br>
superscript_3 = u"\u00b3"<br>
accent_mark = u"\u00b4"<br>
mu = u"\u00b5"<br>
space_symbol = u"\u00b6"<br>
center_dot = u"\u00b7"<br>
curly_comma = u"\u00b8"<br>
superscript_1 = "\u00b9"<br>
superscipt_0 = u"\u00ba"<br>
right_double_arrow = u"\u00bb"<br>
one_fourth = u"\u00bc"<br>
one_half = u"\u00bd"<br>
three_fourths = u"\u00be"<br>
inverted_question = u"\u00bf"<br>
left_accent_a = u"\u00c0"<br>
right_accent_a = u"\u00c1"<br>
circumflex_a = u"\u00c2"<br>
tilda_a = u"\u00c3"<br>
umlaut_a = u"\u00c4"<br>
overdot_a = u"\u00c5"<br>
ae_compound = u"\u00c6"<br>
undercomma_c = u"\u00c7"<br>
left_accent_e = u"\u00c8"<br>
right_accent_e = u"\u00c9"<br>
circumflex_e = u"\u00ca"<br>
umlaut_e = u"\u00cb"<br>
left_accent_i = u"\u00cc"<br>
right_accent_i = u"\u00cd"<br>
circumflex_i = u"\u00ce"<br>
umlaut_i = u"\u00cf"<br>
eth = u"\u00d0"<br>
tilda_n = u"\u00d1"<br>
left_accent_o = u"\u00d2"<br>
right_accent_o = u"\u00d3"<br>
circumflex_o = u"\u00d4"<br>
tilda_o = u"\u00d5"<br>
umlaut_o = u"\u00d6"<br>
multiplication = u"\u00d7"<br>
slashed_o = u"\u00d8"<br>
left_accent_u = u"\u00d9"<br>
right_accent_u = u"\u00da"<br>
circumflex_u = u"\u00db"<br>
umlaut_u = u"\u00dc"<br>
right_accent_y = u"\u00dd"<br>
thorn = u"\u00de"<br>
double_s = u"\u00df"<br>
left_accent_a_lowercase = u"\u00e0"<br>
right_accent_a_lowercase = u"\u00e1"<br>
circumflex_a_lowercase = u"\u00e2"<br>
tilda_a_lowercase = u"\u00e3"<br>
umlaut_a_lowercase = u"\u00e4"<br>
overdot_a_lowercase = u"\u00e5"<br>
ae_compound_lowercase = u"\u00e6"<br>
undercomma_c_lowercase = u"\u00e7"<br>
left_accent_e_lowercase = u"\u00e8"<br>
right_accent_e_lowercase = u"\u00e9"<br>
circumflex_e_lowercase = u"\u00ea"<br>
umlaut_e_lowercase = u"\u00eb"<br>
left_accent_i_lowercase = u"\u00ec"<br>
right_accent_i_lowecase = u"\u00ed"<br>
circumflex_i_lowercase = u"\u00ee"<br>
umlaut_i_lowercase = u"\u00ef"<br>
eth_lowercase = u"\u00f0"<br>
tilda_n = u"\u00f1"<br>
left_accent_o_lowercase = u"\u00f2"<br>
right_accent_o_lowercase = u"\u00f3"<br>
circumflex_o_lowercase = u"\u00f4"<br>
tilda_o_lowercase = u"\u00f5"<br>
umlaut_o_lowercase = u"\u00f6"<br>
division_sign = u"\u00f7"<br>
slashed_o_lowercase = u"\u00f8"<br>
left_accent_u_lowercase u"\u00f9"<br>
right_accent_u_lowercase = u"\u00fa"<br>
circumflex_u_lowercase = u"\u00fb"<br>
umlaut_u_lowercase = u"\u00fc"<br>
right_accent_y_lowercase = u"\u00fd"<br>
thorn_lowercase = u"\u00fe"<br>
umlaut_y_lowercase = u"\u00ff"<br>
