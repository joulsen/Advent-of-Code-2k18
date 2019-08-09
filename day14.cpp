#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void partOne(vector<int> score, int input){
    for (int i = 0; i <= 9; i++){
        cout << score[input+i];
    }
}

void tick(vector<int> &score, unsigned long int &elf1, unsigned long int &elf2){
    int total = score[elf1] + score[elf2];
    if(total < 10){
        score.push_back(total);
    } else {
        score.push_back(total / 10);
        score.push_back(total % 10);
    }
    elf1 = (elf1 + score[elf1] + 1) % score.size();
    elf2 = (elf2 + score[elf2] + 1) % score.size();
}

bool check(vector<int> score, vector<int> in){
    return (search(score.begin(), score.end(), in.begin(), in.end()) != score.end());
}

vector<int> getLastN(vector<int> score, int n){
    return vector<int>(score.begin() + score.size() - n, score.end());
}

int main(){
    const int input = 920831;
    int i = input;
    vector<int> score{3,7};
    vector<int> inputVector;
    while(i > 0) {
        inputVector.push_back(i % 10);
        i /= 10;
    }
    reverse(inputVector.begin(), inputVector.end());
    unsigned long int elf1 = 0;
    unsigned long int elf2 = 1;

    while(!(check(getLastN(score, inputVector.size()+2), inputVector))){
        tick(score, elf1, elf2);
        if(score.size() > 1000000){
            break;
        }
    }
    print(getLastN(score, 5));
    cout << score.size() - inputVector.size();
}
