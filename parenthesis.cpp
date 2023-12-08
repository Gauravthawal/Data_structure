#include<iostream>
using namespace std;
 class stack
 {
  public:
    int top = -1 ;
    const static int size = 100;
    char array[size];

    void push(char x)
    {
        if(top == size -1)
        {
            cout<<"stack is overflow:";
            return  ;
        }
        else
        {
             array[++top] = x;
        }
    }

    char pop()
    {
        if(top == -1)
        {
            cout<<" stack is underflow:";
            return -1;
        }
        else
        {
           return array[top--];
        }
    }

    void display()
    {
        if(top == -1)
        {
            cout<<" stack is empty";
        }

        cout<<" stack contains:";
        for(int i = 0 ; i<top;i++)
        {
            cout<<array[i]<<"  ";

        }
        cout<<endl;
    }

    char peek()
    {
        return array[top];
    }
    
    bool isEmpty()
    {
        if(top == -1)
        {
            return 1 ;
        }
        else{
            return 0 ;
        }
    }

 };

 int main()
 {
    stack bracket ;
    string s;
    cout<<"enter the parathesis to check balancing ";
    cin>>s;


    bool is_balanced = true;
    for( int i =0 ; i <s.size(); i++)
    {
       if(s[i] == '(' or s[i] == '{' or s[i]=='[')
       {
        bracket.push(s[i]);
       }
       else if(s[i] ==')' or s[i]== '}' or s[i] ==']')
       {
        if(bracket.isEmpty())
        {
            is_balanced = false;
            break;
        }
        char last_bracket =bracket.peek();

        if(s[i]==')' and last_bracket == '('){

            bracket.pop();
        }
        else if(s[i] == '}' and last_bracket == '{'){
            bracket.pop();
        }
        else if(s[i] == ']' and last_bracket == '['){
            bracket.pop();
        }
     }
 }
    if(not bracket.isEmpty())
    {
        is_balanced = false;

    }
    if(is_balanced)
    cout<< s <<"is balanced."<<endl;

    else
    cout<<s<<"string is not balnced."<<endl;
 }
