/* 1-Acesse o elemento elementoOndeVoceEsta .
2-Acesse pai a partir de elementoOndeVoceEsta e adicione uma color a ele.
3-Acesse o primeiroFilhoDoFilho e adicione um texto a ele. Você se lembra dos vídeos da aula anterior, como fazer isso?
4-Acesse o primeiroFilho a partir de pai .
5-Agora acesse o primeiroFilho a partir de elementoOndeVoceEsta .
6-Agora acesse o texto Atenção! a partir de elementoOndeVoceEsta .
7-Agora acesse o terceiroFilho a partir de elementoOndeVoceEsta .
8-Agora acesse o terceiroFilho a partir de pai . */

const elementoOndeVoceEsta = document.querySelector('elementoOndeVoceEsta');

const pai = elementoOndeVoceEsta.parentElement;
pai.style.color = 'yellow';

const primeiroFilhoDoFilho = elementoOndeVoceEsta.firstElementChild;
primeiroFilhoDoFilho.innerText = 'Tó cheio de nodes no cérebro';

const primeiroFilho = pai.firstElementChild; 

const primeiroFilho2 = elementoOndeVoceEsta.previousElementSibling; 

const text = elementoOndeVoceEsta.nextSibling; 

const terceiroFilho = elementoOndeVoceEsta.nextSibling.nextSibling; 

const terceirofilho2 = pai.lastElementChild.previousElementSibling; 