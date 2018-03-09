#include <cstdlib>
#include <iostream>
#include "../base64.h"

int main()
{
	base64_encode("Bincrafters"); //don't bother checking anything, this is just to ensure linking works.
    std::cout << "Bincrafters\n";
    return EXIT_SUCCESS;
}
