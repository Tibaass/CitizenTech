const palavras_suspeitas = {"premio": 20, "parabens": 5, "ganhou": 10, "clique": 20, "aqui": 5, "receber": 10, "urgente": 20, "transferencia": 20, "pix": 20, "senha": 20, "cartao": 15, "banco": 15, "dinheiro": 10, "oferta": 10, "desconto": 10, "grátis": 10, "vencedor": 10, "prêmio": 15, "ganhador": 15}
const links_suspeitos = ["http://", "https://", "www.", "bit.ly"]
const botaoApertado = document.getElementById('form-verificador')

botaoApertado.addEventListener('submit', function(event) {
    event.preventDefault();
    const mensagemEnviada = document.getElementById('mensagem').value.trim();
    const mensagemPontuacao = CalcularPontuacaoMensagemUsuario(mensagemEnviada);
    AtribuirCriticidadeMensagem(mensagemPontuacao)
})

function CalcularPontuacaoMensagemUsuario(mensagem){
    let textosSuspeitosNaMensagem = 0
    let pontuacao = 0
    let qtdPalavrasMensagem = (mensagem.split(` `)).length
    
    // Primeira verificação de Palavras Suspeitas
    for (let palavra in palavras_suspeitas) {
        if (mensagem.toLowerCase().includes(palavra)){
            pontuacao += palavras_suspeitas[palavra];
            textosSuspeitosNaMensagem += 1
        }
    }

    // 2º Verficação de Links na Mensagem
    for (let link of links_suspeitos) {
        if (mensagem.toLowerCase().includes(link)){
            pontuacao += 20
            textosSuspeitosNaMensagem += 1
        }
    }

    // Média de Palavras Encontradas e Palavras Totais
    let mediaTotal = textosSuspeitosNaMensagem / qtdPalavrasMensagem
    if (mediaTotal > 0.2) pontuacao += 20
    return pontuacao
}

function AtribuirCriticidadeMensagem(pontuacao){
    if (pontuacao >= 61){
        window.location.href = "golpe.html";
    } else if(pontuacao >= 40 && pontuacao <= 60) { 
        window.location.href = "suspeito.html";
    } else {
        window.location.href = "nogolpe.html";
    }
}
