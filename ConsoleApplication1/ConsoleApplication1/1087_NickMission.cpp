

/*
描述

尼克每天上班之前都连接上英特网，接收他的上司发来的邮件，这些邮件包含了尼克主管的部门当天要完成的全部任务，每个任务由一个开始时刻与一个持续时间构成。

尼克的一个工作日为nn分钟，从第11分钟开始到第nn分钟结束。当尼克到达单位后他就开始干活，公司一共有kk个任务需要完成。如果在同一时刻有多个任务需要完成，尼克可以任选其中的一个来做，而其余的则由他的同事完成，反之如果只有一个任务，则该任务必需由尼克去完成，假如某些任务开始时刻尼克正在工作，则这些任务也由尼克的同事完成。如果某任务于第pp分钟开始，持续时间为tt分钟，则该任务将在第(p + t - 1)(p+t−1)分钟结束。

写一个程序计算尼克应该如何选取任务，才能获得最大的空暇时间。


输入
输入数据第一行含两个用空格隔开的整数nn和kk。

接下来共有kk行，每一行有两个用空格隔开的整数pp和tt，表示该任务从第pp分钟开始，持续时间为tt分钟。


输出
输出文件仅一行，包含一个整数，表示尼克可能获得的最大空暇时间。

输入样例：
15 6
1 2
1 6
4 11
8 5
8 1
11 5

输出样例：
4
*/

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

	Task leading_task[10000] = { 0 };

	int leading_task_cnt = 0;

	int leading_p = 0;

	//第一个有效 可是assign的task index
	int leading_task_index = 0;

	//从leading task 结尾开始的最大spare time
	int spare_without_leading_task = 0;

	//排除任务队列前面已经开始的task
	for (int i = 0; i < count; i++)
	{
		if (taskv[i].p < start_p)
			leading_task_index++;
	}


	if (leading_task_index < count)
	{
		//找出当前可开始的 平行task 数量
		leading_p = taskv[leading_task_index].p;

		for (int i = leading_task_index; i < count ; i++)
		{
			if (taskv[i].p == leading_p)
			{
				leading_task[leading_task_cnt++] = taskv[i];
			}
			else
			{
				break;
			}
		}
	}

	if (leading_task_cnt > 0)
	{
		//计算最先开始的任务开始点之前和工作时间段开始点之间的空闲时间。
		max_spare_time += leading_p - start_p;

		for (int i = 0; i < leading_task_cnt; i++)
		{
			int spare_tmp = 
				find_slot_max(&taskv[leading_task_cnt], count - leading_task_cnt, leading_task[i].p + leading_task[i].t, end_p);
			if (spare_without_leading_task < spare_tmp)
			{
				spare_without_leading_task = spare_tmp;
			}
		}
	}
	else
	{
		//计算最先开始的任务开始点之前和工作时间段开始点之间的空闲时间。
		max_spare_time = end_p - start_p + 1;
	}

	max_spare_time += spare_without_leading_task;

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
