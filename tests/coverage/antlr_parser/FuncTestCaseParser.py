# Generated from FuncTestCaseParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,120,577,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,
        52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,
        59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,
        65,2,66,7,66,1,0,1,0,4,0,137,8,0,11,0,12,0,138,1,0,1,0,1,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,157,8,3,10,3,12,
        3,160,9,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,172,8,5,1,
        5,1,5,1,5,1,6,3,6,178,8,6,1,6,4,6,181,8,6,11,6,12,6,182,1,6,3,6,
        186,8,6,1,6,4,6,189,8,6,11,6,12,6,190,3,6,193,8,6,1,7,1,7,1,7,5,
        7,198,8,7,10,7,12,7,201,9,7,1,8,1,8,3,8,205,8,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,225,
        8,9,1,10,1,10,1,10,1,10,1,10,3,10,232,8,10,1,10,1,10,1,10,1,11,1,
        11,1,11,1,11,3,11,241,8,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,249,
        8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,258,8,11,1,12,1,12,
        1,12,1,12,1,12,1,12,5,12,266,8,12,10,12,12,12,269,9,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,5,13,279,8,13,10,13,12,13,282,9,13,
        3,13,284,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        5,15,296,8,15,10,15,12,15,299,9,15,3,15,301,8,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,315,8,16,1,17,
        1,17,1,17,5,17,320,8,17,10,17,12,17,323,9,17,1,18,1,18,1,18,5,18,
        328,8,18,10,18,12,18,331,9,18,1,19,1,19,1,19,1,19,3,19,337,8,19,
        1,20,1,20,1,20,1,20,3,20,343,8,20,1,21,1,21,1,21,3,21,348,8,21,1,
        22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,
        25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,
        29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,
        32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,
        35,1,35,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,
        38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,5,
        41,428,8,41,10,41,12,41,431,9,41,3,41,433,8,41,1,41,1,41,1,42,1,
        42,3,42,439,8,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,
        43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,43,458,8,43,1,44,1,44,1,
        45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,3,50,474,
        8,50,1,50,1,50,1,50,1,50,3,50,480,8,50,1,51,1,51,3,51,484,8,51,1,
        51,1,51,1,51,1,51,1,52,1,52,3,52,492,8,52,1,52,1,52,1,52,1,52,1,
        53,1,53,3,53,500,8,53,1,53,1,53,1,53,1,53,1,54,1,54,3,54,508,8,54,
        1,54,1,54,1,54,1,54,1,54,1,54,3,54,516,8,54,1,55,1,55,3,55,520,8,
        55,1,55,1,55,1,55,1,55,1,56,1,56,3,56,528,8,56,1,56,1,56,1,56,1,
        56,1,57,1,57,3,57,536,8,57,1,57,1,57,1,57,1,57,1,58,1,58,1,58,1,
        58,1,58,1,58,1,58,3,58,549,8,58,1,59,1,59,1,60,1,60,1,61,1,61,1,
        61,1,61,1,62,1,62,1,63,1,63,1,64,1,64,1,64,5,64,566,8,64,10,64,12,
        64,569,9,64,1,65,1,65,1,66,1,66,3,66,575,8,66,1,66,0,0,67,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,
        94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,
        128,130,132,0,21,1,0,3,4,2,0,17,17,25,25,1,0,52,55,1,0,56,57,2,0,
        51,51,78,78,2,0,58,58,79,79,2,0,59,59,80,80,2,0,60,60,81,81,2,0,
        61,61,82,82,2,0,64,64,83,83,2,0,65,65,84,84,2,0,70,70,88,88,2,0,
        71,71,89,89,2,0,72,72,90,90,2,0,67,67,85,85,2,0,68,68,86,86,2,0,
        69,69,87,87,1,0,9,10,3,0,11,12,20,21,119,119,5,0,13,19,22,22,26,
        26,43,43,119,119,2,0,22,22,115,116,597,0,134,1,0,0,0,2,142,1,0,0,
        0,4,145,1,0,0,0,6,150,1,0,0,0,8,161,1,0,0,0,10,163,1,0,0,0,12,192,
        1,0,0,0,14,194,1,0,0,0,16,204,1,0,0,0,18,224,1,0,0,0,20,226,1,0,
        0,0,22,257,1,0,0,0,24,259,1,0,0,0,26,274,1,0,0,0,28,287,1,0,0,0,
        30,291,1,0,0,0,32,314,1,0,0,0,34,316,1,0,0,0,36,324,1,0,0,0,38,336,
        1,0,0,0,40,342,1,0,0,0,42,347,1,0,0,0,44,349,1,0,0,0,46,351,1,0,
        0,0,48,355,1,0,0,0,50,359,1,0,0,0,52,363,1,0,0,0,54,367,1,0,0,0,
        56,371,1,0,0,0,58,375,1,0,0,0,60,379,1,0,0,0,62,383,1,0,0,0,64,387,
        1,0,0,0,66,391,1,0,0,0,68,395,1,0,0,0,70,399,1,0,0,0,72,403,1,0,
        0,0,74,407,1,0,0,0,76,411,1,0,0,0,78,415,1,0,0,0,80,419,1,0,0,0,
        82,423,1,0,0,0,84,438,1,0,0,0,86,457,1,0,0,0,88,459,1,0,0,0,90,461,
        1,0,0,0,92,463,1,0,0,0,94,465,1,0,0,0,96,467,1,0,0,0,98,469,1,0,
        0,0,100,471,1,0,0,0,102,481,1,0,0,0,104,489,1,0,0,0,106,497,1,0,
        0,0,108,505,1,0,0,0,110,517,1,0,0,0,112,525,1,0,0,0,114,533,1,0,
        0,0,116,548,1,0,0,0,118,550,1,0,0,0,120,552,1,0,0,0,122,554,1,0,
        0,0,124,558,1,0,0,0,126,560,1,0,0,0,128,562,1,0,0,0,130,570,1,0,
        0,0,132,574,1,0,0,0,134,136,3,2,1,0,135,137,3,12,6,0,136,135,1,0,
        0,0,137,138,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,140,1,0,
        0,0,140,141,5,0,0,1,141,1,1,0,0,0,142,143,3,4,2,0,143,144,3,6,3,
        0,144,3,1,0,0,0,145,146,5,2,0,0,146,147,7,0,0,0,147,148,5,111,0,
        0,148,149,5,6,0,0,149,5,1,0,0,0,150,151,5,2,0,0,151,152,5,5,0,0,
        152,153,5,111,0,0,153,158,5,44,0,0,154,155,5,110,0,0,155,157,5,44,
        0,0,156,154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,
        0,0,159,7,1,0,0,0,160,158,1,0,0,0,161,162,5,7,0,0,162,9,1,0,0,0,
        163,164,3,132,66,0,164,165,5,106,0,0,165,166,3,14,7,0,166,171,5,
        107,0,0,167,168,5,108,0,0,168,169,3,128,64,0,169,170,5,109,0,0,170,
        172,1,0,0,0,171,167,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,
        174,5,99,0,0,174,175,3,16,8,0,175,11,1,0,0,0,176,178,3,8,4,0,177,
        176,1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,181,3,10,5,0,180,
        179,1,0,0,0,181,182,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,
        193,1,0,0,0,184,186,3,8,4,0,185,184,1,0,0,0,185,186,1,0,0,0,186,
        188,1,0,0,0,187,189,3,20,10,0,188,187,1,0,0,0,189,190,1,0,0,0,190,
        188,1,0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,192,177,1,0,0,0,192,
        185,1,0,0,0,193,13,1,0,0,0,194,199,3,18,9,0,195,196,5,110,0,0,196,
        198,3,18,9,0,197,195,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,
        200,1,0,0,0,200,15,1,0,0,0,201,199,1,0,0,0,202,205,3,18,9,0,203,
        205,3,120,60,0,204,202,1,0,0,0,204,203,1,0,0,0,205,17,1,0,0,0,206,
        225,3,46,23,0,207,225,3,48,24,0,208,225,3,50,25,0,209,225,3,54,27,
        0,210,225,3,56,28,0,211,225,3,52,26,0,212,225,3,58,29,0,213,225,
        3,60,30,0,214,225,3,62,31,0,215,225,3,64,32,0,216,225,3,66,33,0,
        217,225,3,68,34,0,218,225,3,70,35,0,219,225,3,72,36,0,220,225,3,
        74,37,0,221,225,3,76,38,0,222,225,3,78,39,0,223,225,3,80,40,0,224,
        206,1,0,0,0,224,207,1,0,0,0,224,208,1,0,0,0,224,209,1,0,0,0,224,
        210,1,0,0,0,224,211,1,0,0,0,224,212,1,0,0,0,224,213,1,0,0,0,224,
        214,1,0,0,0,224,215,1,0,0,0,224,216,1,0,0,0,224,217,1,0,0,0,224,
        218,1,0,0,0,224,219,1,0,0,0,224,220,1,0,0,0,224,221,1,0,0,0,224,
        222,1,0,0,0,224,223,1,0,0,0,225,19,1,0,0,0,226,231,3,22,11,0,227,
        228,5,108,0,0,228,229,3,128,64,0,229,230,5,109,0,0,230,232,1,0,0,
        0,231,227,1,0,0,0,231,232,1,0,0,0,232,233,1,0,0,0,233,234,5,99,0,
        0,234,235,3,16,8,0,235,21,1,0,0,0,236,237,3,24,12,0,237,238,3,132,
        66,0,238,240,5,106,0,0,239,241,3,34,17,0,240,239,1,0,0,0,240,241,
        1,0,0,0,241,242,1,0,0,0,242,243,5,107,0,0,243,258,1,0,0,0,244,245,
        3,26,13,0,245,246,3,132,66,0,246,248,5,106,0,0,247,249,3,36,18,0,
        248,247,1,0,0,0,248,249,1,0,0,0,249,250,1,0,0,0,250,251,5,107,0,
        0,251,258,1,0,0,0,252,253,3,132,66,0,253,254,5,106,0,0,254,255,3,
        28,14,0,255,256,5,107,0,0,256,258,1,0,0,0,257,236,1,0,0,0,257,244,
        1,0,0,0,257,252,1,0,0,0,258,23,1,0,0,0,259,260,5,8,0,0,260,261,5,
        119,0,0,261,262,5,106,0,0,262,267,3,84,42,0,263,264,5,110,0,0,264,
        266,3,84,42,0,265,263,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,
        268,1,0,0,0,268,270,1,0,0,0,269,267,1,0,0,0,270,271,5,107,0,0,271,
        272,5,99,0,0,272,273,3,26,13,0,273,25,1,0,0,0,274,283,5,106,0,0,
        275,280,3,30,15,0,276,277,5,110,0,0,277,279,3,30,15,0,278,276,1,
        0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,280,281,1,0,0,0,281,284,1,
        0,0,0,282,280,1,0,0,0,283,275,1,0,0,0,283,284,1,0,0,0,284,285,1,
        0,0,0,285,286,5,107,0,0,286,27,1,0,0,0,287,288,3,30,15,0,288,289,
        5,93,0,0,289,290,3,84,42,0,290,29,1,0,0,0,291,300,5,106,0,0,292,
        297,3,32,16,0,293,294,5,110,0,0,294,296,3,32,16,0,295,293,1,0,0,
        0,296,299,1,0,0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,301,1,0,0,
        0,299,297,1,0,0,0,300,292,1,0,0,0,300,301,1,0,0,0,301,302,1,0,0,
        0,302,303,5,107,0,0,303,31,1,0,0,0,304,315,5,43,0,0,305,315,3,42,
        21,0,306,315,5,26,0,0,307,315,5,44,0,0,308,315,5,30,0,0,309,315,
        5,29,0,0,310,315,5,28,0,0,311,315,5,27,0,0,312,315,5,41,0,0,313,
        315,5,42,0,0,314,304,1,0,0,0,314,305,1,0,0,0,314,306,1,0,0,0,314,
        307,1,0,0,0,314,308,1,0,0,0,314,309,1,0,0,0,314,310,1,0,0,0,314,
        311,1,0,0,0,314,312,1,0,0,0,314,313,1,0,0,0,315,33,1,0,0,0,316,321,
        3,38,19,0,317,318,5,110,0,0,318,320,3,38,19,0,319,317,1,0,0,0,320,
        323,1,0,0,0,321,319,1,0,0,0,321,322,1,0,0,0,322,35,1,0,0,0,323,321,
        1,0,0,0,324,329,3,40,20,0,325,326,5,110,0,0,326,328,3,40,20,0,327,
        325,1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,330,1,0,0,0,330,
        37,1,0,0,0,331,329,1,0,0,0,332,333,5,119,0,0,333,334,5,114,0,0,334,
        337,5,45,0,0,335,337,3,18,9,0,336,332,1,0,0,0,336,335,1,0,0,0,337,
        39,1,0,0,0,338,339,5,45,0,0,339,340,5,93,0,0,340,343,3,84,42,0,341,
        343,3,18,9,0,342,338,1,0,0,0,342,341,1,0,0,0,343,41,1,0,0,0,344,
        348,5,24,0,0,345,348,5,23,0,0,346,348,3,44,22,0,347,344,1,0,0,0,
        347,345,1,0,0,0,347,346,1,0,0,0,348,43,1,0,0,0,349,350,7,1,0,0,350,
        45,1,0,0,0,351,352,5,43,0,0,352,353,5,93,0,0,353,354,3,84,42,0,354,
        47,1,0,0,0,355,356,5,23,0,0,356,357,5,93,0,0,357,358,7,2,0,0,358,
        49,1,0,0,0,359,360,3,42,21,0,360,361,5,93,0,0,361,362,7,3,0,0,362,
        51,1,0,0,0,363,364,3,42,21,0,364,365,5,93,0,0,365,366,3,108,54,0,
        366,53,1,0,0,0,367,368,5,26,0,0,368,369,5,93,0,0,369,370,3,88,44,
        0,370,55,1,0,0,0,371,372,5,44,0,0,372,373,5,93,0,0,373,374,3,90,
        45,0,374,57,1,0,0,0,375,376,5,30,0,0,376,377,5,93,0,0,377,378,5,
        62,0,0,378,59,1,0,0,0,379,380,5,29,0,0,380,381,5,93,0,0,381,382,
        5,63,0,0,382,61,1,0,0,0,383,384,5,28,0,0,384,385,5,93,0,0,385,386,
        3,94,47,0,386,63,1,0,0,0,387,388,5,27,0,0,388,389,5,93,0,0,389,390,
        3,96,48,0,390,65,1,0,0,0,391,392,5,41,0,0,392,393,5,93,0,0,393,394,
        3,98,49,0,394,67,1,0,0,0,395,396,5,42,0,0,396,397,5,93,0,0,397,398,
        3,100,50,0,398,69,1,0,0,0,399,400,5,44,0,0,400,401,5,93,0,0,401,
        402,3,102,51,0,402,71,1,0,0,0,403,404,5,44,0,0,404,405,5,93,0,0,
        405,406,3,104,52,0,406,73,1,0,0,0,407,408,5,44,0,0,408,409,5,93,
        0,0,409,410,3,106,53,0,410,75,1,0,0,0,411,412,5,28,0,0,412,413,5,
        93,0,0,413,414,3,110,55,0,414,77,1,0,0,0,415,416,5,27,0,0,416,417,
        5,93,0,0,417,418,3,112,56,0,418,79,1,0,0,0,419,420,3,82,41,0,420,
        421,5,93,0,0,421,422,3,114,57,0,422,81,1,0,0,0,423,432,5,108,0,0,
        424,429,3,32,16,0,425,426,5,110,0,0,426,428,3,32,16,0,427,425,1,
        0,0,0,428,431,1,0,0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,433,1,
        0,0,0,431,429,1,0,0,0,432,424,1,0,0,0,432,433,1,0,0,0,433,434,1,
        0,0,0,434,435,5,109,0,0,435,83,1,0,0,0,436,439,3,86,43,0,437,439,
        3,116,58,0,438,436,1,0,0,0,438,437,1,0,0,0,439,85,1,0,0,0,440,458,
        3,88,44,0,441,458,5,52,0,0,442,458,5,53,0,0,443,458,5,54,0,0,444,
        458,5,55,0,0,445,458,5,56,0,0,446,458,5,57,0,0,447,458,3,90,45,0,
        448,458,3,92,46,0,449,458,3,94,47,0,450,458,3,96,48,0,451,458,5,
        62,0,0,452,458,5,63,0,0,453,458,3,98,49,0,454,458,5,66,0,0,455,456,
        5,77,0,0,456,458,5,119,0,0,457,440,1,0,0,0,457,441,1,0,0,0,457,442,
        1,0,0,0,457,443,1,0,0,0,457,444,1,0,0,0,457,445,1,0,0,0,457,446,
        1,0,0,0,457,447,1,0,0,0,457,448,1,0,0,0,457,449,1,0,0,0,457,450,
        1,0,0,0,457,451,1,0,0,0,457,452,1,0,0,0,457,453,1,0,0,0,457,454,
        1,0,0,0,457,455,1,0,0,0,458,87,1,0,0,0,459,460,7,4,0,0,460,89,1,
        0,0,0,461,462,7,5,0,0,462,91,1,0,0,0,463,464,7,6,0,0,464,93,1,0,
        0,0,465,466,7,7,0,0,466,95,1,0,0,0,467,468,7,8,0,0,468,97,1,0,0,
        0,469,470,7,9,0,0,470,99,1,0,0,0,471,473,7,10,0,0,472,474,5,112,
        0,0,473,472,1,0,0,0,473,474,1,0,0,0,474,479,1,0,0,0,475,476,5,39,
        0,0,476,477,3,118,59,0,477,478,5,40,0,0,478,480,1,0,0,0,479,475,
        1,0,0,0,479,480,1,0,0,0,480,101,1,0,0,0,481,483,7,11,0,0,482,484,
        5,112,0,0,483,482,1,0,0,0,483,484,1,0,0,0,484,485,1,0,0,0,485,486,
        5,39,0,0,486,487,3,118,59,0,487,488,5,40,0,0,488,103,1,0,0,0,489,
        491,7,12,0,0,490,492,5,112,0,0,491,490,1,0,0,0,491,492,1,0,0,0,492,
        493,1,0,0,0,493,494,5,39,0,0,494,495,3,118,59,0,495,496,5,40,0,0,
        496,105,1,0,0,0,497,499,7,13,0,0,498,500,5,112,0,0,499,498,1,0,0,
        0,499,500,1,0,0,0,500,501,1,0,0,0,501,502,5,39,0,0,502,503,3,118,
        59,0,503,504,5,40,0,0,504,107,1,0,0,0,505,507,7,14,0,0,506,508,5,
        112,0,0,507,506,1,0,0,0,507,508,1,0,0,0,508,515,1,0,0,0,509,510,
        5,39,0,0,510,511,3,118,59,0,511,512,5,110,0,0,512,513,3,118,59,0,
        513,514,5,40,0,0,514,516,1,0,0,0,515,509,1,0,0,0,515,516,1,0,0,0,
        516,109,1,0,0,0,517,519,7,15,0,0,518,520,5,112,0,0,519,518,1,0,0,
        0,519,520,1,0,0,0,520,521,1,0,0,0,521,522,5,39,0,0,522,523,3,118,
        59,0,523,524,5,40,0,0,524,111,1,0,0,0,525,527,7,16,0,0,526,528,5,
        112,0,0,527,526,1,0,0,0,527,528,1,0,0,0,528,529,1,0,0,0,529,530,
        5,39,0,0,530,531,3,118,59,0,531,532,5,40,0,0,532,113,1,0,0,0,533,
        535,5,75,0,0,534,536,5,112,0,0,535,534,1,0,0,0,535,536,1,0,0,0,536,
        537,1,0,0,0,537,538,5,39,0,0,538,539,3,84,42,0,539,540,5,40,0,0,
        540,115,1,0,0,0,541,549,3,102,51,0,542,549,3,104,52,0,543,549,3,
        106,53,0,544,549,3,108,54,0,545,549,3,100,50,0,546,549,3,110,55,
        0,547,549,3,112,56,0,548,541,1,0,0,0,548,542,1,0,0,0,548,543,1,0,
        0,0,548,544,1,0,0,0,548,545,1,0,0,0,548,546,1,0,0,0,548,547,1,0,
        0,0,549,117,1,0,0,0,550,551,5,23,0,0,551,119,1,0,0,0,552,553,7,17,
        0,0,553,121,1,0,0,0,554,555,3,124,62,0,555,556,5,111,0,0,556,557,
        3,126,63,0,557,123,1,0,0,0,558,559,7,18,0,0,559,125,1,0,0,0,560,
        561,7,19,0,0,561,127,1,0,0,0,562,567,3,122,61,0,563,564,5,110,0,
        0,564,566,3,122,61,0,565,563,1,0,0,0,566,569,1,0,0,0,567,565,1,0,
        0,0,567,568,1,0,0,0,568,129,1,0,0,0,569,567,1,0,0,0,570,571,7,20,
        0,0,571,131,1,0,0,0,572,575,3,130,65,0,573,575,5,119,0,0,574,572,
        1,0,0,0,574,573,1,0,0,0,575,133,1,0,0,0,43,138,158,171,177,182,185,
        190,192,199,204,224,231,240,248,257,267,280,283,297,300,314,321,
        329,336,342,347,429,432,438,457,473,479,483,491,499,507,515,519,
        527,535,548,567,574
    ]

class FuncTestCaseParser ( Parser ):

    grammarFileName = "FuncTestCaseParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'###'", "'SUBSTRAIT_SCALAR_TEST'", 
                     "'SUBSTRAIT_AGGREGATE_TEST'", "'SUBSTRAIT_INCLUDE'", 
                     "<INVALID>", "<INVALID>", "'DEFINE'", "'<!ERROR>'", 
                     "'<!UNDEFINED>'", "'OVERFLOW'", "'ROUNDING'", "'ERROR'", 
                     "'SATURATE'", "'SILENT'", "'TIE_TO_EVEN'", "'NAN'", 
                     "'ACCEPT_NULLS'", "'IGNORE_NULLS'", "'NULL_HANDLING'", 
                     "'SPACES_ONLY'", "'TRUNCATE'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'P'", "'T'", "'Y'", "'M'", 
                     "'D'", "'H'", "'S'", "'F'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'null'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'IF'", "'THEN'", "'ELSE'", 
                     "'BOOLEAN'", "'I8'", "'I16'", "'I32'", "'I64'", "'FP32'", 
                     "'FP64'", "'STRING'", "'BINARY'", "'TIMESTAMP'", "'TIMESTAMP_TZ'", 
                     "'DATE'", "'TIME'", "'INTERVAL_YEAR'", "'INTERVAL_DAY'", 
                     "'UUID'", "'DECIMAL'", "'PRECISION_TIMESTAMP'", "'PRECISION_TIMESTAMP_TZ'", 
                     "'FIXEDCHAR'", "'VARCHAR'", "'FIXEDBINARY'", "'STRUCT'", 
                     "'NSTRUCT'", "'LIST'", "'MAP'", "'U!'", "'BOOL'", "'STR'", 
                     "'VBIN'", "'TS'", "'TSTZ'", "'IYEAR'", "'IDAY'", "'DEC'", 
                     "'PTS'", "'PTSTZ'", "'FCHAR'", "'VCHAR'", "'FBIN'", 
                     "'ANY'", "<INVALID>", "'::'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'='", "'!='", "'>='", "'<='", "'>'", 
                     "'<'", "'!'", "'('", "')'", "'['", "']'", "','", "':'", 
                     "'?'", "'#'", "'.'", "'AND'", "'OR'", "':='" ]

    symbolicNames = [ "<INVALID>", "Whitespace", "TripleHash", "SubstraitScalarTest", 
                      "SubstraitAggregateTest", "SubstraitInclude", "FormatVersion", 
                      "DescriptionLine", "Define", "ErrorResult", "UndefineResult", 
                      "Overflow", "Rounding", "Error", "Saturate", "Silent", 
                      "TieToEven", "NaN", "AcceptNulls", "IgnoreNulls", 
                      "NullHandling", "SpacesOnly", "Truncate", "IntegerLiteral", 
                      "DecimalLiteral", "FloatLiteral", "BooleanLiteral", 
                      "TimestampTzLiteral", "TimestampLiteral", "TimeLiteral", 
                      "DateLiteral", "PeriodPrefix", "TimePrefix", "YearPrefix", 
                      "MSuffix", "DaySuffix", "HourSuffix", "SecondSuffix", 
                      "FractionalSecondSuffix", "OAngleBracket", "CAngleBracket", 
                      "IntervalYearLiteral", "IntervalDayLiteral", "NullLiteral", 
                      "StringLiteral", "ColumnName", "LineComment", "BlockComment", 
                      "If", "Then", "Else", "Boolean", "I8", "I16", "I32", 
                      "I64", "FP32", "FP64", "String", "Binary", "Timestamp", 
                      "Timestamp_TZ", "Date", "Time", "Interval_Year", "Interval_Day", 
                      "UUID", "Decimal", "Precision_Timestamp", "Precision_Timestamp_TZ", 
                      "FixedChar", "VarChar", "FixedBinary", "Struct", "NStruct", 
                      "List", "Map", "UserDefined", "Bool", "Str", "VBin", 
                      "Ts", "TsTZ", "IYear", "IDay", "Dec", "PTs", "PTsTZ", 
                      "FChar", "VChar", "FBin", "Any", "AnyVar", "DoubleColon", 
                      "Plus", "Minus", "Asterisk", "ForwardSlash", "Percent", 
                      "Eq", "Ne", "Gte", "Lte", "Gt", "Lt", "Bang", "OParen", 
                      "CParen", "OBracket", "CBracket", "Comma", "Colon", 
                      "QMark", "Hash", "Dot", "And", "Or", "Assign", "Number", 
                      "Identifier", "Newline" ]

    RULE_doc = 0
    RULE_header = 1
    RULE_version = 2
    RULE_include = 3
    RULE_testGroupDescription = 4
    RULE_testCase = 5
    RULE_testGroup = 6
    RULE_arguments = 7
    RULE_result = 8
    RULE_argument = 9
    RULE_aggFuncTestCase = 10
    RULE_aggFuncCall = 11
    RULE_tableData = 12
    RULE_tableRows = 13
    RULE_dataColumn = 14
    RULE_columnValues = 15
    RULE_literal = 16
    RULE_qualifiedAggregateFuncArgs = 17
    RULE_aggregateFuncArgs = 18
    RULE_qualifiedAggregateFuncArg = 19
    RULE_aggregateFuncArg = 20
    RULE_numericLiteral = 21
    RULE_floatLiteral = 22
    RULE_nullArg = 23
    RULE_intArg = 24
    RULE_floatArg = 25
    RULE_decimalArg = 26
    RULE_booleanArg = 27
    RULE_stringArg = 28
    RULE_dateArg = 29
    RULE_timeArg = 30
    RULE_timestampArg = 31
    RULE_timestampTzArg = 32
    RULE_intervalYearArg = 33
    RULE_intervalDayArg = 34
    RULE_fixedCharArg = 35
    RULE_varCharArg = 36
    RULE_fixedBinaryArg = 37
    RULE_precisionTimestampArg = 38
    RULE_precisionTimestampTZArg = 39
    RULE_listArg = 40
    RULE_literalList = 41
    RULE_dataType = 42
    RULE_scalarType = 43
    RULE_booleanType = 44
    RULE_stringType = 45
    RULE_binaryType = 46
    RULE_timestampType = 47
    RULE_timestampTZType = 48
    RULE_intervalYearType = 49
    RULE_intervalDayType = 50
    RULE_fixedCharType = 51
    RULE_varCharType = 52
    RULE_fixedBinaryType = 53
    RULE_decimalType = 54
    RULE_precisionTimestampType = 55
    RULE_precisionTimestampTZType = 56
    RULE_listType = 57
    RULE_parameterizedType = 58
    RULE_numericParameter = 59
    RULE_substraitError = 60
    RULE_funcOption = 61
    RULE_optionName = 62
    RULE_optionValue = 63
    RULE_funcOptions = 64
    RULE_nonReserved = 65
    RULE_identifier = 66

    ruleNames =  [ "doc", "header", "version", "include", "testGroupDescription", 
                   "testCase", "testGroup", "arguments", "result", "argument", 
                   "aggFuncTestCase", "aggFuncCall", "tableData", "tableRows", 
                   "dataColumn", "columnValues", "literal", "qualifiedAggregateFuncArgs", 
                   "aggregateFuncArgs", "qualifiedAggregateFuncArg", "aggregateFuncArg", 
                   "numericLiteral", "floatLiteral", "nullArg", "intArg", 
                   "floatArg", "decimalArg", "booleanArg", "stringArg", 
                   "dateArg", "timeArg", "timestampArg", "timestampTzArg", 
                   "intervalYearArg", "intervalDayArg", "fixedCharArg", 
                   "varCharArg", "fixedBinaryArg", "precisionTimestampArg", 
                   "precisionTimestampTZArg", "listArg", "literalList", 
                   "dataType", "scalarType", "booleanType", "stringType", 
                   "binaryType", "timestampType", "timestampTZType", "intervalYearType", 
                   "intervalDayType", "fixedCharType", "varCharType", "fixedBinaryType", 
                   "decimalType", "precisionTimestampType", "precisionTimestampTZType", 
                   "listType", "parameterizedType", "numericParameter", 
                   "substraitError", "funcOption", "optionName", "optionValue", 
                   "funcOptions", "nonReserved", "identifier" ]

    EOF = Token.EOF
    Whitespace=1
    TripleHash=2
    SubstraitScalarTest=3
    SubstraitAggregateTest=4
    SubstraitInclude=5
    FormatVersion=6
    DescriptionLine=7
    Define=8
    ErrorResult=9
    UndefineResult=10
    Overflow=11
    Rounding=12
    Error=13
    Saturate=14
    Silent=15
    TieToEven=16
    NaN=17
    AcceptNulls=18
    IgnoreNulls=19
    NullHandling=20
    SpacesOnly=21
    Truncate=22
    IntegerLiteral=23
    DecimalLiteral=24
    FloatLiteral=25
    BooleanLiteral=26
    TimestampTzLiteral=27
    TimestampLiteral=28
    TimeLiteral=29
    DateLiteral=30
    PeriodPrefix=31
    TimePrefix=32
    YearPrefix=33
    MSuffix=34
    DaySuffix=35
    HourSuffix=36
    SecondSuffix=37
    FractionalSecondSuffix=38
    OAngleBracket=39
    CAngleBracket=40
    IntervalYearLiteral=41
    IntervalDayLiteral=42
    NullLiteral=43
    StringLiteral=44
    ColumnName=45
    LineComment=46
    BlockComment=47
    If=48
    Then=49
    Else=50
    Boolean=51
    I8=52
    I16=53
    I32=54
    I64=55
    FP32=56
    FP64=57
    String=58
    Binary=59
    Timestamp=60
    Timestamp_TZ=61
    Date=62
    Time=63
    Interval_Year=64
    Interval_Day=65
    UUID=66
    Decimal=67
    Precision_Timestamp=68
    Precision_Timestamp_TZ=69
    FixedChar=70
    VarChar=71
    FixedBinary=72
    Struct=73
    NStruct=74
    List=75
    Map=76
    UserDefined=77
    Bool=78
    Str=79
    VBin=80
    Ts=81
    TsTZ=82
    IYear=83
    IDay=84
    Dec=85
    PTs=86
    PTsTZ=87
    FChar=88
    VChar=89
    FBin=90
    Any=91
    AnyVar=92
    DoubleColon=93
    Plus=94
    Minus=95
    Asterisk=96
    ForwardSlash=97
    Percent=98
    Eq=99
    Ne=100
    Gte=101
    Lte=102
    Gt=103
    Lt=104
    Bang=105
    OParen=106
    CParen=107
    OBracket=108
    CBracket=109
    Comma=110
    Colon=111
    QMark=112
    Hash=113
    Dot=114
    And=115
    Or=116
    Assign=117
    Number=118
    Identifier=119
    Newline=120

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(FuncTestCaseParser.HeaderContext,0)


        def EOF(self):
            return self.getToken(FuncTestCaseParser.EOF, 0)

        def testGroup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.TestGroupContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.TestGroupContext,i)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_doc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoc" ):
                listener.enterDoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoc" ):
                listener.exitDoc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoc" ):
                return visitor.visitDoc(self)
            else:
                return visitor.visitChildren(self)




    def doc(self):

        localctx = FuncTestCaseParser.DocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_doc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.header()
            self.state = 136 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 135
                self.testGroup()
                self.state = 138 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194688) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & 9729) != 0)):
                    break

            self.state = 140
            self.match(FuncTestCaseParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def version(self):
            return self.getTypedRuleContext(FuncTestCaseParser.VersionContext,0)


        def include(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IncludeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader" ):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = FuncTestCaseParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.version()
            self.state = 143
            self.include()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TripleHash(self):
            return self.getToken(FuncTestCaseParser.TripleHash, 0)

        def Colon(self):
            return self.getToken(FuncTestCaseParser.Colon, 0)

        def FormatVersion(self):
            return self.getToken(FuncTestCaseParser.FormatVersion, 0)

        def SubstraitScalarTest(self):
            return self.getToken(FuncTestCaseParser.SubstraitScalarTest, 0)

        def SubstraitAggregateTest(self):
            return self.getToken(FuncTestCaseParser.SubstraitAggregateTest, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_version

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersion" ):
                listener.enterVersion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersion" ):
                listener.exitVersion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersion" ):
                return visitor.visitVersion(self)
            else:
                return visitor.visitChildren(self)




    def version(self):

        localctx = FuncTestCaseParser.VersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_version)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(FuncTestCaseParser.TripleHash)
            self.state = 146
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 147
            self.match(FuncTestCaseParser.Colon)
            self.state = 148
            self.match(FuncTestCaseParser.FormatVersion)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TripleHash(self):
            return self.getToken(FuncTestCaseParser.TripleHash, 0)

        def SubstraitInclude(self):
            return self.getToken(FuncTestCaseParser.SubstraitInclude, 0)

        def Colon(self):
            return self.getToken(FuncTestCaseParser.Colon, 0)

        def StringLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.StringLiteral)
            else:
                return self.getToken(FuncTestCaseParser.StringLiteral, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.Comma)
            else:
                return self.getToken(FuncTestCaseParser.Comma, i)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_include

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclude" ):
                listener.enterInclude(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclude" ):
                listener.exitInclude(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude" ):
                return visitor.visitInclude(self)
            else:
                return visitor.visitChildren(self)




    def include(self):

        localctx = FuncTestCaseParser.IncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_include)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(FuncTestCaseParser.TripleHash)
            self.state = 151
            self.match(FuncTestCaseParser.SubstraitInclude)
            self.state = 152
            self.match(FuncTestCaseParser.Colon)
            self.state = 153
            self.match(FuncTestCaseParser.StringLiteral)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==110:
                self.state = 154
                self.match(FuncTestCaseParser.Comma)
                self.state = 155
                self.match(FuncTestCaseParser.StringLiteral)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestGroupDescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DescriptionLine(self):
            return self.getToken(FuncTestCaseParser.DescriptionLine, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_testGroupDescription

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestGroupDescription" ):
                listener.enterTestGroupDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestGroupDescription" ):
                listener.exitTestGroupDescription(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestGroupDescription" ):
                return visitor.visitTestGroupDescription(self)
            else:
                return visitor.visitChildren(self)




    def testGroupDescription(self):

        localctx = FuncTestCaseParser.TestGroupDescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_testGroupDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(FuncTestCaseParser.DescriptionLine)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.functionName = None # IdentifierContext

        def OParen(self):
            return self.getToken(FuncTestCaseParser.OParen, 0)

        def arguments(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ArgumentsContext,0)


        def CParen(self):
            return self.getToken(FuncTestCaseParser.CParen, 0)

        def Eq(self):
            return self.getToken(FuncTestCaseParser.Eq, 0)

        def result(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ResultContext,0)


        def identifier(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IdentifierContext,0)


        def OBracket(self):
            return self.getToken(FuncTestCaseParser.OBracket, 0)

        def funcOptions(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FuncOptionsContext,0)


        def CBracket(self):
            return self.getToken(FuncTestCaseParser.CBracket, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_testCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestCase" ):
                listener.enterTestCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestCase" ):
                listener.exitTestCase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestCase" ):
                return visitor.visitTestCase(self)
            else:
                return visitor.visitChildren(self)




    def testCase(self):

        localctx = FuncTestCaseParser.TestCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_testCase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            localctx.functionName = self.identifier()
            self.state = 164
            self.match(FuncTestCaseParser.OParen)
            self.state = 165
            self.arguments()
            self.state = 166
            self.match(FuncTestCaseParser.CParen)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==108:
                self.state = 167
                self.match(FuncTestCaseParser.OBracket)
                self.state = 168
                self.funcOptions()
                self.state = 169
                self.match(FuncTestCaseParser.CBracket)


            self.state = 173
            self.match(FuncTestCaseParser.Eq)
            self.state = 174
            self.result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_testGroup

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ScalarFuncTestGroupContext(TestGroupContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.TestGroupContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def testGroupDescription(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TestGroupDescriptionContext,0)

        def testCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.TestCaseContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.TestCaseContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScalarFuncTestGroup" ):
                listener.enterScalarFuncTestGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScalarFuncTestGroup" ):
                listener.exitScalarFuncTestGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarFuncTestGroup" ):
                return visitor.visitScalarFuncTestGroup(self)
            else:
                return visitor.visitChildren(self)


    class AggregateFuncTestGroupContext(TestGroupContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.TestGroupContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def testGroupDescription(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TestGroupDescriptionContext,0)

        def aggFuncTestCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.AggFuncTestCaseContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.AggFuncTestCaseContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateFuncTestGroup" ):
                listener.enterAggregateFuncTestGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateFuncTestGroup" ):
                listener.exitAggregateFuncTestGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateFuncTestGroup" ):
                return visitor.visitAggregateFuncTestGroup(self)
            else:
                return visitor.visitChildren(self)



    def testGroup(self):

        localctx = FuncTestCaseParser.TestGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_testGroup)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = FuncTestCaseParser.ScalarFuncTestGroupContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 176
                    self.testGroupDescription()


                self.state = 180 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 179
                        self.testCase()

                    else:
                        raise NoViableAltException(self)
                    self.state = 182 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 2:
                localctx = FuncTestCaseParser.AggregateFuncTestGroupContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 184
                    self.testGroupDescription()


                self.state = 188 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 187
                        self.aggFuncTestCase()

                    else:
                        raise NoViableAltException(self)
                    self.state = 190 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.ArgumentContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.Comma)
            else:
                return self.getToken(FuncTestCaseParser.Comma, i)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = FuncTestCaseParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.argument()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==110:
                self.state = 195
                self.match(FuncTestCaseParser.Comma)
                self.state = 196
                self.argument()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ArgumentContext,0)


        def substraitError(self):
            return self.getTypedRuleContext(FuncTestCaseParser.SubstraitErrorContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResult" ):
                listener.enterResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResult" ):
                listener.exitResult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResult" ):
                return visitor.visitResult(self)
            else:
                return visitor.visitChildren(self)




    def result(self):

        localctx = FuncTestCaseParser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_result)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 23, 24, 25, 26, 27, 28, 29, 30, 41, 42, 43, 44, 108]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.argument()
                pass
            elif token in [9, 10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.substraitError()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NullArgContext,0)


        def intArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IntArgContext,0)


        def floatArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FloatArgContext,0)


        def booleanArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.BooleanArgContext,0)


        def stringArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.StringArgContext,0)


        def decimalArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.DecimalArgContext,0)


        def dateArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.DateArgContext,0)


        def timeArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TimeArgContext,0)


        def timestampArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TimestampArgContext,0)


        def timestampTzArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TimestampTzArgContext,0)


        def intervalYearArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IntervalYearArgContext,0)


        def intervalDayArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IntervalDayArgContext,0)


        def fixedCharArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FixedCharArgContext,0)


        def varCharArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.VarCharArgContext,0)


        def fixedBinaryArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FixedBinaryArgContext,0)


        def precisionTimestampArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.PrecisionTimestampArgContext,0)


        def precisionTimestampTZArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.PrecisionTimestampTZArgContext,0)


        def listArg(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ListArgContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = FuncTestCaseParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argument)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.nullArg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.intArg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.floatArg()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.booleanArg()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.stringArg()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 211
                self.decimalArg()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 212
                self.dateArg()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 213
                self.timeArg()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 214
                self.timestampArg()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 215
                self.timestampTzArg()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 216
                self.intervalYearArg()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 217
                self.intervalDayArg()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 218
                self.fixedCharArg()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 219
                self.varCharArg()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 220
                self.fixedBinaryArg()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 221
                self.precisionTimestampArg()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 222
                self.precisionTimestampTZArg()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 223
                self.listArg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggFuncTestCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggFuncCall(self):
            return self.getTypedRuleContext(FuncTestCaseParser.AggFuncCallContext,0)


        def Eq(self):
            return self.getToken(FuncTestCaseParser.Eq, 0)

        def result(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ResultContext,0)


        def OBracket(self):
            return self.getToken(FuncTestCaseParser.OBracket, 0)

        def funcOptions(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FuncOptionsContext,0)


        def CBracket(self):
            return self.getToken(FuncTestCaseParser.CBracket, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_aggFuncTestCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggFuncTestCase" ):
                listener.enterAggFuncTestCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggFuncTestCase" ):
                listener.exitAggFuncTestCase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggFuncTestCase" ):
                return visitor.visitAggFuncTestCase(self)
            else:
                return visitor.visitChildren(self)




    def aggFuncTestCase(self):

        localctx = FuncTestCaseParser.AggFuncTestCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_aggFuncTestCase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.aggFuncCall()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==108:
                self.state = 227
                self.match(FuncTestCaseParser.OBracket)
                self.state = 228
                self.funcOptions()
                self.state = 229
                self.match(FuncTestCaseParser.CBracket)


            self.state = 233
            self.match(FuncTestCaseParser.Eq)
            self.state = 234
            self.result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggFuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_aggFuncCall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleArgAggregateFuncCallContext(AggFuncCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.AggFuncCallContext
            super().__init__(parser)
            self.functName = None # IdentifierContext
            self.copyFrom(ctx)

        def OParen(self):
            return self.getToken(FuncTestCaseParser.OParen, 0)
        def dataColumn(self):
            return self.getTypedRuleContext(FuncTestCaseParser.DataColumnContext,0)

        def CParen(self):
            return self.getToken(FuncTestCaseParser.CParen, 0)
        def identifier(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleArgAggregateFuncCall" ):
                listener.enterSingleArgAggregateFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleArgAggregateFuncCall" ):
                listener.exitSingleArgAggregateFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleArgAggregateFuncCall" ):
                return visitor.visitSingleArgAggregateFuncCall(self)
            else:
                return visitor.visitChildren(self)


    class MultiArgAggregateFuncCallContext(AggFuncCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.AggFuncCallContext
            super().__init__(parser)
            self.funcName = None # IdentifierContext
            self.copyFrom(ctx)

        def tableData(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TableDataContext,0)

        def OParen(self):
            return self.getToken(FuncTestCaseParser.OParen, 0)
        def CParen(self):
            return self.getToken(FuncTestCaseParser.CParen, 0)
        def identifier(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IdentifierContext,0)

        def qualifiedAggregateFuncArgs(self):
            return self.getTypedRuleContext(FuncTestCaseParser.QualifiedAggregateFuncArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiArgAggregateFuncCall" ):
                listener.enterMultiArgAggregateFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiArgAggregateFuncCall" ):
                listener.exitMultiArgAggregateFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiArgAggregateFuncCall" ):
                return visitor.visitMultiArgAggregateFuncCall(self)
            else:
                return visitor.visitChildren(self)


    class CompactAggregateFuncCallContext(AggFuncCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.AggFuncCallContext
            super().__init__(parser)
            self.functName = None # IdentifierContext
            self.copyFrom(ctx)

        def tableRows(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TableRowsContext,0)

        def OParen(self):
            return self.getToken(FuncTestCaseParser.OParen, 0)
        def CParen(self):
            return self.getToken(FuncTestCaseParser.CParen, 0)
        def identifier(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IdentifierContext,0)

        def aggregateFuncArgs(self):
            return self.getTypedRuleContext(FuncTestCaseParser.AggregateFuncArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompactAggregateFuncCall" ):
                listener.enterCompactAggregateFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompactAggregateFuncCall" ):
                listener.exitCompactAggregateFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompactAggregateFuncCall" ):
                return visitor.visitCompactAggregateFuncCall(self)
            else:
                return visitor.visitChildren(self)



    def aggFuncCall(self):

        localctx = FuncTestCaseParser.AggFuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_aggFuncCall)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = FuncTestCaseParser.MultiArgAggregateFuncCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.tableData()
                self.state = 237
                localctx.funcName = self.identifier()
                self.state = 238
                self.match(FuncTestCaseParser.OParen)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32987488059392) != 0) or _la==108 or _la==119:
                    self.state = 239
                    self.qualifiedAggregateFuncArgs()


                self.state = 242
                self.match(FuncTestCaseParser.CParen)
                pass
            elif token in [106]:
                localctx = FuncTestCaseParser.CompactAggregateFuncCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.tableRows()
                self.state = 245
                localctx.functName = self.identifier()
                self.state = 246
                self.match(FuncTestCaseParser.OParen)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68171860148224) != 0) or _la==108:
                    self.state = 247
                    self.aggregateFuncArgs()


                self.state = 250
                self.match(FuncTestCaseParser.CParen)
                pass
            elif token in [22, 115, 116, 119]:
                localctx = FuncTestCaseParser.SingleArgAggregateFuncCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                localctx.functName = self.identifier()
                self.state = 253
                self.match(FuncTestCaseParser.OParen)
                self.state = 254
                self.dataColumn()
                self.state = 255
                self.match(FuncTestCaseParser.CParen)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tableName = None # Token

        def Define(self):
            return self.getToken(FuncTestCaseParser.Define, 0)

        def OParen(self):
            return self.getToken(FuncTestCaseParser.OParen, 0)

        def dataType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.DataTypeContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.DataTypeContext,i)


        def CParen(self):
            return self.getToken(FuncTestCaseParser.CParen, 0)

        def Eq(self):
            return self.getToken(FuncTestCaseParser.Eq, 0)

        def tableRows(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TableRowsContext,0)


        def Identifier(self):
            return self.getToken(FuncTestCaseParser.Identifier, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.Comma)
            else:
                return self.getToken(FuncTestCaseParser.Comma, i)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_tableData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableData" ):
                listener.enterTableData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableData" ):
                listener.exitTableData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableData" ):
                return visitor.visitTableData(self)
            else:
                return visitor.visitChildren(self)




    def tableData(self):

        localctx = FuncTestCaseParser.TableDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tableData)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(FuncTestCaseParser.Define)
            self.state = 260
            localctx.tableName = self.match(FuncTestCaseParser.Identifier)
            self.state = 261
            self.match(FuncTestCaseParser.OParen)
            self.state = 262
            self.dataType()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==110:
                self.state = 263
                self.match(FuncTestCaseParser.Comma)
                self.state = 264
                self.dataType()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 270
            self.match(FuncTestCaseParser.CParen)
            self.state = 271
            self.match(FuncTestCaseParser.Eq)
            self.state = 272
            self.tableRows()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableRowsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OParen(self):
            return self.getToken(FuncTestCaseParser.OParen, 0)

        def CParen(self):
            return self.getToken(FuncTestCaseParser.CParen, 0)

        def columnValues(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.ColumnValuesContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.ColumnValuesContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.Comma)
            else:
                return self.getToken(FuncTestCaseParser.Comma, i)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_tableRows

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableRows" ):
                listener.enterTableRows(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableRows" ):
                listener.exitTableRows(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableRows" ):
                return visitor.visitTableRows(self)
            else:
                return visitor.visitChildren(self)




    def tableRows(self):

        localctx = FuncTestCaseParser.TableRowsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_tableRows)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(FuncTestCaseParser.OParen)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==106:
                self.state = 275
                self.columnValues()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==110:
                    self.state = 276
                    self.match(FuncTestCaseParser.Comma)
                    self.state = 277
                    self.columnValues()
                    self.state = 282
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 285
            self.match(FuncTestCaseParser.CParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnValues(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ColumnValuesContext,0)


        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def dataType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.DataTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_dataColumn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataColumn" ):
                listener.enterDataColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataColumn" ):
                listener.exitDataColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataColumn" ):
                return visitor.visitDataColumn(self)
            else:
                return visitor.visitChildren(self)




    def dataColumn(self):

        localctx = FuncTestCaseParser.DataColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dataColumn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.columnValues()
            self.state = 288
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 289
            self.dataType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OParen(self):
            return self.getToken(FuncTestCaseParser.OParen, 0)

        def CParen(self):
            return self.getToken(FuncTestCaseParser.CParen, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.LiteralContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.LiteralContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.Comma)
            else:
                return self.getToken(FuncTestCaseParser.Comma, i)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_columnValues

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnValues" ):
                listener.enterColumnValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnValues" ):
                listener.exitColumnValues(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnValues" ):
                return visitor.visitColumnValues(self)
            else:
                return visitor.visitChildren(self)




    def columnValues(self):

        localctx = FuncTestCaseParser.ColumnValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_columnValues)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(FuncTestCaseParser.OParen)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32987488059392) != 0):
                self.state = 292
                self.literal()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==110:
                    self.state = 293
                    self.match(FuncTestCaseParser.Comma)
                    self.state = 294
                    self.literal()
                    self.state = 299
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 302
            self.match(FuncTestCaseParser.CParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NullLiteral(self):
            return self.getToken(FuncTestCaseParser.NullLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NumericLiteralContext,0)


        def BooleanLiteral(self):
            return self.getToken(FuncTestCaseParser.BooleanLiteral, 0)

        def StringLiteral(self):
            return self.getToken(FuncTestCaseParser.StringLiteral, 0)

        def DateLiteral(self):
            return self.getToken(FuncTestCaseParser.DateLiteral, 0)

        def TimeLiteral(self):
            return self.getToken(FuncTestCaseParser.TimeLiteral, 0)

        def TimestampLiteral(self):
            return self.getToken(FuncTestCaseParser.TimestampLiteral, 0)

        def TimestampTzLiteral(self):
            return self.getToken(FuncTestCaseParser.TimestampTzLiteral, 0)

        def IntervalYearLiteral(self):
            return self.getToken(FuncTestCaseParser.IntervalYearLiteral, 0)

        def IntervalDayLiteral(self):
            return self.getToken(FuncTestCaseParser.IntervalDayLiteral, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = FuncTestCaseParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_literal)
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(FuncTestCaseParser.NullLiteral)
                pass
            elif token in [17, 23, 24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.numericLiteral()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.match(FuncTestCaseParser.BooleanLiteral)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
                self.match(FuncTestCaseParser.StringLiteral)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 5)
                self.state = 308
                self.match(FuncTestCaseParser.DateLiteral)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 6)
                self.state = 309
                self.match(FuncTestCaseParser.TimeLiteral)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 7)
                self.state = 310
                self.match(FuncTestCaseParser.TimestampLiteral)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 8)
                self.state = 311
                self.match(FuncTestCaseParser.TimestampTzLiteral)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 9)
                self.state = 312
                self.match(FuncTestCaseParser.IntervalYearLiteral)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 10)
                self.state = 313
                self.match(FuncTestCaseParser.IntervalDayLiteral)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedAggregateFuncArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedAggregateFuncArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.QualifiedAggregateFuncArgContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.QualifiedAggregateFuncArgContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.Comma)
            else:
                return self.getToken(FuncTestCaseParser.Comma, i)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_qualifiedAggregateFuncArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedAggregateFuncArgs" ):
                listener.enterQualifiedAggregateFuncArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedAggregateFuncArgs" ):
                listener.exitQualifiedAggregateFuncArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedAggregateFuncArgs" ):
                return visitor.visitQualifiedAggregateFuncArgs(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedAggregateFuncArgs(self):

        localctx = FuncTestCaseParser.QualifiedAggregateFuncArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_qualifiedAggregateFuncArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.qualifiedAggregateFuncArg()
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==110:
                self.state = 317
                self.match(FuncTestCaseParser.Comma)
                self.state = 318
                self.qualifiedAggregateFuncArg()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateFuncArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregateFuncArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.AggregateFuncArgContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.AggregateFuncArgContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.Comma)
            else:
                return self.getToken(FuncTestCaseParser.Comma, i)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_aggregateFuncArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateFuncArgs" ):
                listener.enterAggregateFuncArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateFuncArgs" ):
                listener.exitAggregateFuncArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateFuncArgs" ):
                return visitor.visitAggregateFuncArgs(self)
            else:
                return visitor.visitChildren(self)




    def aggregateFuncArgs(self):

        localctx = FuncTestCaseParser.AggregateFuncArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_aggregateFuncArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.aggregateFuncArg()
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==110:
                self.state = 325
                self.match(FuncTestCaseParser.Comma)
                self.state = 326
                self.aggregateFuncArg()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedAggregateFuncArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tableName = None # Token

        def Dot(self):
            return self.getToken(FuncTestCaseParser.Dot, 0)

        def ColumnName(self):
            return self.getToken(FuncTestCaseParser.ColumnName, 0)

        def Identifier(self):
            return self.getToken(FuncTestCaseParser.Identifier, 0)

        def argument(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ArgumentContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_qualifiedAggregateFuncArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedAggregateFuncArg" ):
                listener.enterQualifiedAggregateFuncArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedAggregateFuncArg" ):
                listener.exitQualifiedAggregateFuncArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedAggregateFuncArg" ):
                return visitor.visitQualifiedAggregateFuncArg(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedAggregateFuncArg(self):

        localctx = FuncTestCaseParser.QualifiedAggregateFuncArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_qualifiedAggregateFuncArg)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [119]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                localctx.tableName = self.match(FuncTestCaseParser.Identifier)
                self.state = 333
                self.match(FuncTestCaseParser.Dot)
                self.state = 334
                self.match(FuncTestCaseParser.ColumnName)
                pass
            elif token in [17, 23, 24, 25, 26, 27, 28, 29, 30, 41, 42, 43, 44, 108]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateFuncArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ColumnName(self):
            return self.getToken(FuncTestCaseParser.ColumnName, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def dataType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.DataTypeContext,0)


        def argument(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ArgumentContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_aggregateFuncArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateFuncArg" ):
                listener.enterAggregateFuncArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateFuncArg" ):
                listener.exitAggregateFuncArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateFuncArg" ):
                return visitor.visitAggregateFuncArg(self)
            else:
                return visitor.visitChildren(self)




    def aggregateFuncArg(self):

        localctx = FuncTestCaseParser.AggregateFuncArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_aggregateFuncArg)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(FuncTestCaseParser.ColumnName)
                self.state = 339
                self.match(FuncTestCaseParser.DoubleColon)
                self.state = 340
                self.dataType()
                pass
            elif token in [17, 23, 24, 25, 26, 27, 28, 29, 30, 41, 42, 43, 44, 108]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(FuncTestCaseParser.DecimalLiteral, 0)

        def IntegerLiteral(self):
            return self.getToken(FuncTestCaseParser.IntegerLiteral, 0)

        def floatLiteral(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FloatLiteralContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_numericLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteral" ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteral" ):
                listener.exitNumericLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericLiteral" ):
                return visitor.visitNumericLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteral(self):

        localctx = FuncTestCaseParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_numericLiteral)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(FuncTestCaseParser.DecimalLiteral)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.match(FuncTestCaseParser.IntegerLiteral)
                pass
            elif token in [17, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self.floatLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FloatLiteral(self):
            return self.getToken(FuncTestCaseParser.FloatLiteral, 0)

        def NaN(self):
            return self.getToken(FuncTestCaseParser.NaN, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_floatLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)




    def floatLiteral(self):

        localctx = FuncTestCaseParser.FloatLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_floatLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            _la = self._input.LA(1)
            if not(_la==17 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NullLiteral(self):
            return self.getToken(FuncTestCaseParser.NullLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def dataType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.DataTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_nullArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullArg" ):
                listener.enterNullArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullArg" ):
                listener.exitNullArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullArg" ):
                return visitor.visitNullArg(self)
            else:
                return visitor.visitChildren(self)




    def nullArg(self):

        localctx = FuncTestCaseParser.NullArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_nullArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(FuncTestCaseParser.NullLiteral)
            self.state = 352
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 353
            self.dataType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(FuncTestCaseParser.IntegerLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def I8(self):
            return self.getToken(FuncTestCaseParser.I8, 0)

        def I16(self):
            return self.getToken(FuncTestCaseParser.I16, 0)

        def I32(self):
            return self.getToken(FuncTestCaseParser.I32, 0)

        def I64(self):
            return self.getToken(FuncTestCaseParser.I64, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_intArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntArg" ):
                listener.enterIntArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntArg" ):
                listener.exitIntArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntArg" ):
                return visitor.visitIntArg(self)
            else:
                return visitor.visitChildren(self)




    def intArg(self):

        localctx = FuncTestCaseParser.IntArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_intArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(FuncTestCaseParser.IntegerLiteral)
            self.state = 356
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 357
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67553994410557440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericLiteral(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NumericLiteralContext,0)


        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def FP32(self):
            return self.getToken(FuncTestCaseParser.FP32, 0)

        def FP64(self):
            return self.getToken(FuncTestCaseParser.FP64, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_floatArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatArg" ):
                listener.enterFloatArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatArg" ):
                listener.exitFloatArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatArg" ):
                return visitor.visitFloatArg(self)
            else:
                return visitor.visitChildren(self)




    def floatArg(self):

        localctx = FuncTestCaseParser.FloatArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_floatArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.numericLiteral()
            self.state = 360
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 361
            _la = self._input.LA(1)
            if not(_la==56 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecimalArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericLiteral(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NumericLiteralContext,0)


        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def decimalType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.DecimalTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_decimalArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimalArg" ):
                listener.enterDecimalArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimalArg" ):
                listener.exitDecimalArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimalArg" ):
                return visitor.visitDecimalArg(self)
            else:
                return visitor.visitChildren(self)




    def decimalArg(self):

        localctx = FuncTestCaseParser.DecimalArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_decimalArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.numericLiteral()
            self.state = 364
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 365
            self.decimalType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BooleanLiteral(self):
            return self.getToken(FuncTestCaseParser.BooleanLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def booleanType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.BooleanTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_booleanArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanArg" ):
                listener.enterBooleanArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanArg" ):
                listener.exitBooleanArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanArg" ):
                return visitor.visitBooleanArg(self)
            else:
                return visitor.visitChildren(self)




    def booleanArg(self):

        localctx = FuncTestCaseParser.BooleanArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_booleanArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(FuncTestCaseParser.BooleanLiteral)
            self.state = 368
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 369
            self.booleanType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(FuncTestCaseParser.StringLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def stringType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.StringTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_stringArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringArg" ):
                listener.enterStringArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringArg" ):
                listener.exitStringArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringArg" ):
                return visitor.visitStringArg(self)
            else:
                return visitor.visitChildren(self)




    def stringArg(self):

        localctx = FuncTestCaseParser.StringArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stringArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(FuncTestCaseParser.StringLiteral)
            self.state = 372
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 373
            self.stringType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DateLiteral(self):
            return self.getToken(FuncTestCaseParser.DateLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def Date(self):
            return self.getToken(FuncTestCaseParser.Date, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_dateArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateArg" ):
                listener.enterDateArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateArg" ):
                listener.exitDateArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateArg" ):
                return visitor.visitDateArg(self)
            else:
                return visitor.visitChildren(self)




    def dateArg(self):

        localctx = FuncTestCaseParser.DateArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_dateArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(FuncTestCaseParser.DateLiteral)
            self.state = 376
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 377
            self.match(FuncTestCaseParser.Date)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TimeLiteral(self):
            return self.getToken(FuncTestCaseParser.TimeLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def Time(self):
            return self.getToken(FuncTestCaseParser.Time, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_timeArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeArg" ):
                listener.enterTimeArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeArg" ):
                listener.exitTimeArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeArg" ):
                return visitor.visitTimeArg(self)
            else:
                return visitor.visitChildren(self)




    def timeArg(self):

        localctx = FuncTestCaseParser.TimeArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_timeArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(FuncTestCaseParser.TimeLiteral)
            self.state = 380
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 381
            self.match(FuncTestCaseParser.Time)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimestampArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TimestampLiteral(self):
            return self.getToken(FuncTestCaseParser.TimestampLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def timestampType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TimestampTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_timestampArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimestampArg" ):
                listener.enterTimestampArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimestampArg" ):
                listener.exitTimestampArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimestampArg" ):
                return visitor.visitTimestampArg(self)
            else:
                return visitor.visitChildren(self)




    def timestampArg(self):

        localctx = FuncTestCaseParser.TimestampArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_timestampArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(FuncTestCaseParser.TimestampLiteral)
            self.state = 384
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 385
            self.timestampType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimestampTzArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TimestampTzLiteral(self):
            return self.getToken(FuncTestCaseParser.TimestampTzLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def timestampTZType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TimestampTZTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_timestampTzArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimestampTzArg" ):
                listener.enterTimestampTzArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimestampTzArg" ):
                listener.exitTimestampTzArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimestampTzArg" ):
                return visitor.visitTimestampTzArg(self)
            else:
                return visitor.visitChildren(self)




    def timestampTzArg(self):

        localctx = FuncTestCaseParser.TimestampTzArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_timestampTzArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(FuncTestCaseParser.TimestampTzLiteral)
            self.state = 388
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 389
            self.timestampTZType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalYearArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntervalYearLiteral(self):
            return self.getToken(FuncTestCaseParser.IntervalYearLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def intervalYearType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IntervalYearTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_intervalYearArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntervalYearArg" ):
                listener.enterIntervalYearArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntervalYearArg" ):
                listener.exitIntervalYearArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntervalYearArg" ):
                return visitor.visitIntervalYearArg(self)
            else:
                return visitor.visitChildren(self)




    def intervalYearArg(self):

        localctx = FuncTestCaseParser.IntervalYearArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_intervalYearArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(FuncTestCaseParser.IntervalYearLiteral)
            self.state = 392
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 393
            self.intervalYearType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalDayArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntervalDayLiteral(self):
            return self.getToken(FuncTestCaseParser.IntervalDayLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def intervalDayType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IntervalDayTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_intervalDayArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntervalDayArg" ):
                listener.enterIntervalDayArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntervalDayArg" ):
                listener.exitIntervalDayArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntervalDayArg" ):
                return visitor.visitIntervalDayArg(self)
            else:
                return visitor.visitChildren(self)




    def intervalDayArg(self):

        localctx = FuncTestCaseParser.IntervalDayArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_intervalDayArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(FuncTestCaseParser.IntervalDayLiteral)
            self.state = 396
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 397
            self.intervalDayType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FixedCharArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(FuncTestCaseParser.StringLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def fixedCharType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FixedCharTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_fixedCharArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixedCharArg" ):
                listener.enterFixedCharArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixedCharArg" ):
                listener.exitFixedCharArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFixedCharArg" ):
                return visitor.visitFixedCharArg(self)
            else:
                return visitor.visitChildren(self)




    def fixedCharArg(self):

        localctx = FuncTestCaseParser.FixedCharArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_fixedCharArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(FuncTestCaseParser.StringLiteral)
            self.state = 400
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 401
            self.fixedCharType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarCharArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(FuncTestCaseParser.StringLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def varCharType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.VarCharTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_varCharArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarCharArg" ):
                listener.enterVarCharArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarCharArg" ):
                listener.exitVarCharArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarCharArg" ):
                return visitor.visitVarCharArg(self)
            else:
                return visitor.visitChildren(self)




    def varCharArg(self):

        localctx = FuncTestCaseParser.VarCharArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_varCharArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(FuncTestCaseParser.StringLiteral)
            self.state = 404
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 405
            self.varCharType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FixedBinaryArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(FuncTestCaseParser.StringLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def fixedBinaryType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FixedBinaryTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_fixedBinaryArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixedBinaryArg" ):
                listener.enterFixedBinaryArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixedBinaryArg" ):
                listener.exitFixedBinaryArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFixedBinaryArg" ):
                return visitor.visitFixedBinaryArg(self)
            else:
                return visitor.visitChildren(self)




    def fixedBinaryArg(self):

        localctx = FuncTestCaseParser.FixedBinaryArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_fixedBinaryArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(FuncTestCaseParser.StringLiteral)
            self.state = 408
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 409
            self.fixedBinaryType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrecisionTimestampArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TimestampLiteral(self):
            return self.getToken(FuncTestCaseParser.TimestampLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def precisionTimestampType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.PrecisionTimestampTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_precisionTimestampArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecisionTimestampArg" ):
                listener.enterPrecisionTimestampArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecisionTimestampArg" ):
                listener.exitPrecisionTimestampArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecisionTimestampArg" ):
                return visitor.visitPrecisionTimestampArg(self)
            else:
                return visitor.visitChildren(self)




    def precisionTimestampArg(self):

        localctx = FuncTestCaseParser.PrecisionTimestampArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_precisionTimestampArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(FuncTestCaseParser.TimestampLiteral)
            self.state = 412
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 413
            self.precisionTimestampType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrecisionTimestampTZArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TimestampTzLiteral(self):
            return self.getToken(FuncTestCaseParser.TimestampTzLiteral, 0)

        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def precisionTimestampTZType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.PrecisionTimestampTZTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_precisionTimestampTZArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecisionTimestampTZArg" ):
                listener.enterPrecisionTimestampTZArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecisionTimestampTZArg" ):
                listener.exitPrecisionTimestampTZArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecisionTimestampTZArg" ):
                return visitor.visitPrecisionTimestampTZArg(self)
            else:
                return visitor.visitChildren(self)




    def precisionTimestampTZArg(self):

        localctx = FuncTestCaseParser.PrecisionTimestampTZArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_precisionTimestampTZArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(FuncTestCaseParser.TimestampTzLiteral)
            self.state = 416
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 417
            self.precisionTimestampTZType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalList(self):
            return self.getTypedRuleContext(FuncTestCaseParser.LiteralListContext,0)


        def DoubleColon(self):
            return self.getToken(FuncTestCaseParser.DoubleColon, 0)

        def listType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ListTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_listArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListArg" ):
                listener.enterListArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListArg" ):
                listener.exitListArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListArg" ):
                return visitor.visitListArg(self)
            else:
                return visitor.visitChildren(self)




    def listArg(self):

        localctx = FuncTestCaseParser.ListArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_listArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.literalList()
            self.state = 420
            self.match(FuncTestCaseParser.DoubleColon)
            self.state = 421
            self.listType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBracket(self):
            return self.getToken(FuncTestCaseParser.OBracket, 0)

        def CBracket(self):
            return self.getToken(FuncTestCaseParser.CBracket, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.LiteralContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.LiteralContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.Comma)
            else:
                return self.getToken(FuncTestCaseParser.Comma, i)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_literalList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralList" ):
                listener.enterLiteralList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralList" ):
                listener.exitLiteralList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralList" ):
                return visitor.visitLiteralList(self)
            else:
                return visitor.visitChildren(self)




    def literalList(self):

        localctx = FuncTestCaseParser.LiteralListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_literalList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(FuncTestCaseParser.OBracket)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32987488059392) != 0):
                self.state = 424
                self.literal()
                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==110:
                    self.state = 425
                    self.match(FuncTestCaseParser.Comma)
                    self.state = 426
                    self.literal()
                    self.state = 431
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 434
            self.match(FuncTestCaseParser.CBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ScalarTypeContext,0)


        def parameterizedType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.ParameterizedTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = FuncTestCaseParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_dataType)
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 77, 78, 79, 80, 81, 82, 83]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.scalarType()
                pass
            elif token in [65, 67, 68, 69, 70, 71, 72, 84, 85, 86, 87, 88, 89, 90]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.parameterizedType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_scalarType

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DateContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Date(self):
            return self.getToken(FuncTestCaseParser.Date, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDate" ):
                return visitor.visitDate(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stringType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.StringTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class I64Context(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def I64(self):
            return self.getToken(FuncTestCaseParser.I64, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterI64" ):
                listener.enterI64(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitI64" ):
                listener.exitI64(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitI64" ):
                return visitor.visitI64(self)
            else:
                return visitor.visitChildren(self)


    class UserDefinedContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UserDefined(self):
            return self.getToken(FuncTestCaseParser.UserDefined, 0)
        def Identifier(self):
            return self.getToken(FuncTestCaseParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUserDefined" ):
                listener.enterUserDefined(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUserDefined" ):
                listener.exitUserDefined(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUserDefined" ):
                return visitor.visitUserDefined(self)
            else:
                return visitor.visitChildren(self)


    class I32Context(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def I32(self):
            return self.getToken(FuncTestCaseParser.I32, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterI32" ):
                listener.enterI32(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitI32" ):
                listener.exitI32(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitI32" ):
                return visitor.visitI32(self)
            else:
                return visitor.visitChildren(self)


    class IntervalYearContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def intervalYearType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IntervalYearTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntervalYear" ):
                listener.enterIntervalYear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntervalYear" ):
                listener.exitIntervalYear(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntervalYear" ):
                return visitor.visitIntervalYear(self)
            else:
                return visitor.visitChildren(self)


    class UuidContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(FuncTestCaseParser.UUID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUuid" ):
                listener.enterUuid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUuid" ):
                listener.exitUuid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUuid" ):
                return visitor.visitUuid(self)
            else:
                return visitor.visitChildren(self)


    class I8Context(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def I8(self):
            return self.getToken(FuncTestCaseParser.I8, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterI8" ):
                listener.enterI8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitI8" ):
                listener.exitI8(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitI8" ):
                return visitor.visitI8(self)
            else:
                return visitor.visitChildren(self)


    class I16Context(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def I16(self):
            return self.getToken(FuncTestCaseParser.I16, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterI16" ):
                listener.enterI16(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitI16" ):
                listener.exitI16(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitI16" ):
                return visitor.visitI16(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.BooleanTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class BinaryContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def binaryType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.BinaryTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary" ):
                listener.enterBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary" ):
                listener.exitBinary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary" ):
                return visitor.visitBinary(self)
            else:
                return visitor.visitChildren(self)


    class Fp64Context(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FP64(self):
            return self.getToken(FuncTestCaseParser.FP64, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFp64" ):
                listener.enterFp64(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFp64" ):
                listener.exitFp64(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFp64" ):
                return visitor.visitFp64(self)
            else:
                return visitor.visitChildren(self)


    class Fp32Context(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FP32(self):
            return self.getToken(FuncTestCaseParser.FP32, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFp32" ):
                listener.enterFp32(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFp32" ):
                listener.exitFp32(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFp32" ):
                return visitor.visitFp32(self)
            else:
                return visitor.visitChildren(self)


    class TimeContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Time(self):
            return self.getToken(FuncTestCaseParser.Time, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime" ):
                return visitor.visitTime(self)
            else:
                return visitor.visitChildren(self)


    class TimestampContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def timestampType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TimestampTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimestamp" ):
                listener.enterTimestamp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimestamp" ):
                listener.exitTimestamp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimestamp" ):
                return visitor.visitTimestamp(self)
            else:
                return visitor.visitChildren(self)


    class TimestampTzContext(ScalarTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ScalarTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def timestampTZType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.TimestampTZTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimestampTz" ):
                listener.enterTimestampTz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimestampTz" ):
                listener.exitTimestampTz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimestampTz" ):
                return visitor.visitTimestampTz(self)
            else:
                return visitor.visitChildren(self)



    def scalarType(self):

        localctx = FuncTestCaseParser.ScalarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_scalarType)
        try:
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51, 78]:
                localctx = FuncTestCaseParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.booleanType()
                pass
            elif token in [52]:
                localctx = FuncTestCaseParser.I8Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.match(FuncTestCaseParser.I8)
                pass
            elif token in [53]:
                localctx = FuncTestCaseParser.I16Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.match(FuncTestCaseParser.I16)
                pass
            elif token in [54]:
                localctx = FuncTestCaseParser.I32Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 443
                self.match(FuncTestCaseParser.I32)
                pass
            elif token in [55]:
                localctx = FuncTestCaseParser.I64Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 444
                self.match(FuncTestCaseParser.I64)
                pass
            elif token in [56]:
                localctx = FuncTestCaseParser.Fp32Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 445
                self.match(FuncTestCaseParser.FP32)
                pass
            elif token in [57]:
                localctx = FuncTestCaseParser.Fp64Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 446
                self.match(FuncTestCaseParser.FP64)
                pass
            elif token in [58, 79]:
                localctx = FuncTestCaseParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 447
                self.stringType()
                pass
            elif token in [59, 80]:
                localctx = FuncTestCaseParser.BinaryContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 448
                self.binaryType()
                pass
            elif token in [60, 81]:
                localctx = FuncTestCaseParser.TimestampContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 449
                self.timestampType()
                pass
            elif token in [61, 82]:
                localctx = FuncTestCaseParser.TimestampTzContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 450
                self.timestampTZType()
                pass
            elif token in [62]:
                localctx = FuncTestCaseParser.DateContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 451
                self.match(FuncTestCaseParser.Date)
                pass
            elif token in [63]:
                localctx = FuncTestCaseParser.TimeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 452
                self.match(FuncTestCaseParser.Time)
                pass
            elif token in [64, 83]:
                localctx = FuncTestCaseParser.IntervalYearContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 453
                self.intervalYearType()
                pass
            elif token in [66]:
                localctx = FuncTestCaseParser.UuidContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 454
                self.match(FuncTestCaseParser.UUID)
                pass
            elif token in [77]:
                localctx = FuncTestCaseParser.UserDefinedContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 455
                self.match(FuncTestCaseParser.UserDefined)
                self.state = 456
                self.match(FuncTestCaseParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Bool(self):
            return self.getToken(FuncTestCaseParser.Bool, 0)

        def Boolean(self):
            return self.getToken(FuncTestCaseParser.Boolean, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_booleanType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanType" ):
                listener.enterBooleanType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanType" ):
                listener.exitBooleanType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanType" ):
                return visitor.visitBooleanType(self)
            else:
                return visitor.visitChildren(self)




    def booleanType(self):

        localctx = FuncTestCaseParser.BooleanTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_booleanType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            _la = self._input.LA(1)
            if not(_la==51 or _la==78):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Str(self):
            return self.getToken(FuncTestCaseParser.Str, 0)

        def String(self):
            return self.getToken(FuncTestCaseParser.String, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_stringType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringType" ):
                listener.enterStringType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringType" ):
                listener.exitStringType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringType" ):
                return visitor.visitStringType(self)
            else:
                return visitor.visitChildren(self)




    def stringType(self):

        localctx = FuncTestCaseParser.StringTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stringType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            _la = self._input.LA(1)
            if not(_la==58 or _la==79):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Binary(self):
            return self.getToken(FuncTestCaseParser.Binary, 0)

        def VBin(self):
            return self.getToken(FuncTestCaseParser.VBin, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_binaryType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryType" ):
                listener.enterBinaryType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryType" ):
                listener.exitBinaryType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryType" ):
                return visitor.visitBinaryType(self)
            else:
                return visitor.visitChildren(self)




    def binaryType(self):

        localctx = FuncTestCaseParser.BinaryTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_binaryType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            _la = self._input.LA(1)
            if not(_la==59 or _la==80):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimestampTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ts(self):
            return self.getToken(FuncTestCaseParser.Ts, 0)

        def Timestamp(self):
            return self.getToken(FuncTestCaseParser.Timestamp, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_timestampType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimestampType" ):
                listener.enterTimestampType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimestampType" ):
                listener.exitTimestampType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimestampType" ):
                return visitor.visitTimestampType(self)
            else:
                return visitor.visitChildren(self)




    def timestampType(self):

        localctx = FuncTestCaseParser.TimestampTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_timestampType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            _la = self._input.LA(1)
            if not(_la==60 or _la==81):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimestampTZTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TsTZ(self):
            return self.getToken(FuncTestCaseParser.TsTZ, 0)

        def Timestamp_TZ(self):
            return self.getToken(FuncTestCaseParser.Timestamp_TZ, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_timestampTZType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimestampTZType" ):
                listener.enterTimestampTZType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimestampTZType" ):
                listener.exitTimestampTZType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimestampTZType" ):
                return visitor.visitTimestampTZType(self)
            else:
                return visitor.visitChildren(self)




    def timestampTZType(self):

        localctx = FuncTestCaseParser.TimestampTZTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_timestampTZType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            _la = self._input.LA(1)
            if not(_la==61 or _la==82):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalYearTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IYear(self):
            return self.getToken(FuncTestCaseParser.IYear, 0)

        def Interval_Year(self):
            return self.getToken(FuncTestCaseParser.Interval_Year, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_intervalYearType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntervalYearType" ):
                listener.enterIntervalYearType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntervalYearType" ):
                listener.exitIntervalYearType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntervalYearType" ):
                return visitor.visitIntervalYearType(self)
            else:
                return visitor.visitChildren(self)




    def intervalYearType(self):

        localctx = FuncTestCaseParser.IntervalYearTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_intervalYearType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            _la = self._input.LA(1)
            if not(_la==64 or _la==83):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalDayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.isnull = None # Token
            self.len_ = None # NumericParameterContext

        def IDay(self):
            return self.getToken(FuncTestCaseParser.IDay, 0)

        def Interval_Day(self):
            return self.getToken(FuncTestCaseParser.Interval_Day, 0)

        def OAngleBracket(self):
            return self.getToken(FuncTestCaseParser.OAngleBracket, 0)

        def CAngleBracket(self):
            return self.getToken(FuncTestCaseParser.CAngleBracket, 0)

        def QMark(self):
            return self.getToken(FuncTestCaseParser.QMark, 0)

        def numericParameter(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NumericParameterContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_intervalDayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntervalDayType" ):
                listener.enterIntervalDayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntervalDayType" ):
                listener.exitIntervalDayType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntervalDayType" ):
                return visitor.visitIntervalDayType(self)
            else:
                return visitor.visitChildren(self)




    def intervalDayType(self):

        localctx = FuncTestCaseParser.IntervalDayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_intervalDayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            _la = self._input.LA(1)
            if not(_la==65 or _la==84):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==112:
                self.state = 472
                localctx.isnull = self.match(FuncTestCaseParser.QMark)


            self.state = 479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 475
                self.match(FuncTestCaseParser.OAngleBracket)
                self.state = 476
                localctx.len_ = self.numericParameter()
                self.state = 477
                self.match(FuncTestCaseParser.CAngleBracket)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FixedCharTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.isnull = None # Token
            self.len_ = None # NumericParameterContext

        def OAngleBracket(self):
            return self.getToken(FuncTestCaseParser.OAngleBracket, 0)

        def CAngleBracket(self):
            return self.getToken(FuncTestCaseParser.CAngleBracket, 0)

        def FChar(self):
            return self.getToken(FuncTestCaseParser.FChar, 0)

        def FixedChar(self):
            return self.getToken(FuncTestCaseParser.FixedChar, 0)

        def numericParameter(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NumericParameterContext,0)


        def QMark(self):
            return self.getToken(FuncTestCaseParser.QMark, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_fixedCharType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixedCharType" ):
                listener.enterFixedCharType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixedCharType" ):
                listener.exitFixedCharType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFixedCharType" ):
                return visitor.visitFixedCharType(self)
            else:
                return visitor.visitChildren(self)




    def fixedCharType(self):

        localctx = FuncTestCaseParser.FixedCharTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_fixedCharType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            _la = self._input.LA(1)
            if not(_la==70 or _la==88):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==112:
                self.state = 482
                localctx.isnull = self.match(FuncTestCaseParser.QMark)


            self.state = 485
            self.match(FuncTestCaseParser.OAngleBracket)
            self.state = 486
            localctx.len_ = self.numericParameter()
            self.state = 487
            self.match(FuncTestCaseParser.CAngleBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarCharTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.isnull = None # Token
            self.len_ = None # NumericParameterContext

        def OAngleBracket(self):
            return self.getToken(FuncTestCaseParser.OAngleBracket, 0)

        def CAngleBracket(self):
            return self.getToken(FuncTestCaseParser.CAngleBracket, 0)

        def VChar(self):
            return self.getToken(FuncTestCaseParser.VChar, 0)

        def VarChar(self):
            return self.getToken(FuncTestCaseParser.VarChar, 0)

        def numericParameter(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NumericParameterContext,0)


        def QMark(self):
            return self.getToken(FuncTestCaseParser.QMark, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_varCharType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarCharType" ):
                listener.enterVarCharType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarCharType" ):
                listener.exitVarCharType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarCharType" ):
                return visitor.visitVarCharType(self)
            else:
                return visitor.visitChildren(self)




    def varCharType(self):

        localctx = FuncTestCaseParser.VarCharTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_varCharType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            _la = self._input.LA(1)
            if not(_la==71 or _la==89):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==112:
                self.state = 490
                localctx.isnull = self.match(FuncTestCaseParser.QMark)


            self.state = 493
            self.match(FuncTestCaseParser.OAngleBracket)
            self.state = 494
            localctx.len_ = self.numericParameter()
            self.state = 495
            self.match(FuncTestCaseParser.CAngleBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FixedBinaryTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.isnull = None # Token
            self.len_ = None # NumericParameterContext

        def OAngleBracket(self):
            return self.getToken(FuncTestCaseParser.OAngleBracket, 0)

        def CAngleBracket(self):
            return self.getToken(FuncTestCaseParser.CAngleBracket, 0)

        def FBin(self):
            return self.getToken(FuncTestCaseParser.FBin, 0)

        def FixedBinary(self):
            return self.getToken(FuncTestCaseParser.FixedBinary, 0)

        def numericParameter(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NumericParameterContext,0)


        def QMark(self):
            return self.getToken(FuncTestCaseParser.QMark, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_fixedBinaryType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixedBinaryType" ):
                listener.enterFixedBinaryType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixedBinaryType" ):
                listener.exitFixedBinaryType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFixedBinaryType" ):
                return visitor.visitFixedBinaryType(self)
            else:
                return visitor.visitChildren(self)




    def fixedBinaryType(self):

        localctx = FuncTestCaseParser.FixedBinaryTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_fixedBinaryType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            _la = self._input.LA(1)
            if not(_la==72 or _la==90):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==112:
                self.state = 498
                localctx.isnull = self.match(FuncTestCaseParser.QMark)


            self.state = 501
            self.match(FuncTestCaseParser.OAngleBracket)
            self.state = 502
            localctx.len_ = self.numericParameter()
            self.state = 503
            self.match(FuncTestCaseParser.CAngleBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecimalTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.isnull = None # Token
            self.precision = None # NumericParameterContext
            self.scale = None # NumericParameterContext

        def Dec(self):
            return self.getToken(FuncTestCaseParser.Dec, 0)

        def Decimal(self):
            return self.getToken(FuncTestCaseParser.Decimal, 0)

        def OAngleBracket(self):
            return self.getToken(FuncTestCaseParser.OAngleBracket, 0)

        def Comma(self):
            return self.getToken(FuncTestCaseParser.Comma, 0)

        def CAngleBracket(self):
            return self.getToken(FuncTestCaseParser.CAngleBracket, 0)

        def QMark(self):
            return self.getToken(FuncTestCaseParser.QMark, 0)

        def numericParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.NumericParameterContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.NumericParameterContext,i)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_decimalType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimalType" ):
                listener.enterDecimalType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimalType" ):
                listener.exitDecimalType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimalType" ):
                return visitor.visitDecimalType(self)
            else:
                return visitor.visitChildren(self)




    def decimalType(self):

        localctx = FuncTestCaseParser.DecimalTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_decimalType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            _la = self._input.LA(1)
            if not(_la==67 or _la==85):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==112:
                self.state = 506
                localctx.isnull = self.match(FuncTestCaseParser.QMark)


            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 509
                self.match(FuncTestCaseParser.OAngleBracket)
                self.state = 510
                localctx.precision = self.numericParameter()
                self.state = 511
                self.match(FuncTestCaseParser.Comma)
                self.state = 512
                localctx.scale = self.numericParameter()
                self.state = 513
                self.match(FuncTestCaseParser.CAngleBracket)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrecisionTimestampTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.isnull = None # Token
            self.precision = None # NumericParameterContext

        def OAngleBracket(self):
            return self.getToken(FuncTestCaseParser.OAngleBracket, 0)

        def CAngleBracket(self):
            return self.getToken(FuncTestCaseParser.CAngleBracket, 0)

        def PTs(self):
            return self.getToken(FuncTestCaseParser.PTs, 0)

        def Precision_Timestamp(self):
            return self.getToken(FuncTestCaseParser.Precision_Timestamp, 0)

        def numericParameter(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NumericParameterContext,0)


        def QMark(self):
            return self.getToken(FuncTestCaseParser.QMark, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_precisionTimestampType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecisionTimestampType" ):
                listener.enterPrecisionTimestampType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecisionTimestampType" ):
                listener.exitPrecisionTimestampType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecisionTimestampType" ):
                return visitor.visitPrecisionTimestampType(self)
            else:
                return visitor.visitChildren(self)




    def precisionTimestampType(self):

        localctx = FuncTestCaseParser.PrecisionTimestampTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_precisionTimestampType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            _la = self._input.LA(1)
            if not(_la==68 or _la==86):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==112:
                self.state = 518
                localctx.isnull = self.match(FuncTestCaseParser.QMark)


            self.state = 521
            self.match(FuncTestCaseParser.OAngleBracket)
            self.state = 522
            localctx.precision = self.numericParameter()
            self.state = 523
            self.match(FuncTestCaseParser.CAngleBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrecisionTimestampTZTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.isnull = None # Token
            self.precision = None # NumericParameterContext

        def OAngleBracket(self):
            return self.getToken(FuncTestCaseParser.OAngleBracket, 0)

        def CAngleBracket(self):
            return self.getToken(FuncTestCaseParser.CAngleBracket, 0)

        def PTsTZ(self):
            return self.getToken(FuncTestCaseParser.PTsTZ, 0)

        def Precision_Timestamp_TZ(self):
            return self.getToken(FuncTestCaseParser.Precision_Timestamp_TZ, 0)

        def numericParameter(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NumericParameterContext,0)


        def QMark(self):
            return self.getToken(FuncTestCaseParser.QMark, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_precisionTimestampTZType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecisionTimestampTZType" ):
                listener.enterPrecisionTimestampTZType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecisionTimestampTZType" ):
                listener.exitPrecisionTimestampTZType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecisionTimestampTZType" ):
                return visitor.visitPrecisionTimestampTZType(self)
            else:
                return visitor.visitChildren(self)




    def precisionTimestampTZType(self):

        localctx = FuncTestCaseParser.PrecisionTimestampTZTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_precisionTimestampTZType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            _la = self._input.LA(1)
            if not(_la==69 or _la==87):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 527
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==112:
                self.state = 526
                localctx.isnull = self.match(FuncTestCaseParser.QMark)


            self.state = 529
            self.match(FuncTestCaseParser.OAngleBracket)
            self.state = 530
            localctx.precision = self.numericParameter()
            self.state = 531
            self.match(FuncTestCaseParser.CAngleBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_listType

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListContext(ListTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.ListTypeContext
            super().__init__(parser)
            self.isnull = None # Token
            self.elemType = None # DataTypeContext
            self.copyFrom(ctx)

        def List(self):
            return self.getToken(FuncTestCaseParser.List, 0)
        def OAngleBracket(self):
            return self.getToken(FuncTestCaseParser.OAngleBracket, 0)
        def CAngleBracket(self):
            return self.getToken(FuncTestCaseParser.CAngleBracket, 0)
        def dataType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.DataTypeContext,0)

        def QMark(self):
            return self.getToken(FuncTestCaseParser.QMark, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)



    def listType(self):

        localctx = FuncTestCaseParser.ListTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_listType)
        self._la = 0 # Token type
        try:
            localctx = FuncTestCaseParser.ListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(FuncTestCaseParser.List)
            self.state = 535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==112:
                self.state = 534
                localctx.isnull = self.match(FuncTestCaseParser.QMark)


            self.state = 537
            self.match(FuncTestCaseParser.OAngleBracket)
            self.state = 538
            localctx.elemType = self.dataType()
            self.state = 539
            self.match(FuncTestCaseParser.CAngleBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterizedTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixedCharType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FixedCharTypeContext,0)


        def varCharType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.VarCharTypeContext,0)


        def fixedBinaryType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.FixedBinaryTypeContext,0)


        def decimalType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.DecimalTypeContext,0)


        def intervalDayType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.IntervalDayTypeContext,0)


        def precisionTimestampType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.PrecisionTimestampTypeContext,0)


        def precisionTimestampTZType(self):
            return self.getTypedRuleContext(FuncTestCaseParser.PrecisionTimestampTZTypeContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_parameterizedType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterizedType" ):
                listener.enterParameterizedType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterizedType" ):
                listener.exitParameterizedType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterizedType" ):
                return visitor.visitParameterizedType(self)
            else:
                return visitor.visitChildren(self)




    def parameterizedType(self):

        localctx = FuncTestCaseParser.ParameterizedTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_parameterizedType)
        try:
            self.state = 548
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [70, 88]:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.fixedCharType()
                pass
            elif token in [71, 89]:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
                self.varCharType()
                pass
            elif token in [72, 90]:
                self.enterOuterAlt(localctx, 3)
                self.state = 543
                self.fixedBinaryType()
                pass
            elif token in [67, 85]:
                self.enterOuterAlt(localctx, 4)
                self.state = 544
                self.decimalType()
                pass
            elif token in [65, 84]:
                self.enterOuterAlt(localctx, 5)
                self.state = 545
                self.intervalDayType()
                pass
            elif token in [68, 86]:
                self.enterOuterAlt(localctx, 6)
                self.state = 546
                self.precisionTimestampType()
                pass
            elif token in [69, 87]:
                self.enterOuterAlt(localctx, 7)
                self.state = 547
                self.precisionTimestampTZType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_numericParameter

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerLiteralContext(NumericParameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FuncTestCaseParser.NumericParameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IntegerLiteral(self):
            return self.getToken(FuncTestCaseParser.IntegerLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerLiteral" ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerLiteral" ):
                listener.exitIntegerLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerLiteral" ):
                return visitor.visitIntegerLiteral(self)
            else:
                return visitor.visitChildren(self)



    def numericParameter(self):

        localctx = FuncTestCaseParser.NumericParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_numericParameter)
        try:
            localctx = FuncTestCaseParser.IntegerLiteralContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(FuncTestCaseParser.IntegerLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubstraitErrorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ErrorResult(self):
            return self.getToken(FuncTestCaseParser.ErrorResult, 0)

        def UndefineResult(self):
            return self.getToken(FuncTestCaseParser.UndefineResult, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_substraitError

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstraitError" ):
                listener.enterSubstraitError(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstraitError" ):
                listener.exitSubstraitError(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubstraitError" ):
                return visitor.visitSubstraitError(self)
            else:
                return visitor.visitChildren(self)




    def substraitError(self):

        localctx = FuncTestCaseParser.SubstraitErrorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_substraitError)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncOptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optionName(self):
            return self.getTypedRuleContext(FuncTestCaseParser.OptionNameContext,0)


        def Colon(self):
            return self.getToken(FuncTestCaseParser.Colon, 0)

        def optionValue(self):
            return self.getTypedRuleContext(FuncTestCaseParser.OptionValueContext,0)


        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_funcOption

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncOption" ):
                listener.enterFuncOption(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncOption" ):
                listener.exitFuncOption(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncOption" ):
                return visitor.visitFuncOption(self)
            else:
                return visitor.visitChildren(self)




    def funcOption(self):

        localctx = FuncTestCaseParser.FuncOptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_funcOption)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.optionName()
            self.state = 555
            self.match(FuncTestCaseParser.Colon)
            self.state = 556
            self.optionValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Overflow(self):
            return self.getToken(FuncTestCaseParser.Overflow, 0)

        def Rounding(self):
            return self.getToken(FuncTestCaseParser.Rounding, 0)

        def NullHandling(self):
            return self.getToken(FuncTestCaseParser.NullHandling, 0)

        def SpacesOnly(self):
            return self.getToken(FuncTestCaseParser.SpacesOnly, 0)

        def Identifier(self):
            return self.getToken(FuncTestCaseParser.Identifier, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_optionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionName" ):
                listener.enterOptionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionName" ):
                listener.exitOptionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionName" ):
                return visitor.visitOptionName(self)
            else:
                return visitor.visitChildren(self)




    def optionName(self):

        localctx = FuncTestCaseParser.OptionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_optionName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3151872) != 0) or _la==119):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Error(self):
            return self.getToken(FuncTestCaseParser.Error, 0)

        def Saturate(self):
            return self.getToken(FuncTestCaseParser.Saturate, 0)

        def Silent(self):
            return self.getToken(FuncTestCaseParser.Silent, 0)

        def TieToEven(self):
            return self.getToken(FuncTestCaseParser.TieToEven, 0)

        def NaN(self):
            return self.getToken(FuncTestCaseParser.NaN, 0)

        def Truncate(self):
            return self.getToken(FuncTestCaseParser.Truncate, 0)

        def AcceptNulls(self):
            return self.getToken(FuncTestCaseParser.AcceptNulls, 0)

        def IgnoreNulls(self):
            return self.getToken(FuncTestCaseParser.IgnoreNulls, 0)

        def BooleanLiteral(self):
            return self.getToken(FuncTestCaseParser.BooleanLiteral, 0)

        def NullLiteral(self):
            return self.getToken(FuncTestCaseParser.NullLiteral, 0)

        def Identifier(self):
            return self.getToken(FuncTestCaseParser.Identifier, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_optionValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionValue" ):
                listener.enterOptionValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionValue" ):
                listener.exitOptionValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionValue" ):
                return visitor.visitOptionValue(self)
            else:
                return visitor.visitChildren(self)




    def optionValue(self):

        localctx = FuncTestCaseParser.OptionValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_optionValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8796165365760) != 0) or _la==119):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncOptionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcOption(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncTestCaseParser.FuncOptionContext)
            else:
                return self.getTypedRuleContext(FuncTestCaseParser.FuncOptionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(FuncTestCaseParser.Comma)
            else:
                return self.getToken(FuncTestCaseParser.Comma, i)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_funcOptions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncOptions" ):
                listener.enterFuncOptions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncOptions" ):
                listener.exitFuncOptions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncOptions" ):
                return visitor.visitFuncOptions(self)
            else:
                return visitor.visitChildren(self)




    def funcOptions(self):

        localctx = FuncTestCaseParser.FuncOptionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_funcOptions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.funcOption()
            self.state = 567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==110:
                self.state = 563
                self.match(FuncTestCaseParser.Comma)
                self.state = 564
                self.funcOption()
                self.state = 569
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonReservedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def And(self):
            return self.getToken(FuncTestCaseParser.And, 0)

        def Or(self):
            return self.getToken(FuncTestCaseParser.Or, 0)

        def Truncate(self):
            return self.getToken(FuncTestCaseParser.Truncate, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_nonReserved

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonReserved" ):
                listener.enterNonReserved(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonReserved" ):
                listener.exitNonReserved(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonReserved" ):
                return visitor.visitNonReserved(self)
            else:
                return visitor.visitChildren(self)




    def nonReserved(self):

        localctx = FuncTestCaseParser.NonReservedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_nonReserved)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            _la = self._input.LA(1)
            if not(_la==22 or _la==115 or _la==116):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonReserved(self):
            return self.getTypedRuleContext(FuncTestCaseParser.NonReservedContext,0)


        def Identifier(self):
            return self.getToken(FuncTestCaseParser.Identifier, 0)

        def getRuleIndex(self):
            return FuncTestCaseParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = FuncTestCaseParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_identifier)
        try:
            self.state = 574
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 115, 116]:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                self.nonReserved()
                pass
            elif token in [119]:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                self.match(FuncTestCaseParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





