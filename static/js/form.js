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
        for(let i = 0; i < codeforces_list.length; i++){
            let index = problems_list.indexOf(codeforces_list[i])
            if(index != -1){
                problems_list.splice(index, 1)
            }
        }
    }

})

const subscribe_horoscope = document.querySelector('#subscribe_horoscope')
const subscribe_constellation = document.querySelector('#constellation_subscribe')
let constellation_problem = document.querySelector('#constellation')
let cnt_horoscope = 0

subscribe_horoscope.addEventListener('click', ()=>{
    cnt_horoscope ^= 1
    if(cnt_horoscope){
        subscribe_constellation.classList.add('is-active')
        problems_list.push(constellation_problem)
    }

    else{
        subscribe_constellation.classList.remove('is-active')
        index = problems_list.indexOf(constellation_problem)
        if(index != -1){
            problems_list.splice(index, 1)
        }
    }

    console.log(problems_list)
})


submit_button.addEventListener('click', (event)=>{
    let cnt = 0
    for(let i=0;i<problems_list.length;i++){
        tmp_value = problems_list[i].value.trim()
        if(tmp_value != '' && tmp_value != "None"){
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
