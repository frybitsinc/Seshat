/*
//  tests/string.cpp
//
//  Author:     Sophia Lee
//  Created:    2017. 05. 26. 11:40
//  Copyright (c) 2017 Sophia Lee. All rights reserved.
//
//
*/
#include <seshat/string.h>

#include <cassert>
#include <iostream>

int main()
{
    using seshat::CodePointSequence;
    using seshat::String;

    CodePointSequence seq = {
        'D', 0x0323
    };
    String s1 = String(seq);
    String s2 = String(CodePointSequence{ 'T', 'e', 's', 't' });
    String s3 = {
        'T', 'e', 's', 't'
    };
    String s4 = "UTF-8 テスト"; // count: 9

    std::cout << "s1.count(): " << s1.count() << std::endl;
    std::cout << "s2.count(): " << s2.count() << std::endl;
    std::cout << "s3.count(): " << s3.count() << std::endl;
    std::cout << "s4.count(): " << s4.count() << std::endl;

    s2 += String { '!', '!' };
    assert(s2.count() == 6);
    assert(s2 == (String { 'T', 'e', 's', 't', '!', '!' }));

    auto iter = s2.begin();
    ++iter; ++iter; // iter points 's'
    s2.insert(iter, seshat::CodePoint(0x0301));
    std::cout << "s2.to_utf8(): " << s2.to_utf8() << std::endl;
    assert(s2.count() == 6);

    // Count
    { // GB10
        String count_gb10 = {
            0x261D, 0x1F3FB,  // index pointing up: light skin tone
            0x1F469, 0x1F3FF, // woman: dark skin tone
            0x1F930, 0x1F3FD  // pregnant woman: medium skin tone
        }; 
        assert(count_gb10.count() == 3);
    }
    { // GB11
        String count_gb11 = {
            0x1F469, 0x200D, 0x2764, 0xFE0F, 0x200D, 0x1F48B, 0x200D, 0x1F469,
                // kiss: woman, woman
            // 0x1F469, 0x1F3FE, 0x200D, 0x1F3A4,
                // woman singer: medium-dark skin tone
                // Emoji ZWJ Sequence break not works properly since it
                // requires CLDR expanded rule.
            0x1F441, 0xFE0F, 0x200D, 0x1F5E8, 0xFE0F
                // eye in speech bubble
        };
        assert(count_gb11.count() == 2);
    }
    { // GB12, GB13
        String count_gb12_gb13 = {
            0x1F1E6, 0x1F1E8, // Ascension Islan
            0x1F1E6, 0x1F1E8, // Ascension Islan
            0x1F1E6 // REGIONAL INDICATOR SYMBOL LETTER A
        };
        assert(count_gb12_gb13.count() == 3);
    }

    return 0;
}
