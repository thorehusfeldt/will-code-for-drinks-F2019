tailrec fun turn(s: String, i: Int, R: StringBuilder): String {
    return if (i < 0) {
        val r = R.toString()
        if (s < r) s else r
    } else {
        R.append(when(s[i]) {
            '6' -> '9'
            '9' -> '6'
            in "018" -> s[i]
            else -> return s
        })
        turn(s, i-1, R)
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
