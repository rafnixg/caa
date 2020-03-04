
// let type = localStorage.getItem('type')

// if (type === 'student')  {
//     type = 'delegate'
// } else if (type === 'delegate') {
//     type = 'student'
// } else {
//     type = 'generic'
// }

// const items = document.getElementsByClassName(type)
// for (let item of items) {
//     item.classList.add('d-none')
// }

// REGISTER TABS
// const nextButton = document.getElementById('next')

// if (nextButton) {
//     nextButton.addEventListener('click', (event) => {
//         // jQuery for Boostrap Tabs

//         const tab_init = $('a[aria-selected=true]').attr('href')
//         if((type === 'student' || type === 'delegate') && tab_init==='#data'){
//             $('a[aria-selected=true]').parent('li').next().next().children('a').tab('show')
//             const tab = $('a[aria-selected=true]').attr('href')

//         }else{

//             $('a[aria-selected=true]').parent('li').next().children('a').tab('show')
//             const tab = $('a[aria-selected=true]').attr('href')
//         }

//         if (tab === '#confirm') {
//             const actionButtons = document.getElementById('action-buttons')
//             actionButtons.classList.add('d-none')
//         }
//     })
// }


// REGISTER FORM
const addAssistantButton = document.getElementById('addAssistant')
const submitAssistantButton = document.getElementById('submitAssistant')

if (addAssistantButton) {
    addAssistantButton.addEventListener('click', (event) => {
        const forms = document.getElementsByName('assistantForm')
        const form = document.createElement('div')
        form.setAttribute('class','form-group row mb-4')
        form.setAttribute('name', 'assistantForm')
        form.innerHTML = forms[0].innerHTML

        const formsContainer = document.getElementById('forms')
        formsContainer.appendChild(form)
    })
}

if (submitAssistantButton){
    submitAssistantButton.addEventListener('click', (event) => {
        document.getElementById('forms').submit()

    })
}