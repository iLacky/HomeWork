let int = document.getElementById("demo").innerHTML = Math.floor(Math.random() * 1000);
let i = 1

const myBut = document.createElement('button');
myBut.className = 'buttons';
myBut.style.textAlign = 'center';


['Add friends'].map(butonName => {
    let button = document.createElement('buton');
    button.className = 'btn btn-success';
    button.innerText = butonName;
    button.style.margin = '5px';
    myBut.appendChild(button)
})
document.getElementsByTagName('body')[0].appendChild(myBut)

const btn = document.getElementsByTagName('button')[0];
btn.addEventListener('click' ,(myButEvent) =>{
    myButEvent.target.innerText = 'Pending confirmation';
    document.getElementById('demo').innerHTML = int + i;
    myButEvent.target.disabled = true;

})
