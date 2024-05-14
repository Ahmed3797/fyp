// Hover on Profile and opening select image from PC

const add_profile_image_input = document.querySelector(
  "#add_profile_image_input"
);
const profile_pic = document.querySelector(".profile_pic");
const profile_edit_icon = document.querySelector(".profile_edit_icon");

profile_pic.addEventListener("click", () => {
  add_profile_image_input.click();
});
profile_edit_icon.addEventListener("click", () => {
  add_profile_image_input.click();
});
profile_pic.addEventListener("mouseover", () => {
  profile_edit_icon.style.display = "block";
  profile_pic.style.opacity = ".5";
});
profile_edit_icon.addEventListener("mouseover", () => {
  profile_edit_icon.style.display = "block";
  profile_pic.style.opacity = ".5";
});
profile_pic.addEventListener("mouseout", () => {
  profile_edit_icon.style.display = "none";
  profile_pic.style.opacity = "1";
});

// Adding skills and Education

// after adding skill or education the skill is dynamically entered in these containers
const skills_container = document.querySelector(".skills_container");
const edu_container = document.querySelector(".edu_container");
// add buttons
const add_EduBtn = document.querySelector(".add_EduBtn");
const add_skillbtn = document.querySelector(".add_skillBtn");


const skill_added_container=document.querySelector(".skill_added_container")
const edu_added_container=document.querySelector(".edu_added_container")

const skill_cancel=document.querySelector(".skill_cancel")
const skill_save=document.querySelector(".skill_save")

const edu_cancel=document.querySelector(".edu_cancel")
const edu_save=document.querySelector(".edu_save")

skill_cancel.addEventListener("click",(event)=>{


  event.preventDefault()
  skill_added_container.style.display="none"
})

edu_cancel.addEventListener("click",(event)=>
{
  event.preventDefault()
  edu_added_container.style.display="none"
})
// const addNewSkillOrEducation = (
//   added_container_name,
//   inputClass,
//   inputPlaceHolder,
//   saveBtnName,
//   cancelBtnName,
//   destinationContainer
// ) => {
//   let htmlData = `<div class=${added_container_name}>
//   <form method="post" action="/" enctype="multipart/form-data">
//     <input type="text" class="w-100 px-2 py-1 ${inputClass} " placeholder=${inputPlaceHolder}>
//     <div class="d-flex justify-content-end">
//        <button class="btn ${saveBtnName} mx-2">Save</button>
//        <button class="btn btn-danger  ${cancelBtnName}">Cancel</button>
//        </div>
//        </form>
//        </div>`;

//   destinationContainer.insertAdjacentHTML("afterbegin", htmlData);
//   if (saveBtnName == "save_new_skillBtn" || saveBtnName == "save_new_eduBtn") {
//     const saveItem = destinationContainer.querySelector(`.${saveBtnName}`);

//     saveItem.addEventListener("click", () => {
//       const added_container = destinationContainer.querySelector(
//         `.${added_container_name}`
//       );
//       const new_skill = added_container.querySelector(`.${inputClass}`).value;
//       added_container.remove();
//       let insertedSkill = `<div class=''>
//     ${new_skill}
// </div>`;

//       destinationContainer.insertAdjacentHTML("afterbegin", insertedSkill);
//     });
//   }

//   if (
//     cancelBtnName == "cancel_new_skillBtn" ||
//     cancelBtnName == "cancel_new_eduBtn"
//   ) {
//     const cancelItem = destinationContainer.querySelector(`.${cancelBtnName}`);

//     cancelItem.addEventListener("click", () => {
//       const added_container = destinationContainer.querySelector(
//         `.${added_container_name}`
//       );
//       added_container.remove();
//     });
//   }
// };

// add_skillBtn.addEventListener("click", () => {
//   addNewSkillOrEducation(
//     "add_new_skill_input_container",
//     "new_skill",
//     "Add Skill",
//     "save_new_skillBtn",
//     "cancel_new_skillBtn",
//     skills_container
//   );
// });

add_skillbtn.addEventListener("click",()=>
{
skill_added_container.style.display="block"
})


add_EduBtn.addEventListener("click",()=>
{
edu_added_container.style.display="block"
})

// add_EduBtn.addEventListener("click", () => {
//   addNewSkillOrEducation(
//     "add_new_edu_input_container",
//     "new_edu",
//     "Add Education",
//     "save_new_eduBtn",
//     "cancel_new_eduBtn",
//     edu_container
//   );
// });


