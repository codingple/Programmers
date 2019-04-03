#include <string>
#include <vector>

using namespace std;

int arr[20];
int total;
int len;

typedef struct state{
    int idx;
    int accum;
    int s_arr[20];
}state;

void cpy (int * nw_arr, int * s_arr){
    for(int i=0; i<len; i++)
        nw_arr[i] = s_arr[i];
}

// accum == 0 -> fin
// return min(left, right) + crnt_move
int find_mn(state s){
    // current idx pressed
    s.accum -= s.s_arr[s.idx];
    // finish
    if (s.accum == 0)
        return 0;
    s.s_arr[s.idx] = 0;
    // need to press more
    // right
    state nw_right = s;
    int right = 0;
    do{
        right++;
        nw_right.idx = (nw_right.idx+1) % len;
    }while ( !nw_right.s_arr[nw_right.idx] );
    right += find_mn(nw_right);
    // left
    state nw_left = s;
    int left = 0;
    do{
        left++;
        nw_left.idx = ( (nw_left.idx-1<0)? len-1 : nw_left.idx-1 );
    }while ( !nw_left.s_arr[nw_left.idx] );
    left += find_mn(nw_left);
    
    // find minimum
    return (left<right)? left : right;
}

int solution(string name) {
    int answer = 0;
    len = name.size();
    
    // up, down pressed
    for(int i=0; i<len; i++){
        int up = name.at(i) - 'A';
        int down = 'Z' - name.at(i) + 1;
        arr[i] = (up<down)? up : down;
        total += arr[i];
    }
    answer += total;
    
    state start;
    start.idx = 0;
    start.accum = total;
    cpy(start.s_arr, arr);
    
    answer += find_mn(start);
    
    return answer;
}