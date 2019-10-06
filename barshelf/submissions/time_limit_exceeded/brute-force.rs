use std::io;
use std::io::BufRead;
use std::str;

fn main() {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    let n : usize = line.trim_end().parse().unwrap();
    line.clear();
    stdin.lock().read_line(&mut line).unwrap();
    let vec : Vec<i32> = line.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let mut res = 0;
    for i in 0..n {
        let lim = vec[i] * 2;
        let mut sum : i32 = 0;
        for x in &vec[0..i] {
            if *x > lim {
                sum += 1;
            }
        }
        res += sum as i64;
    }
    println!("{}", res);
}
