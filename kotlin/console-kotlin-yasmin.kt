import java.util.*

fun main() {
    val sn = Scanner(System.`in`)

    print("Digite seu email:")
    val email = sn.next()
    print("Digite sua senha:")
    val senha = sn.next()
    print("Digite seu token:")
    val token = sn.next()

    val splitEmail = email.split("@")
    val usuario = splitEmail[0]

    validacao(token, usuario)
}

fun validacao(token:String, usuario:String) {
    val acesso = when (token) {
        "cco-nocline" -> "CCO"
        "sso-nocline" -> "SSO"
        else -> "N/A"
    }

    when (acesso){
        "CCO" -> print("\n\rBem vindo(a) ${usuario.replaceFirstChar { if (it.isLowerCase()) it.titlecase(Locale.getDefault()) else it.toString() }} do $acesso!") //$usuario.captalize()
        "SSO" -> print("\n\rBem vindo(a) ${usuario.replaceFirstChar { if (it.isLowerCase()) it.titlecase(Locale.getDefault()) else it.toString() }} do $acesso!")
        else -> print("\n\rLogin inválido!")
    }
}


