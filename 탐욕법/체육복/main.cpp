#include <string>
#include <vector>

using namespace std;

int arr[32];

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = n - lost.size();
    for(int i=0; i<reserve.size(); i++)
        arr[reserve.at(i)]++;
    for(int i=lost.size()-1; i>=0; i--){
        for(int j=reserve.size()-1; j>=0; j--){
            if (reserve.at(j) == lost.at(i)){
                arr[reserve.at(j)]--;
                reserve.erase(reserve.begin()+j);
                lost.erase(lost.begin()+i);
                answer++;
                break;
            }
        }
    }
    int head=0;
    int rear=lost.size() - 1;
    while(rear > head){
        int crnt_head = lost.at(head);
        int crnt_rear = lost.at(rear);
        if (arr[crnt_head-1]){
            arr[crnt_head-1]--;
            answer++;
        }
        else if (arr[crnt_head+1] ){
            arr[crnt_head+1]--;
            answer++;
        }
        head++;
        
        if (arr[crnt_rear+1]){
            arr[crnt_rear+1]--;
            answer++;
        }
        else if (arr[crnt_rear-1] ){
            arr[crnt_rear-1]--;
            answer++;
        }
        rear--;
    }
    if (head==rear && (arr[lost.at(head)+1] || arr[lost.at(head)-1] ) )
            answer++;
    
    return answer;
}