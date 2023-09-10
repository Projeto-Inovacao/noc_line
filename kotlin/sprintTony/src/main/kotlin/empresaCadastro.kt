import java.util.*
fun main() {
    val sn = Scanner(System. `in`)
    val listaEmpresas = mutableListOf<CadastroEmpresa>()
    val listaFuncionarios = mutableListOf<CadastroFuncionario>()

    print("*****************************************")
    print("\r\nBem Vindo ao Cadastro de Empresas!\r\n")
    print("Por Favor Preencha os Campos Abaixo:\r\n")
    print("*****************************************\r\n")

    val empresa1 = CadastroEmpresa()
    print("Nome Fantasia:")
    empresa1.razaoSocial = sn.next()
    print("CNPJ:")
    empresa1.CNPJ = sn.next()
    print("Email:")
    empresa1.email = sn.next()
    print("Senha:")
    empresa1.senha = sn.next()
    print("Confirme sua senha:")
    empresa1.confirmarSenha = sn.next()
    listaEmpresas.add(empresa1)

    if (empresa1.senha != empresa1.confirmarSenha) {
        print("Senhas diferentes! Tente novamente")
    } else {
        print("\r\nCadastro realizado com sucesso!\r\n")
        while(true){
            print("*****************************************\r\n")
            print("Bem vindo ${empresa1.razaoSocial}! \r\n")
            print("""O que deseja fazer?
                |1 - Cadastrar Funcionários
                |2 - Ver Funcionários Cadastrados
                |3 - Sair
            """.trimMargin())
            print("\r\n*****************************************\r\n")

            val opcao = sn.next().toInt()
            if(opcao == 1){
                //var contador = 1
                print("*****************************************\r\n")
                print("Cadastrando novos funcionários, preencha os campos abaixo:\r\n")
                val func1 = CadastroFuncionario()
                print("Nome:")
                func1.nome = sn.next()
                print("CPF:")
                func1.CPF = sn.next()
                print("Tipo de Acesso:")
                func1.tipoAcesso = sn.next()
                print("Senha:")
                func1.senha = sn.next()
                listaFuncionarios.add(func1)
                print("\r\nCadastro realizado com sucesso!\r\n")
            }
            if(opcao == 2){
                print("\r\n*****************************************\r\n")
                println("Você possuí ${listaFuncionarios.size} funcionários ativos!\r\n")
                print("Funcionários Cadastrados:\r\n")

                var i = 0
                while (i < listaFuncionarios.size) {
                    print("Nome:${listaFuncionarios[i].nome}, CPF:${listaFuncionarios[i].CPF}, Tipo de Acesso: ${listaFuncionarios[i].tipoAcesso} \r\n")
                    i++
                }
            }
            if(opcao == 3) {
                print("Tudo OK, saindo da aplicação!")
                break
            }
        }
    }
}