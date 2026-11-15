#include<iostream>
using namespace std;
class A{
    int x = 9;
    friend class B;
    public:
     A (int i){
      cout << "A's class called" << endl;
    }
};
class B {
  public:
  void print(A obj){
    cout << obj.x << endl;
  }
};
class C:public A{
  public:
    C (): A(3){

      cout << "C's class called" << endl;
    }
};
int main (){
  A obj{3};
  B obj2;
  C obj3;
  obj2.print(obj);
}