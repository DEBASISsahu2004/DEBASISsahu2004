#include<iostream>
using namespace std;

int main(){
	int num, size=0;
	cout << "Enter a number : ";
	cin >> num;
	
	if(num<=99){
		cout << "No middle number";
	}else{
		// To get size
		int dummy = num;		
		while(dummy != 0){
			dummy = dummy / 10;
			size++;
		}
		// Storing the elements in array
		dummy = num;
		int arr[size], r,i=0;
		while(dummy!=0){
			r = dummy % 10;
			arr[i]=r;
			dummy /= 10;
			i++;
		}
		// printing the middle element
		int s = size/2;
		if(size%2==0){
			cout << "Middle elements are : " << arr[s] << arr[s-1];
		}else{
			cout << "Middle elements is : " << arr[s];
		}
		
	return 0;
	}
}
