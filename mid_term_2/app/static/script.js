// async function getQuestion(examId){
//     $.ajax({
//         url: "/getQuestion",
//         data: {
//             eId : examId
//         },
//         success: function(rs){
//             $('#question_table').empty();
//            rs.forEach(function(ele){
//                  template = `<div style='padding:10px;background-color:#232344;'>
//                 <div style='width:100%;height:10px;color:white;'>Question ${ele[0].substring(1,2)}: ${ele[1]}</div><br>
//                 <div style='color:white;'>
//                     <form id='answer_option_${ele[0]}'>
//                         <input type='radio' name='option_${ele[0]}' value='${ele[2]}'/><label for='option_${ele[0]}'>A. ${ele[2]}</label>
//                         <input type='radio' name='option_${ele[0]}' value='${ele[3]}'/><label for='option_${ele[0]}'>B. ${ele[3]}</label>
//                         <input type='radio' name='option_${ele[0]}' value='${ele[4]}'/><label for='option_${ele[0]}'>C. ${ele[4]}</label>
//                         <input type='radio' name='option_${ele[0]}' value='${ele[5]}'/><label for='option_${ele[0]}'>D. ${ele[5]}</label>
//                     </form>
//                 </div>
//             </div>`;
//             $("#question_table").append(template);
//            })
//         },
//         dataType: "json"
//       });

//     return "Success";
// }

async function recieveOTP(){
    await axios.post("/getOTP",{
        email:stdInfo.email
    }); 
}
let stdInfo;


async function loadUserLoginInfo(){
    let rp = await axios.get('/getUserLoginInfo');
    console.log(rp);
    stdInfo = rp.data.studentInfo[0];

    $("#fnameTb").val(stdInfo.fname);
    $("#fnameTb").prop( "disabled", true );

    $("#emailTB").val(stdInfo.email);
    $("#emailTB").prop( "disabled", true );

    $("#phoneTb").val(stdInfo.phone);
    $("#phoneTb").prop( "disabled", true );

    var balanceRp = await axios.get(`/balance/${stdInfo.email}`); 
    var baln = balanceRp.data.balance;
    $("#balance").val(baln);
    
}
async function calFee(ev){
    let count = $("#stIdTb").val().length;
    if(count <8)
        return;
    else{
        let feeRp = await axios.get(`/getTuition/${$("#stIdTb").val()}`);
        $("#stdFee").val(feeRp.data.student_fee);
        $("#stdFee").prop( "disabled", true );
    }

}
// function loadSubject(){
//     $.ajax({
//         url: "/getSubject",
//         success: function(rs){
//             rs.forEach(function(line){
//                 let color = '#'+Math.floor(Math.random()*16777215).toString(16);
//                 // let textColor = '#'+Math.floor(Math.random()*16777215).toString(16);
//                 let template = `<div class="subject" onclick="loadExamBySub('${line[0]}')" style="color:black;box-shadow:1px 1px 3px 3px lightblue;text-align:center;display:inline-block;background-color:${color};"><p>${line[1]}</p></div>`;
//                 $('#subjects').append(template);
//             });
//         },
//         dataType: "json"
//     });
// }

function initView(){
    loadSubject();
}


