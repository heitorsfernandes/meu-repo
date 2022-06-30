
const url = 'https://api.coincap.io/v2/assets';
const list = document.getElementById('criptoList');

function append(data) {
 return data.forEach((criptoCoin) => {
 const li = document.createElement('li');
 li.innerText = `${criptoCoin.name}(${criptoCoin.symbol}):${criptoCoin.priceUsd}`;
 list.appendChild(li);
 })
} 

const fetchCripto = () => {
  const cripto = fetch(url)
    .then((response) => response.json())
    .then((data) => append(data))
    .catch((error) => console.log('ih deu ruim', error));
  console.log(cripto);

};

window.onload = () => fetchCripto();