import java.util.*;
import java.io.*;
public class intervalscheduling
{
    static class Interval 
    {
	int s, f;
	Interval(int s, int f) 
	{
	    this.s = s;
	    this.f = f;
	}
    }

    public static void main(String[] args) throws IOException
    {
	BufferedReader R = new BufferedReader(new InputStreamReader(System.in));
	int n = Integer.parseInt(R.readLine().trim());
	Interval[] intervals = new Interval[n];

	String[] tokens;
	for (int i = 0; i < n; ++i){
	    tokens = R.readLine().split(" ");
	    intervals[i] = new Interval(Integer.parseInt(tokens[0]),Integer.parseInt(tokens[1]));
	}
	Arrays.sort(intervals, (i,j) -> i.f - j.f);
	int next_idle = 0;
	int res = 0;
	for (Interval I: intervals) 
	    if (I.s >= next_idle) {
		++res;
		next_idle = I.f;
	    }
	System.out.println(res);

    }
}
