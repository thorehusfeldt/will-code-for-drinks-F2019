fun main(args: Array<String>) {
    repeat(1000) {
        val doors = "ABC".toList().shuffled()
        println(doors[0])
        val (hint, _, bottle) = readLine()!!.toList()
        println(if (bottle == '1') hint else doors[if (hint != doors[1]) 1 else 2])
        readLine()
    }
}
