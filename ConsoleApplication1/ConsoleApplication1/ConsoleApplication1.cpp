#include <iostream>
#include <vector>
using namespace std;

typedef struct _task
{
	int p;//start time
	int t;//duration
}Task;

int find_slot_max(Task taskv[], int count, int start_p, int end_p)
{
	int max_spare_time = 0;
	Task leading_task[256];
	int leading_task_cnt = 0;

	int leading_p = taskv[0].p;

	/*for (int i = 0; i < count; i++)
	{
		if (taskv[i].p < start_p)
		{

		}
	}*/

	for (int i = 0; i < count; i++)
	{
		if (taskv[i].p == leading_p)
		{
			leading_task[leading_task_cnt++] = taskv[i];
		}
	}

	for (int i = 0; i < leading_task_cnt; i++)
	{
		
	}


	



	return max_spare_time;
}

int main(int argc, char* argv)
{
	int n, k;
	Task tsk[10000] = { 0 };
	cin >> n >> k;
	for (int i = 0; i < k; i++)
	{
		Task &task = tsk[i];
		cin >> task.p >> task.t;
	}

	cout << find_slot_max(tsk, k, 1, n);
	return 0;
}
