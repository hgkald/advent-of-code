fun main() { 
    val MAX = mapOf(
        "red" to 12,
        "green" to 13,
        "blue" to 14
    )

    var total = 0

    val games = generateSequence(::readLine)
        .map { it.split(":") }
        .toList()
    
    games.forEach { game -> 
        val gameNum = game[0].split(" ")[1].toInt()
        val values = game[1].split(",",";")
        val impossible = values.map { it.split(" ") }
            .filter { MAX.getValue(it[2]) < it[1].toInt() }
        if (impossible.isEmpty()) { 
            total = total + gameNum
        }
    }
    println(total)
   
}
