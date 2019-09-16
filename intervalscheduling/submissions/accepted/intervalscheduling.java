import java.util.*;
public class intervalscheduling
{
    static class Interval implements Comparable<Interval>
    {
	int s, f;
	Interval(int s, int f) 
	{
	    this.s = s;
	    this.f = f;
	}

	public int compareTo(Interval that)
	{
	    if (this.f == that.f) return  0;
	    if (this.f < that.f) return -1;
	    return +1;
	}
    }

    public static void main(String[] args)
    {
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	List<Interval> intervals = new ArrayList<Interval>();

	for (int i = 0; i < n; ++i)
	    intervals.add(new Interval(sc.nextInt(),sc.nextInt()));
	Collections.sort(intervals);
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
