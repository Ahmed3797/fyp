
const submit_btn = document.querySelector(".submit_btn");
const candidate_pic = document.querySelector(".candidate_pic");
const candidate_name = document.querySelector(".candidate_name");
const interview_questions_container=document.querySelector('.interview_questions_container')
 const questions_count_container=document.querySelector('.questions_count_container')
const instruction_modal=document.querySelector('.instruction_modal')


setTimeout(function() {
    $('#exampleModal').modal('show');
  }, 3000);
  function closeModal() {
    $('#exampleModal').modal('hide');
  }
// ===================================================================================



// ========================================================================




const confirmQuit = () => {
    const quit = confirm("Are you sure to quit the test?");

    if (quit == true) {
        // if user moves to his profile while interview, interview terminated
        //API call send to server with filled questionsAnswerArray
        console.log("perform the test submission");
    }
};

// if candidate leave the interview page to move to his profile interview is terminated
candidate_pic.addEventListener("click", () => {
    confirmQuit();
});
candidate_name.addEventListener("click", () => {
    confirmQuit();
});

// ================================================================
// document.addEventListener("contextmenu", function (e) {
//     e.preventDefault();
// });

// document.addEventListener("selectstart", function (e) {
//     e.preventDefault();
// });
// ====================================================



// ====================================================================

// =============================================================




// ======================================================================================
//getting save buttons for each question
const interview_ques_save_btn = interview_questions_container.querySelectorAll(
    ".interview_ques_save_btn"
);
//getting all the questions
const interview_question = interview_questions_container.querySelectorAll(".interview_question");
//getting all answers for questions
const interview_question__answer = interview_questions_container.querySelectorAll(
    ".interview_question__answer "
);

//accessing count numbr of each question
const questionsCount= questions_count_container.querySelectorAll('.ques_count')
const questionsCountArray=Array.from(questionsCount)

//ALL save buttons related to questions comes with nodelist when queryselector all applied
//so converting nodelist to array
let allSaveButtons = Array.from(interview_ques_save_btn);
let allAnswers = Array.from(interview_question__answer);

allSaveButtons.forEach((btn, index) => {
    btn.addEventListener("click", () => {
        allAnswers.forEach((answer, ansIndex) => {
            if (ansIndex == index) {    //when textarea/answer Array index matches the index of save btn means save btn is related to
                // that answer 
                let obj = {
                    ques: arrayof_Questions_from_Interview_Creation_Page[index],  
                    ans: answer.value,
                };

                //if user writes answer for question 1 and then write ans for question 5 then in the final array of question/answers
                // all the answers are set to "" empty. if candidate dont save those question by default "" answer is saved
                for (let i = 0; i < ansIndex; i++) {
                    if (
                        questionAnswerArray[i] == "" ||
                        questionAnswerArray[i] == null ||
                        questionAnswerArray[i] == undefined
                    ) {
                        let obj = {
                            ques: arrayof_Questions_from_Interview_Creation_Page[i],
                            ans: "",
                        };
                        questionAnswerArray[i] = obj;
                    }
                }



                // if candidate add answers for remaining question, "" empty answer is overridden
                questionAnswerArray[index] = obj;
                btn.style.backgroundColor="rgb(17, 180, 17)"
                btn.style.color="white"
                questionsCountArray[index].style.backgroundColor="rgb(17, 180, 17)"
                questionsCountArray[index].style.color="white"
                console.log(questionAnswerArray, "question and answers");
            }
        });
    });
});
// ===================================================================