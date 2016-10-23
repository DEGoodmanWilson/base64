//
// base64
//
// Copyright © 2016 D.E. Goodman-Wilson
//

#include <gtest/gtest.h>
#include "../base64.h"

TEST(basic_functioning, decode_encode_1)
{
    std::string encoded = base64_encode("helloo");
    std::string decoded = base64_decode(encoded);
    ASSERT_EQ("aGVsbG9v", encoded);
    ASSERT_EQ("helloo", decoded);
}

TEST(basic_functioning, decode_encode_2)
{
    std::string encoded = base64_encode("hello");
    std::string decoded = base64_decode(encoded);
    ASSERT_EQ("aGVsbG8=", encoded);
    ASSERT_EQ("hello", decoded);
}

TEST(basic_functioning, decode_encode_3)
{
    std::string encoded = base64_encode("hell");
    std::string decoded = base64_decode(encoded);
    ASSERT_EQ("aGVsbA==", encoded);
    ASSERT_EQ("hell", decoded);
}