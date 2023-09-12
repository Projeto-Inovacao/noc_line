package LOGIN

import java.util.Scanner

fun main() {
    val login = Login()
    val tk = Scanner(System.`in` )
    println("Token de Acesso")
    val userToken = tk.nextLine()
    println(userToken)


    val sn = Scanner(System.`in`)
    println("Senha")
    val userPassword = sn.nextLine()
    login.senha = userPassword
    println(userPassword)


}