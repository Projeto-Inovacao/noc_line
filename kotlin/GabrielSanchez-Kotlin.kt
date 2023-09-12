import  java.util.Scanner
import javax.swing.JOptionPane

fun main() {
    val scanner = Scanner(System. `in`)
    println("Digite o  nome do Usuário:")
    var nome = scanner.next()
    println("Digite a senha do usuário:")
    var senha = scanner.next()
    println("Nivel de acesso do usuário:")
    var acesso = scanner.next()
    var email = ""
    if (acesso == "SSO"){
        email = "${nome}.SSO@gmail.com"

    }else if(acesso == "CCO"){
        email = "${nome}.CCO@gmail.com"
    }
    println("Bem vindo a Noc Line")
    println("Seu nome é ${nome}")
    println("Seu email é ${email}")
    println("sua senha é ${senha}")
    println("seu nivel de acesso: ${acesso}")


}