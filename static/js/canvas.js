const canvas = document.getElementById('croquiCanvas'); // Obtém o elemento HTML <canvas> pelo seu ID 'croquiCanvas'
const ctx = canvas.getContext('2d'); // Obtém o contexto de renderização 2D para desenhar na tela
let desenhando = false; // Cria uma variável de controle para saber se o usuário está com o botão do mouse pressionado

const croquiRef = database.ref('croquis/sala_1/linhas'); // Cria uma referência no Firebase Realtime Database no caminho 'croquis/sala_1/linhas'

canvas.addEventListener('mousedown', () => desenhando = true); // Ativa o modo de desenho quando o botão do mouse é pressionado sobre o canvas
canvas.addEventListener('mouseup', () => { // Adiciona um ouvinte para o evento de soltar o botão do mouse no canvas
    desenhando = false; // Desativa o modo de desenho ao soltar o mouse
    ctx.beginPath(); // Reseta o caminho atual do desenho para não conectar linhas ao iniciar um novo traço
}); // Fecha o manipulador do evento 'mouseup'

canvas.addEventListener('mousemove', (e) => { // Adiciona um ouvinte para registrar o movimento do mouse sobre o canvas
    if (!desenhando) return; // Cancela a execução da função se o usuário não estiver pressionando o mouse (desenhando)

    const rect = canvas.getBoundingClientRect(); // Obtém o tamanho do canvas e sua posição relativa à tela
    const ponto = { // Cria um objeto contendo os dados do ponto atual
        x: e.clientX - rect.left, // Calcula a posição X do clique relativa à borda esquerda do canvas
        y: e.clientY - rect.top, // Calcula a posição Y do clique relativa à borda superior do canvas
        cor: document.getElementById('colorPicker').value, // Captura a cor selecionada no elemento de input 'colorPicker'
        espessura: document.getElementById('strokeWidth').value, // Captura a espessura da linha selecionada no input 'strokeWidth'
        timestamp: Date.now() // Registra a data/hora exata em milissegundos para ordenação/histórico
    }; // Fecha a definição do objeto 'ponto'

    // Envia o ponto para o Firebase em tempo real
    croquiRef.push(ponto); // Adiciona o objeto 'ponto' como um novo registro dentro do caminho no Firebase
}); // Fecha o manipulador do evento 'mousemove'

// Escuta novos pontos enviados por qualquer usuário conectado
croquiRef.on('child_added', (snapshot) => { // Registra um ouvinte no Firebase que dispara sempre que um novo ponto é adicionado à lista
    const p = snapshot.val(); // Extrai os dados do objeto do ponto gravado no banco de dados
    desenharPonto(p.x, p.y, p.cor, p.espessura); // Chama a função para desenhar o ponto na tela usando os dados recebidos
}); // Fecha o manipulador do evento do Firebase

function desenharPonto(x, y, cor, espessura) { // Define a função responsável por desenhar as linhas no canvas
    ctx.lineWidth = espessura; // Define a largura da linha de contorno do desenho
    ctx.lineCap = 'round'; // Define as extremidades das linhas como arredondadas
    ctx.strokeStyle = cor; // Define a cor da linha de contorno

    ctx.lineTo(x, y); // Desenha uma linha da posição anterior até a coordenada (x, y) informada
    ctx.stroke(); // Renderiza visualmente o traço da linha no canvas
    ctx.beginPath(); // Limpa o caminho atual para iniciar um novo segmento
    ctx.moveTo(x, y); // Move o cursor de desenho para a posição atual (x, y) sem desenhar nada
} // Fecha o bloco da função 'desenharPonto'
