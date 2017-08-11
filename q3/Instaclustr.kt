fun main(args: Array<String>) {
    for (k in 1..100) {
        if (k % 3 == 0) print("Insta")
        if (k % 5 == 0) print("clustr")
        else if (k % 3 != 0) print (k)
        print("\n")
    }
}