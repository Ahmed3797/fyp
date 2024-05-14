const add_profile_image_input=document.querySelector('#add_profile_image_input');
const profile_pic=document.querySelector('.profile_pic');
const profile_edit_icon=document.querySelector('.profile_edit_icon')

profile_pic.addEventListener('click',()=>{
    add_profile_image_input.click()  
})
profile_edit_icon.addEventListener('click',()=>{
    add_profile_image_input.click() 
})
profile_pic.addEventListener('mouseover',()=>{
    profile_edit_icon.style.display='block'
})
profile_edit_icon.addEventListener('mouseover',()=>{
    profile_edit_icon.style.display='block'
})
profile_pic.addEventListener('mouseout',()=>{
    profile_edit_icon.style.display='none'
})



