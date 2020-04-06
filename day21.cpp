/**
* @file day21.cpp
* @author Andreas P.
* (https://github.com/supercigar)
*
* Today i decided to do it in C++ as i correctly assumed it would run much faster
* and i already knew, by trying to decipher the program by hand, that the program
* would take forever to simulate in Python.
*/

#include <iostream>
#include <set>
using namespace std;

volatile int reg0, reg1, reg2, reg3, reg4 = 0;

set<int> reg4_seen;
int last_unique;
int first_unique;

// This is the boolean operator check check, found on lines 0-6 in the input.
// This always returns and is such not needed.
void boolean_operator_check(){
    while (reg4 != 72) {
        reg4  = 123;
        reg4 &= 456;
    }
    reg4 = 0;
}

// Input program rewritten in C++
void program(unsigned int limit){
    unsigned int check_count = 0;

    pre_loop:
        reg3 = reg4 | 65536;        // Line 6
        reg4 = 4332021;

    outer_loop: // Line 8
        reg2 = reg3 & 255;
        reg4 = (((reg4 + reg2) & 16777215) * 65899) & 16777215;
        if (256 > reg3){ // Line 13-14
            goto check;
        } else {
            reg2 = 0;
            inner_loop:
                reg1 = reg2 + 1;
                reg1 *= 256;
                if (reg1 > reg3) {
                    goto pre_check;
                } else {
                    reg2 += 1;
                    goto inner_loop;
                }
        }

    pre_check:
        reg3 = reg2;
        goto outer_loop;
    check:
    // Control - in order to examine registry 4.
        if (check_count == 0) {
            first_unique = reg4;
        }
        if (reg4_seen.find((int) reg4) == reg4_seen.end()) {
            reg4_seen.insert((int) reg4);
            last_unique = reg4;
        }
        check_count++;
    // Continue with program
        if ((reg4 == reg0) ||  check_count > limit) {
            return;
        } else {
            goto pre_loop;
        }
}

int main(){
    program(15000);
    cout << reg4_seen.size() << " total unique values for registry 4.\n";
    cout << "Answer to part 1 is: " << first_unique << '\n';
    cout << "Answer to part 2 is: " << last_unique  << '\n';
}
