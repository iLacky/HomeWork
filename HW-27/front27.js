let int = document.getElementById("demo").innerHTML = Math.floor(Math.random() * 1000);
let i = 1

const myDiv = document.createElement('button');
myDiv.className = 'buttons';
myDiv.style.textAlign = 'center';


['Add friends', 'Send message', 'Offer a job'].map(buttonName => {
    let button = document.createElement('button');
    button.className = 'btn btn-success';
    button.innerText = buttonName;
    button.style.margin = '5px';
    myDiv.appendChild(button)
})
document.getElementsByTagName('body')[0].appendChild(myDiv)

const btn = document.getElementsByTagName('button')[0];
btn.addEventListener('click' ,(myButEvent) =>{
    myButEvent.target.innerText = 'Pending confirmation';
    document.getElementById('demo').innerHTML = int + i;
    myButEvent.target.disabled = true;

})
