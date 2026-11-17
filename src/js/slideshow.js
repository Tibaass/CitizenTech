// Slideshow das personas (página Público Alvo)
const trilho = document.querySelector('.slides-trilho');
const slides = document.querySelectorAll('.slides-trilho .persona-card');
const indicadores = document.querySelector('.slide-indicadores');
const botaoAnterior = document.querySelector('.slide-anterior');
const botaoProximo = document.querySelector('.slide-proximo');
let slideAtual = 0;

function irParaSlide(indice) {
    slideAtual = (indice + slides.length) % slides.length;
    trilho.style.transform = 'translateX(-' + (slideAtual * 100) + '%)';
}

botaoAnterior.addEventListener('click', function () {
    irParaSlide(slideAtual - 1);
});

botaoProximo.addEventListener('click', function () {
    irParaSlide(slideAtual + 1);
});

irParaSlide(0);
