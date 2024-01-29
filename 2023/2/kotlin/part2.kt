fun main() { 
    var total = 0

    val games = generateSequence(::readLine)
        .map { it.split(":") }
        .toList()
    
    games.forEach { game -> 
        var max = mutableMapOf(
            "red" to 0,
            "green" to 0,
            "blue" to 0
        )

        //val gameNum = game[0].split(" ")[1].toInt()
        game[1].split(",",";")
            .map { it.split(" ") }
            .forEach { colour -> 
                val num = colour[1].toInt()
                val curr = max.getValue(colour[2])
                max[colour[2]] = if (num > curr) num else curr 
            }
        total += max.values.reduce { acc, i -> acc*i }
    }

    println(total)
}
