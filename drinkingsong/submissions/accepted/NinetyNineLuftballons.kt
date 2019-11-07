fun plural(n : Int) : String =
    "${if (n==0) "no more" else "$n"} bottle${if (n==1) "" else "s"} of"

fun main(args: Array<String>) {
    val N = readLine()?.toInt() ?: 0
    val drink = readLine() ?: "beer"
    for (n in N downTo 1) 
        println("""
${plural(n)} $drink on the wall, ${plural(n)} $drink.
Take ${if (n > 1) "one" else "it"} down, pass it around, ${plural(n-1)} $drink${if (n > 1) " on the wall" else ""}.""")
}
