//
//  utils.h
//
//  Author:     Sophia Lee
//  Created:    2017. 04. 14. 16:03
//  Copyright (c) 2016 Sophia Lee. All rights reserved.
//

/// \file
/// \brief  Utility functions for convenience.
#ifndef _SESHAT_UTILS_H
#define _SESHAT_UTILS_H

#include <string>
#include <utility>

namespace seshat {

/// \brief  Template class for range.
///
/// Range contains from lower to upper, that means, for every values V in range
/// satisfy lower <= V <= upper.
template <typename T>
struct Range {
    /// \brief  Lower boundary of range.
    T lower;
    /// \brief  Upper boundary of range.
    T upper;

    /// \brief  Construct the Range with lower and upper values.
    Range(const T& lower, const T& upper)
        : lower(lower), upper(upper)
    {}

    /// \brief  Returns true if the range contains the other range.
    ///
    /*! \code
     * equal if other range is in this range.
     *          ___________  <- other --->  __________________
     *      ___|___________|__             |__________________|
     *     |   |           |  | <- this -> |                  |
     *  ---.---.-----------.--.----     ---.------------------.----
     *  \endcode
     */
    /// Note that this behavior is just a trick for using key of std::map.
    bool operator==(const Range<T>& other) const
    {
        return (this->lower <= other.lower) && (this->upper >= other.upper);
    }

    /// \brief  Returns true if not this == other.
    bool operator!=(const Range<T>& other) const
    {
        return (this->lower > other.lower) || (this->upper < other.upper);
    }

    /// \brief  Returns true if the range is not overlap to and lower than
    ///         the other.
    bool operator<(const Range<T>& other) const
    {
        return (this->upper < other.lower);
    }

    /// \brief  Returns true if the range is not overlap to and greater than
    ///         the other.
    bool operator>(const Range<T>& other) const
    {
        return (this->lower > other.upper);
    }
};

/// \brief  Alias to Range<uint32_t>.
using CodePointRange = Range<uint32_t>;

/// \brief  Select a hexademical digit from given number (in hexademical).
/*!
// AT_DIGIT_32(uint32_t, int) - select a hexademical digit from given number
/// \n
// e.g. AT_DIGIT_32(0x1a3f, 3) == 10(0xa)
 */
#define AT_DIGIT_32(code, digit) \
    ((code & (0x0000000F << ((digit - 1) * 4))) >> ((digit - 1) * 4))

/// \brief  Get maxinum digit of code point in hexademical.
/*!
// CP_MAX_DIGIT(uint32_t) - Get maximum digit of code point in hexademical.
/// \n
// Only works with legal Unicode code points.
 */
#define CP_MAX_DIGIT(code) \
    ((code) <= 0xf) ? 1 : \
    (0x00010 <= (code) && (code) <= 0x000ff) ? 2 : \
    (0x00100 <= (code) && (code) <= 0x00fff) ? 3 : \
    (0x01000 <= (code) && (code) <= 0x0ffff) ? 4 : \
    (0x10000 <= (code) && (code) <= 0xfffff) ? 5 : 6

/// \brief  A char array for convert hex digit to character.
static const char HEX_CHAR[16] = {
    '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
};

/// \brief  Make std::string from code point in Unicode code point format.
///
/// Add U+ prefix to hexademical number, if digit is lower than 4, fill zeros
/// front of number.\n
/// e.g. 0x42 => "U+0042", 0x1FFFF => "U+1FFFF".\n
/// Behavior for illegal code point that over 0x10FFFF is undefined.
std::string code_point_to_string(uint32_t cp);

} // namespace seshat

#endif /* _SESHAT_UTILS_H */
