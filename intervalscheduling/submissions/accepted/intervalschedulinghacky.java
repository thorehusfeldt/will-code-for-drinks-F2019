import java.util.*;
import java.io.*;
public class intervalschedulinghacky
{
    public static void main(String[] args) throws IOException
    {
	BufferedReader R = new BufferedReader(new InputStreamReader(System.in));
	int n = Integer.parseInt(R.readLine().trim());
	long[] intervals = new long[n];

	String[] tokens;
	for (int i = 0; i < n; ++i){
	    tokens = R.readLine().split(" ");
	    long val = Integer.parseInt(tokens[0]);
	    val |= Long.parseLong(tokens[1]) << 32;

	    intervals[i] = val;
	}
	Arrays.sort(intervals);
	int next_idle = 0;
	int res = 0;
	for (int i = 0; i < n; ++i) {
	    int s = (int)( intervals[i] & 0xFFFFFFFF);
	    int f = (int)( intervals[i] >> 32);
	    if (s >= next_idle) {
		++res;
		next_idle = f;
	    }
	}
	System.out.println(res);

    }
}
