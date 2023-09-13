import java.util.Scanner
import javax.swing.JOptionPane

fun main() {
    val sn = Scanner(System.`in`)
    print ("Insira seu nome:")
    val nome = sn.next()
    print ("Insira seu email:")
    val email = sn.next()
    print ("Insira sua senha:")
    val senha = sn.next()
    validar(email, senha, nome)
}

fun validar(email: String, senha: String, nome: String, ) {

    while (true){
    if (email == "$nome.cco@gmail.com" && senha == "cco-NOCLINE") {
        print("Bem vindo a NocLine $nome - Você é do CCO ")
        break
    }
    if (email == "$nome.sso@gmail.com" && senha == "sso-NOCLINE") {
        print("Bem vindo a NocLine $nome - Você é do SSO ")
        break

    } else {
        print("Você não pode continuar, não está cadastrado")
        break
    }
    }
}