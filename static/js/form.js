const subscribe_codeforces = document.querySelector('#subscribe_codeforces')
const subscribe_codeforces_info = document.querySelectorAll('#Codeforces')
const submit_button = document.querySelector('#submit')
const alert = document.querySelector('.alert')
let problems_list = document.querySelectorAll('.basic')
let subscribe_codeforces_state = 0

problems_list = Array.from(problems_list)

subscribe_codeforces.addEventListener('click', ()=>{
    subscribe_codeforces_state ^= 1

    for(let i = 0; i<subscribe_codeforces_info.length; i++){
        subscribe_codeforces_info[i].classList.toggle('is-active')
    }
    
    if (subscribe_codeforces_state) {
        codeforces_list = document.querySelectorAll('.codeforces')
        problems_list.push(codeforces_list[0])
        problems_list.push(codeforces_list[1])
    }

    else{
        problems_list.pop()
        problems_list.pop()
    }

})


submit_button.addEventListener('click', (event)=>{
    let cnt = 0
    for(let i=0;i<problems_list.length;i++){
        if(problems_list[i].value.trim() != ''){
            cnt++
        }
    }

    if(cnt != problems_list.length){
        event.preventDefault()
        alert.classList.add('is-active')
    }

    else{
        alert.classList.remove('is-active')
    }
})