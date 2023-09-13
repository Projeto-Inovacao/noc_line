import java.util.Scanner
fun main() {

    val reader = Scanner(System.`in`)
    print("Digite seu email: ")
    var email = reader.nextLine()

    print("Digite sua senha: ")
    var senha = reader.nextLine()

    print("Digite seu Token: ")
    var token = reader.nextLine()

    if (email == "jose@nocline.com" && senha == "323" && token == "#IamNocLine"){
        println("lOGIN REALIZADO COM SUCESSO")
    }
    else {
        println("Algo deu errado")
    }
}