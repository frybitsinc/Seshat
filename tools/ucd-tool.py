#!/usr/bin/env python3
# Unicode Character Data tool that download, parse the database files
# from http://www.unicode.org/Public/UNIDATA
import sys
import os

class Gc:
    '''General_Category'''
    # C = 'Other'
    Cc = 'Control' # 'cntrl'
    Cf = 'Format'
    Cn = 'Unassigned'
    Co = 'Private_Use'
    Cs = 'Surrogate'
    # L = 'Letter'
    # LC = 'Cased_Letter' # Ll | Lt | Lu
    Ll = 'Lowercase_Letter'
    Lm = 'Modifier_Letter'
    Lo = 'Other_Letter'
    Lt = 'Titlecase_Letter'
    Lu = 'Uppercase_Letter'
    # M = 'Mark' # 'Combining_Mark' # Mc | Me | Mn
    Mc = 'Spacing_Mark'
    Me = 'Enclosing_Mark'
    Mn = 'Nonspacing_Mark'
    # N = 'Number' # Nd | Nl | No
    Nd = 'Decimal_Number' # 'digit'
    Nl = 'Letter_Number'
    No = 'Other_Number'
    # P = 'Punctuation' # 'punct' # Pc | Pd | Pe | Pf | Pi | Po | Ps
    Pc = 'Connector_Punctuation'
    Pd = 'Dash_Punctuation'
    Pe = 'Close_Punctuation'
    Pf = 'Final_Punctuation'
    Pi = 'Initial_Punctuation'
    Po = 'Other_Punctuation'
    Ps = 'Open_Punctuation'
    # S = 'Symbol' # Sc | Sk | Sm | So
    Sc = 'Currency_Symbol'
    Sk = 'Modifier_Symbol'
    Sm = 'Math_Symbol'
    So = 'Other_Symbol'
    # Z = 'Separator' # Zl | Zp | Zs
    Zl = 'Line_Separator'
    Zp = 'Paragraph_Separator'
    Zs = 'Space_Separator'

# Table 8. Property Type Key
#
# Property Type | Symbol | Examples
# --------------------------------
# Catalog	| C	| Age, Block
# Enumeration	| E	| Joining_Type, Line_Break
# Binary	| B	| Uppercase, White_Space
# String	| S	| Uppercase_Mapping, Case_Folding
# Numeric	| N	| Numeric_Value
# Miscellaneous	| M	| Name, Jamo_Short_Name
#
# http://www.unicode.org/reports/tr44/tr44-18.html#Type_Key_Table
class UnicodeData:
    '''Contains data single line in UnicodeData.txt'''
    def __init__(self):
        self.code = ''
        self.name = '' # M
        self.general_category = '' # E
        self.canonical_combining_class = '' # N
        self.bidi_class = '' # E
        self.decomposition_type = ''    # E
        self.decomposition_mapping = '' # S
        self.numeric_type = ''  # E
        self.numeric_value = '' # N
        self.bidi_mirrored = '' # B
        self.unicode_1_name = '' # M
        self.iso_comment = '' # M
        self.simple_uppercase_mapping = '' # S
        self.simple_lowercase_mapping = '' # S
        self.simple_titlecase_mapping = '' # S
    def parse(self, line):
        line = line.rstrip('\n')
        li = line.split(';')

        self.code = li[0]
        self.name = li[1]
        self.general_category = li[2]
        self.canonical_combining_class = li[3]
        self.bidi_class = li[4]
        self.decomposition_type = li[5]
        self.decomposition_mapping = li[6]
        self.numeric_type = li[7]
        self.numeric_value = li[8]
        self.bidi_mirrored = li[9]
        self.unicode_1_name = li[10]
        self.iso_comment = li[11]
        self.simple_uppercase_mapping = li[12]
        self.simple_lowercase_mapping = li[13]
        self.simple_titlecase_mapping = li[14]

# Ranged data. Some large data area are omitted such as Hangul Syllable,
# CJK Ideograph etc.
#
# 3400-4DB5: CJK Ideograph Extension A (Lo)
CJK_Ideograph_Ext_A_First = '<CJK Ideograph Extension A, First>'
CJK_Ideograph_Ext_A_Last = '<CJK Ideograph Extension A, Last>'
# 4E00-9FD5: CJK Ideograph (Lo)
CJK_Ideograph_First = '<CJK Ideograph, First>'
CJK_Ideograph_Last = '<CJK Ideograph, Last>'
# AC00-D7A3: Hangul Syllable (Lo)
Hangul_Syllable_First = '<Hangul Syllable, First>'
Hangul_Syllable_Last = '<Hangul Syllable, Last>'
# D800-DB7F: Non Private Use High Surrogate (Cs)
Non_PU_High_Srg_First = '<Non Private Use High Surrogate, First>'
Non_PU_High_Srg_Last = '<Non Private Use High Surrogate, Last>'
# DB80-DBFF: Private Use High Surrogate (Cs)
PU_High_Srg_First = '<Private Use High Surrogate, First>'
PU_High_Srg_Last = '<Private Use High Surrogate, Last>'
# DC00-DFFF: Low Surrogate (Cs)
Low_Srg_First = '<Low Surrogate, First>'
Low_Srg_Last = '<Low Surrogate, Last>'
# E000-F8FF: Private Use (Co)
PU_First = '<Private Use, First>'
PU_Last = '<Private Use, Last>'
# 17000-187EC: Tangut Ideograph (Lo)
Tangut_Ideograph_First = '<Tangut Ideograph, First>'
Tangut_Ideograph_Last = '<Tangut Ideograph, Last>'
# 20000-2A6D6: CJK Ideograph Extension B (Lo)
CJK_Ideograph_Ext_B_First = '<CJK Ideograph Extension B, First>'
CJK_Ideograph_Ext_B_Last = '<CJK Ideograph Extension B, Last>'
# 2A700-2B734: CJK Ideograph Extension C (Lo)
CJK_Ideograph_Ext_C_First = '<CJK Ideograph Extension C, First>'
CJK_Ideograph_Ext_C_Last = '<CJK Ideograph Extension C, Last>'
# 2B740-2B81D: CJK Ideograph Extension D (Lo)
CJK_Ideograph_Ext_D_First = '<CJK Ideograph Extension D, First>'
CJK_Ideograph_Ext_D_Last = '<CJK Ideograph Extension D, Last>'
# 2B820-2CEA1: CJK Ideograph Extension E (Lo)
CJK_Ideograph_Ext_E_First = '<CJK Ideograph Extension E, First>'
CJK_Ideograph_Ext_E_Last = '<CJK Ideograph Extension E, Last>'
# F0000-FFFFD: Plane 15 Private Use (Co)
Plane_15_PU_First = '<Plane 15 Private Use, First>'
Plane_15_PU_Last = '<Plane 15 Private Use, Last>'
# 100000-10FFFD: Plane 16 Private Use (Co)
Plane_16_PU_First = '<Plane 16 Private Use, First>'
Plane_16_PU_Last = '<Plane 16 Private Use, Last>'

ranged_list = (
    CJK_Ideograph_Ext_A_First, CJK_Ideograph_Ext_A_Last,
    CJK_Ideograph_First, CJK_Ideograph_Last,
    Hangul_Syllable_First, Hangul_Syllable_Last,
    Non_PU_High_Srg_First, Non_PU_High_Srg_Last,
    PU_High_Srg_First, PU_High_Srg_Last, Low_Srg_First, Low_Srg_Last,
    PU_First, PU_Last,
    Tangut_Ideograph_First, Tangut_Ideograph_Last,
    CJK_Ideograph_Ext_B_First, CJK_Ideograph_Ext_B_Last,
    CJK_Ideograph_Ext_C_First, CJK_Ideograph_Ext_C_Last,
    CJK_Ideograph_Ext_D_First, CJK_Ideograph_Ext_D_Last,
    CJK_Ideograph_Ext_E_First, CJK_Ideograph_Ext_E_Last,
    Plane_15_PU_First, Plane_15_PU_Last, Plane_16_PU_First, Plane_16_PU_Last
)

# Prefix strings. To prevent duplication of same text.
#
Prefix_Yi_Syllable = 'YI SYLLABLE' # A000-A48C
Prefix_Egyptian_Hieroglyph = 'EGYPTIAN_HIEROGLYPH' # 13000-1342E
Prefix_Tangut_Component = 'TANGUT COMPONENT' # 18800-18AF2
Prefix_Canadian_Syllabics = 'CANADIAN SYLLABICS' # 1400-167F, 18B0-18F5
# Prefix_CJK_Compatibility_Ideograph = 'CJK_COMPATIBILITY_IDEOGRAPH' # F900-FAD9, 2F800-2FA1D
Prefix_Bamum_Letter_Phase_A = 'BAMUM LETTER PHASE-A' # 16800-16856
Prefix_Bamum_Letter_Phase_B = 'BAMUM LETTER PHASE-B' # 16857-1688E
Prefix_Bamum_Letter_Phase_C = 'BAMUM LETTER PHASE-C' # 1688F-168F0
Prefix_Bamum_Letter_Phase_D = 'BAMUM LETTER PHASE-D' # 168F1-16965
Prefix_Bamum_Letter_Phase_E = 'BAMUM LETTER PHASE-E' # 16966-16A02
Prefix_Bamum_Letter_Phase_F = 'BAMUM LETTER PHASE-F' # 16A03-16A38

# Prefix select
def search_prefix(code_point):
    if 0xA000 <= code_point and code_point <= 0xA48C:
        return Prefix_Yi_Syllable
    elif 0x13000 <= code_point and code_point <= 0x1342E:
        return Prefix_Egyptian_Hieroglyph
    elif 0x18800 <= code_point and code_point <= 0x18AF2:
        return Prefix_Tangut_Component
    elif (0x1400 <= code_point and code_point <= 0x167F) or \
        (0x18B0 <= code_point and code_point <= 0x18F5):
        return Prefix_Canadian_Syllabics
    elif 0x16800 <= code_point and code_point <= 0x16856:
        return Prefix_Bamum_Letter_Phase_A
    elif 0x16857 <= code_point and code_point <= 0x1688E:
        return Prefix_Bamum_Letter_Phase_B
    elif 0x1688F <= code_point and code_point <= 0x168F0:
        return Prefix_Bamum_Letter_Phase_C
    elif 0x168F1 <= code_point and code_point <= 0x16965:
        return Prefix_Bamum_Letter_Phase_D
    elif 0x16966 <= code_point and code_point <= 0x16A02:
        return Prefix_Bamum_Letter_Phase_E
    elif 0x16A03 <= code_point and code_point <= 0x16A38:
        return Prefix_Bamum_Letter_Phase_F
    else:
        return None

# CJK Compatibility Ideograph skip function.
# CJK Compatibility Ideograph name always followed by code point.
# So, there's no reason to write the names in database.
#
def is_cjk_compat(code_point):
    if (0xF900 <= code_point and code_point <= 0xFAD9) or \
        (0x2F800 <= code_point and code_point <= 0x2FA1D):
        return True
    else:
        return False

# Text data for making auto generated source files
comment = '''//  This file generated automatically using 'ucd-tool.py'.
//  You can find the author and the copyright in file 'tools/ucd-tool.py'.
'''

boilerplate_gc_cpp_1 = comment + '''//
//  General category(gc) of Unicode code points.
#include <seshat/unicodedata.h>

#include <cstdint>
#include <map>

namespace seshat {

'''

boilerplate_gc_cpp_2 = '''

} // namespace seshat
'''

boilerplate_name_cpp_1 = comment + '''//
//  Name for individual code points.
#include <seshat/unicodedata.h>

#include <cstdint>
#include <map>

namespace seshat {
'''
boilerplate_name_cpp_2 = '''

} // namespace seshat
'''

def download_data():
    if 'UnicodeData.txt' not in os.listdir('./data'):
        os.system('wget http://www.unicode.org/Public/UNIDATA/UnicodeData.txt -O data/UnicodeData.txt')

def parse_unicode_data():
    unicode_data_list = []
    f = open('data/UnicodeData.txt', 'r')
    for l in f.readlines():
        udata = UnicodeData()
        udata.parse(l)
        unicode_data_list.append(udata)
    f.close()

    return unicode_data_list

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'clean':
            os.system('rm -v data/UnicodeData.txt')
            exit()
        elif sys.argv[1] == '--help':
            print('Usage: ./ucd-tool.py [--help] <command>')
            print('Commands')
            print('  clean    remove all downloaded data')
            print('Arguments')
            print('  --help   print this help')
            exit()

    download_data()

    unicode_data_list = parse_unicode_data()

    # Make gc.cpp
    gc_cpp_table_size = int(unicode_data_list[-1].code, base=16)
    gc_cpp_table = '''
const std::map<uint32_t, Gc> gc_table = {
    '''

    for udata in unicode_data_list:
        if udata.name in ranged_list:
            continue
        cp = '0x' + udata.code
        gc_cpp_table += ('{ ' + cp + ', Gc::' + udata.general_category + ' },')
        gc_cpp_table += '\n    '
    gc_cpp_table = gc_cpp_table.rstrip().rstrip(',')
    gc_cpp_table += '\n};'

    f = open('../src/gc.cpp', 'w')
    f.write(boilerplate_gc_cpp_1 + gc_cpp_table + boilerplate_gc_cpp_2)
    f.close()

    # Make name.cpp
    name_cpp_table = '''
const std::map<uint32_t, const char*> name_table = {
    '''

    for udata in unicode_data_list:
        if udata.name in ranged_list or udata.name == '<control>':
            continue
        cp = '0x' + udata.code
        if is_cjk_compat(int(cp, base=16)) == True:
            continue
        name = udata.name
        prefix = search_prefix(int(cp, base=16))
        if prefix != None:
            name = name[len(prefix):].lstrip()
        name_cpp_table += '{ ' + cp + ', "' + name + '" },'
        name_cpp_table += '\n    '
    name_cpp_table = name_cpp_table.rstrip().rstrip(',')
    name_cpp_table += '\n};'

    f = open('../src/name.cpp', 'w')
    f.write(boilerplate_name_cpp_1 + name_cpp_table + boilerplate_name_cpp_2)
    f.close()