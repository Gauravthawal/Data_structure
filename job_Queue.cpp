#include<iostream>
using namespace std;
class Queue
{
    public :
    const static int size = 100;
    int start = -1 ;
    int end = -1;
    int array[size] ;

    void push(int x)
    {
        if(end == size -1)
        {
            cout<<" QUeue is overflow";
        }
        else
        {
            array[++end] = x;
        }

    }
    int pop()
    {
        if(start == -1 && end ==-1)
        {
             cout<<" QUeue is underflow"<<endl;
             return -1 ;
        }
        return array[++start];
        
    }
    void display()
    {
        if(start == -1 && end ==-1)
        {
             cout<<" QUeue is Empty"<<endl;
             
        }
        else{
            cout<<"queue contains:"<<endl;
            for(int i = start +1;i<= end ; i++)
            {
                cout<<array[i]<<" ";
            }
            cout<<endl;

        }
    }
};
void add_job(Queue &q ,int job)
{
    q.push(job);
}
void delete_job( Queue &q)
{
    q.pop();
}

int main()
{
    Queue job_line;
   
    add_job( job_line ,10);
    add_job( job_line ,102);
    add_job( job_line ,140);
    add_job( job_line ,150);
    add_job( job_line ,170);
    add_job( job_line ,109);
    job_line.display();
    delete_job(job_line);
    job_line.display();
    
    return 0;
}