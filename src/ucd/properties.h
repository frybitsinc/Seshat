/*
//  ucd/properties.h
//
//  Author:     Sophia Lee
//  Created:    2017. 06. 23. 18:29
//  Copyright (c) 2017-2018 Sophia Lee. All rights reserved.
//
//  Unicode property functions that using Seshat UCD table to get
//  properties.
*/
#ifndef _SESHAT_UCD_PROPERTIES_H
#define _SESHAT_UCD_PROPERTIES_H

#include <seshat/unicode/properties.h>

#include "gc.h"
#include "gcb.h"
#include "script.h"
#include "wb.h"

namespace seshat {
namespace unicode {
namespace ucd {

Version age(uint32_t cp);
Block block(uint32_t cp);
uint8_t ccc(uint32_t cp);
Dt dt(uint32_t cp);
// Gc gc(uint32_t cp);
// Gcb gcb(uint32_t cp);
// Wb wb(uint32_t cp);
// Script script(uint32_t cp);
bool grapheme_extend(uint32_t cp);
bool cased(uint32_t cp);
bool default_ignorable_code_point(uint32_t cp);
bool variation_selector(uint32_t cp);
bool odi(uint32_t cp);
bool ogr_ext(uint32_t cp);
bool prepended_concatenation_mark(uint32_t cp);
bool white_space(uint32_t cp);
bool other_lowercase(uint32_t cp);
bool other_uppercase(uint32_t cp);
bool lowercase(uint32_t cp);
bool uppercase(uint32_t cp);
bool dash(uint32_t cp);
bool hyphen(uint32_t cp);
bool bidi_control(uint32_t cp);
bool join_control(uint32_t cp);
bool quotation_mark(uint32_t cp);
bool terminal_punctuation(uint32_t cp);
bool other_math(uint32_t cp);
bool hex_digit(uint32_t cp);
bool ascii_hex_digit(uint32_t cp);
bool oalpha(uint32_t cp);
bool ideographic(uint32_t cp);
bool diacritic(uint32_t cp);
bool extender(uint32_t cp);
bool nchar(uint32_t cp);
bool ids_binary_operator(uint32_t cp);
bool ids_trinary_operator(uint32_t cp);
bool radical(uint32_t cp);
bool unified_ideograph(uint32_t cp);
bool deprecated(uint32_t cp);
bool soft_dotted(uint32_t cp);
bool logical_order_exception(uint32_t cp);
bool oids(uint32_t cp);
bool oidc(uint32_t cp);
bool sentence_terminal(uint32_t cp);
bool pattern_white_space(uint32_t cp);
bool pattern_syntax(uint32_t cp);
bool regional_indicator(uint32_t cp);
uint32_t simple_lowercase_mapping(uint32_t cp);
uint32_t simple_uppercase_mapping(uint32_t cp);
uint32_t simple_titlecase_mapping(uint32_t cp);

} // namespace ucd
} // namespace unicode
} // namespace seshat

#endif /* _SESHAT_UCD_PROPERTIES_H */
