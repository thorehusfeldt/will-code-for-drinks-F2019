tailrec fun turn(s: String, i: Int, R: StringBuilder): String =
    if (i < 0) {
        val r = R.toString()
        if (s < r) s else r
    } else {
        when (val si = s[i]) {
            '6' -> turn(s, i-1, R.append('9'))
            '9' -> turn(s, i-1, R.append('6'))
            in "018" -> turn(s, i-1, R.append(si))
            else -> s
        }
    }

fun turn(s: String) = turn(s, s.length - 1, StringBuilder())

fun main(args: Array<String>) {
    readLine()
    println(generateSequence(::readLine)
        .map{turn(it)}
        .sortedWith(Comparator<String>{a,b -> (a+b).compareTo(b+a)})
        .joinToString(""))
}
