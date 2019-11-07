fun turn(s : String) : String {
    val R = StringBuilder()
    for (x in s.reversed()) R.append(when(x) {
        '6' -> '9'
        '9' -> '6'
        in "018" -> x
        else -> return s
    })
    val r = R.toString()
    return if (s < r) s else r
}

fun main(args: Array<String>) {
    readLine()
    println(generateSequence(::readLine)
        .map{turn(it)}
        .sortedWith(Comparator<String>{a,b -> (a+b).compareTo(b+a)})
        .joinToString(""))
}