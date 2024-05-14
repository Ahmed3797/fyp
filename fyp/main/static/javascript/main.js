const testimonial_user_pic = document.querySelector(".user_pic");
const testimonial_para = document.querySelector("#testimonial_para");
const test_control_left = document.querySelector(".test_control_left");
const test_control_right = document.querySelector(".test_control_right");

const testimonial_name = document.querySelector(".testimonial_name");

const testimonial = [
  {
    user_pic: "./static/images/user1.jpg",
    name: "Jake",
    review:
      "kkdjksjkfj Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste magni ad obcaecati facilis dicta doloribus suscipit molestiae? Officiis alias accusantium esse et iusto, nesciunt possimus perferendis tempora distinctio, ex odio beatae at dolor. Sunt atque hic nostrum eaque perferendis omnis quidem quia dolore rerum.",
  },
  {
    user_pic: "./static/images/user2.jpg",
    name: "Samra Magician",
    review:
      " user 2 Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste magni ad obcaecati facilis dicta doloribus suscipit molestiae? Officiis alias accusantium esse et iusto, nesciunt possimus perferendis tempora distinctio, ex odio beatae at dolor. Sunt atque hic nostrum eaque perferendis omnis quidem quia dolore rerum.",
  },
  {
    user_pic: "./static/images/user1.jpg",
    name: "Ali",
    review:
      "user 3 Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste magni ad obcaecati facilis dicta doloribus suscipit molestiae? Officiis alias accusantium esse et iusto, nesciunt possimus perferendis tempora distinctio, ex odio beatae at dolor. Sunt atque hic nostrum eaque perferendis omnis quidem quia dolore rerum.",
  },
];
let i = 0;
testimonial_para.innerHTML = testimonial[0].review;
testimonial_name.innerHTML = testimonial[0].name;
test_control_left.addEventListener("click", () => {
  if (i == 0) {
    i = 0;
  } else {
    i = i - 1;
    testimonial_user_pic.src = testimonial[i].user_pic;
    testimonial_para.innerText = testimonial[i].review;
    test_control_right.style.display = "block";
    test_control_left.style.display = "block";
    testimonial_name.innerHTML = testimonial[i].name;

    testimonial_para.style.transform = "translateX(-1000px)";
    testimonial_para.style.transition = ".5s";
    setTimeout(() => {
      testimonial_para.style.transform = "translateX(0px)";
    }, 300);
  }
});

test_control_right.addEventListener("click", () => {
  if (i == 2) {
    test_control_right.style.display = "none";
  } else {
    i = i + 1;
    testimonial_user_pic.src = testimonial[i].user_pic;
    testimonial_para.innerHTML = testimonial[i].review;
    test_control_right.style.display = "block";
    test_control_left.style.display = "block";
    testimonial_name.innerHTML = testimonial[i].name;
    testimonial_para.style.transform = "translateX(1000px)";
    testimonial_para.style.transition = ".5s";
    setTimeout(() => {
      testimonial_para.style.transform = "translateX(0px)";
    }, 300);
  }

  if (i == 2) {
    test_control_right.style.display = "none";
  }
});


// hero section animation
gsap.from(".hero_img_container", {
  x: 1000,
  duration: 1,
});

gsap.to(".hero_img_container", {
  x: 0,
  duration: 1,
  scrollTrigger: {
    trigger: ".hero_img_container",
  },
});


// about section animation
gsap.from("#about", {
  x: -1000,
  duration: 1,
});

gsap.to("#about", {
  x: 0,
  duration: 1,
  scrollTrigger: {
    trigger: "#about",
  },
});

// services animation

gsap.from(".services_toleft_animate", {
  x: 1000,
  duration: 1,
});

gsap.to(".services_toleft_animate", {
  x: 0,
  duration: 1,
  scrollTrigger: {
    trigger: ".services_toleft_animate",
  },
});

gsap.from(".services_toright_animate", {
  x: -1000,
  duration: 1,
});

gsap.to(".services_toright_animate", {
  x: 0,
  duration: 1,
  scrollTrigger: {
    trigger: ".services_toright_animate",
  },
});
