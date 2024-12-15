#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define SIZE 10
#define SIZE2 11
#define SIZE3 5
#define SIZE4 16

/*int main(){
	int num[SIZE] = {0};
	
	for (int i = 0; i < SIZE; i ++){
		num[i] = (rand()%100) + 1;
		printf("%-3d", num[i]);
	}
	printf("\n");
	int min = num[0];
	for (int i = 0; i < SIZE; i ++){
		if (min > num[i]){
			min = num[i];
		}
	}
	printf("최솟값은 %d 입니다.",min);
	return 0;
}*/

/*int main(){
	int pe[SIZE2] = { 0 }, ans = 0;;
	
	while (1){
		printf("후보자 선택(-1: 종료): ");
		scanf("%d", &ans); 
		if (ans < 0) break;
		pe[--ans]++;
	}
	printf("값 득표결과\n");
	for (int i = 0; i < SIZE2; i ++){
		printf("%3d %3d\n", i + 1, pe[i]);
	}
	return 0;
}*/

/*int main(){
	int num[SIZE3] = {0};
	int ans = 0;
	for (int i = 0; i < SIZE3; i ++){
		printf("입력: ");	scanf("%d", &ans); 
		num[i] = ans;	
	}
	
	for (int i = SIZE3 - 1; i >= 0; i --){
		printf("%3d",num[i]);
	}
}*/

/*int av_grade(int num, int grade[]);

int main(){
	int grade_st = {1, 2, 3, 4, 5};
	int num_st = 5, ave = 0;
	
	ave = av_grade(num_st, grade_st);
	
	printf ("평균: %d", ave);
	
	return 0;
}

int av_grade(int num, int grade[]){
	int all = 0;
	for (int i = 0; i < SIZE3; i ++){
		all += grade[i];
	}
	
	return all / num;
}*/

/*int main(){
	int list[SIZE] = {0,1,2,3,4,5,6,7,8,9};
	int ans_num = 0, x = 0;;
	
	printf("탐색할 값을 입력하세요: ");
	scanf("%d", &ans_num);
	
	for ( int i = 0; i < SIZE; i ++){
		if (ans_num == list[i]){
			printf("탐색 성공!\n");
			printf("인덱스: %d", i);
			x ++;
			break;
		}
	} 
	if(x <= 0)
		printf("탐색 실패!"); 

	
}*/

int sort(int list[], int key, int n);

int main(){
	int list[SIZE4] = {2,6,11,13,18,20,22,27,29,30,34,38,41,42,45,47};
	int ans_num = 0;
	
	printf("탐색할 값을 선택하세요: ");
	scanf("%d",&ans_num);
	printf("%d의 인덱스값: %d", ans_num, sort(list, ans_num, SIZE4 - 1));
	 
}
int sort(int list[], int key, int n){
	int front = 0, rear = n, mid = 0; 
	
	while (front <= rear){
		mid = front + (rear - front) / 2;
		printf("[%d %d]\n", front, rear);
		if (list[mid] > key){
			front = mid + 1;
		}
		else if (list[mid] < key){
			rear = mid - 1;
		}
		else if (list[mid] == key){
			return mid;
		}
		
		else
			return -1;
	}
}
