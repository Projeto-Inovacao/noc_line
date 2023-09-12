// Função pra redirecionar pras paginas..
function home() {
  window.location = 'index.html'
}

function login() {
  var token = input_token.value
  var senha = input_senha.value

  if (token != '' && senha != '') {
    Swal.fire({ icon: 'success', title: 'Login realizado com sucesso!' })
  } else {
    Swal.fire({ icon: 'error', title: 'Login inválido!' })
  }
}

function cadastro() {
  var razao_social = input_razao_social.value
  var cnpj = input_cnpj.value
  var email = input_email.value
  var senha = input_senha.value

  if (razao_social != '' && cnpj != '' && email != '' && senha != '') {
    Swal.fire({ icon: 'success', title: 'Cadastro realizado com sucesso!' })
  } else {
    Swal.fire({ icon: 'error', title: 'Cadastro inválido!' })
  }
}
