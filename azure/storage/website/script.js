// Script executado quando a página carrega
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Site carregado com sucesso!');

    // Atualiza a data atual
    atualizarData();

    // Atualiza o horário de deploy
    atualizarDeployTime();

    // Inicia o contador de visitantes
    iniciarContador();

    // Adiciona listener para Enter no input
    const nomeInput = document.getElementById('nomeInput');
    nomeInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            saudar();
        }
    });
});

// Atualiza a data atual no footer
function atualizarData() {
    const dataAtual = new Date();
    const opcoes = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    const dataFormatada = dataAtual.toLocaleDateString('pt-BR', opcoes);
    document.getElementById('data-atual').textContent = dataFormatada;
}

// Mostra o horário de deploy (simula com horário atual)
function atualizarDeployTime() {
    const agora = new Date();
    const horas = String(agora.getHours()).padStart(2, '0');
    const minutos = String(agora.getMinutes()).padStart(2, '0');
    document.getElementById('deploy-time').textContent = `${horas}:${minutos}`;
}

// Mostra mensagem quando clica no botão
function mostrarMensagem() {
    const mensagemDiv = document.getElementById('mensagem');

    const mensagens = [
        "🎉 Parabéns! Você está aprendendo Azure!",
        "⚡ Este site está super rápido, não?",
        "☁️ A nuvem é incrível!",
        "🚀 Você é um desenvolvedor de nuvem agora!",
        "💙 Azure Storage é muito fácil de usar!",
        "🎯 Você está mandando muito bem!",
        "🌟 Continue assim, você vai longe!",
        "💡 Que tal adicionar mais recursos ao site?"
    ];

    const mensagemAleatoria = mensagens[Math.floor(Math.random() * mensagens.length)];

    mensagemDiv.innerHTML = `
        <strong>✨ Mensagem especial:</strong><br>
        ${mensagemAleatoria}
    `;

    mensagemDiv.className = 'mensagem-visivel';

    // Esconde depois de 5 segundos
    setTimeout(() => {
        mensagemDiv.className = 'mensagem-oculta';
    }, 5000);
}

// Sauda o usuário pelo nome
function saudar() {
    const nomeInput = document.getElementById('nomeInput');
    const saudacaoDiv = document.getElementById('saudacao');
    const nome = nomeInput.value.trim();

    if (nome === '') {
        alert('Por favor, digite seu nome primeiro! 😊');
        nomeInput.focus();
        return;
    }

    const saudacoes = [
        `👋 Olá, ${nome}! Bem-vindo ao Azure!`,
        `🎉 Que legal ter você aqui, ${nome}!`,
        `🚀 ${nome}, você é incrível!`,
        `⭐ ${nome}, continue estudando!`,
        `💙 Prazer em conhecer você, ${nome}!`,
        `🌟 ${nome}, você está fazendo um ótimo trabalho!`
    ];

    const saudacaoAleatoria = saudacoes[Math.floor(Math.random() * saudacoes.length)];

    saudacaoDiv.textContent = saudacaoAleatoria;
    saudacaoDiv.className = 'saudacao visivel';

    // Limpa o input
    nomeInput.value = '';

    // Remove a classe depois da animação
    setTimeout(() => {
        saudacaoDiv.className = 'saudacao';
    }, 3000);
}

// Contador de visitantes simulado
function iniciarContador() {
    let visitantes = Math.floor(Math.random() * 100) + 50; // Começa com um número aleatório
    const visitorsElement = document.getElementById('visitors');

    // Anima o contador
    let atual = 0;
    const duracao = 2000; // 2 segundos
    const incremento = visitantes / (duracao / 16); // 60 FPS

    const timer = setInterval(() => {
        atual += incremento;
        if (atual >= visitantes) {
            atual = visitantes;
            clearInterval(timer);

            // Incrementa lentamente depois
            setInterval(() => {
                visitantes++;
                visitorsElement.textContent = visitantes.toLocaleString('pt-BR');
            }, 5000);
        }
        visitorsElement.textContent = Math.floor(atual).toLocaleString('pt-BR');
    }, 16);
}

// Easter egg: console
console.log('%c🚀 Azure Storage Website', 'font-size: 20px; color: #667eea; font-weight: bold;');
console.log('%cEste site está hospedado em um Azure Storage Account!', 'font-size: 14px; color: #764ba2;');
console.log('%c💡 Dica: Você pode modificar este site e fazer upload novamente!', 'font-size: 12px; color: #555;');
console.log('%cArquivos: index.html, style.css, script.js', 'font-size: 12px; color: #999;');

// Adiciona efeito de parallax suave no scroll
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const logo = document.querySelector('.logo');
    if (logo) {
        logo.style.transform = `translateY(${scrolled * 0.3}px)`;
    }
});

// Mostra no console quando o usuário interage
document.addEventListener('click', (e) => {
    if (e.target.tagName === 'BUTTON') {
        console.log(`🖱️ Botão clicado: ${e.target.textContent}`);
    }
});
